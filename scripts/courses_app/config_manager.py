"""
课程配置持久化层 - 基于JSON文件的线程安全读写
Config file: /app/data/groups_config.json
"""
import json
import os
import tempfile
import threading
import logging

logger = logging.getLogger(__name__)

CONFIG_PATH = "/app/data/groups_config.json"
_lock = threading.Lock()
_cache = None


def _load():
    """从磁盘加载JSON配置到内存缓存"""
    global _cache
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        _cache = {"courses": []}
        _save()
        logger.info("Initialized empty groups_config.json")
    else:
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                _cache = json.load(f)
            if "courses" not in _cache:
                _cache["courses"] = []
                _save()
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to load config: {e}, using empty config")
            _cache = {"courses": []}


def _save():
    """原子写入：先写临时文件，再rename，防止写入中途崩溃导致文件损坏"""
    dirname = os.path.dirname(CONFIG_PATH)
    fd, tmp_path = tempfile.mkstemp(dir=dirname, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(_cache, f, ensure_ascii=False, indent=2)
        os.rename(tmp_path, CONFIG_PATH)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


def _ensure_loaded():
    """确保缓存已加载（惰性初始化）"""
    global _cache
    if _cache is None:
        with _lock:
            if _cache is None:  # double-check
                _load()


# ==================== Course CRUD ====================

def get_all_courses():
    """返回所有课程列表（包含章节和题目）"""
    _ensure_loaded()
    with _lock:
        return list(_cache.get("courses", []))


def get_course(course_id):
    """根据ID获取单个课程"""
    _ensure_loaded()
    with _lock:
        for c in _cache.get("courses", []):
            if c["id"] == course_id:
                return dict(c)
        return None


def create_course(course_data):
    """创建新课程，自动分配ID"""
    _ensure_loaded()
    with _lock:
        courses = _cache.setdefault("courses", [])
        max_id = max((c["id"] for c in courses), default=0)
        course = {
            "id": max_id + 1,
            "title": course_data.get("title", ""),
            "description": course_data.get("description", ""),
            "visible": course_data.get("visible", True),
            "order": course_data.get("order", 0),
            "chapters": [],
        }
        courses.append(course)
        _save()
        return dict(course)


def update_course(course_id, updates):
    """更新课程属性"""
    _ensure_loaded()
    with _lock:
        for c in _cache["courses"]:
            if c["id"] == course_id:
                for k in ("title", "description", "visible", "order", "contest_id"):
                    if k in updates:
                        c[k] = updates[k]
                _save()
                return dict(c)
        return None


def delete_course(course_id):
    """删除课程及其所有章节"""
    _ensure_loaded()
    with _lock:
        _cache["courses"] = [c for c in _cache["courses"] if c["id"] != course_id]
        _save()
        return True


# ==================== Chapter CRUD ====================

def get_chapters(course_id):
    """获取课程的所有章节"""
    course = get_course(course_id)
    return list(course.get("chapters", [])) if course else []


def _find_chapter(course, chapter_id):
    """在课程中查找章节，返回(chapter_dict, index)或(None, -1)"""
    for i, ch in enumerate(course.get("chapters", [])):
        if ch["id"] == chapter_id:
            return ch, i
    return None, -1


def create_chapter(course_id, chapter_data):
    """在课程中创建新章节"""
    _ensure_loaded()
    with _lock:
        for c in _cache["courses"]:
            if c["id"] == course_id:
                max_id = max((ch["id"] for ch in c.get("chapters", [])), default=course_id * 100)
                chapter = {
                    "id": max_id + 1,
                    "title": chapter_data.get("title", ""),
                    "visible": chapter_data.get("visible", True),
                    "order": chapter_data.get("order", 0),
                    "problems": [],
                }
                c.setdefault("chapters", []).append(chapter)
                _save()
                return dict(chapter)
        return None


def update_chapter(course_id, chapter_id, updates):
    """更新章节属性"""
    _ensure_loaded()
    with _lock:
        for c in _cache["courses"]:
            if c["id"] == course_id:
                ch, _ = _find_chapter(c, chapter_id)
                if ch is None:
                    return None
                for k in ("title", "visible", "order"):
                    if k in updates:
                        ch[k] = updates[k]
                _save()
                return dict(ch)
        return None


def delete_chapter(course_id, chapter_id):
    """删除章节"""
    _ensure_loaded()
    with _lock:
        for c in _cache["courses"]:
            if c["id"] == course_id:
                c["chapters"] = [ch for ch in c.get("chapters", []) if ch["id"] != chapter_id]
                _save()
                return True
        return False


# ==================== Problem Assignment CRUD ====================

def get_chapter_problems(course_id, chapter_id):
    """获取章节中的所有题目"""
    course = get_course(course_id)
    if not course:
        return []
    ch, _ = _find_chapter(course, chapter_id)
    return list(ch.get("problems", [])) if ch else []


def add_problem_to_chapter(course_id, chapter_id, problem_data):
    """向章节添加题目，返回 (problem_dict, error_string)"""
    _ensure_loaded()
    with _lock:
        for c in _cache["courses"]:
            if c["id"] == course_id:
                ch, _ = _find_chapter(c, chapter_id)
                if ch is None:
                    return None, "Chapter not found"
                # 检查重复
                display_id = problem_data.get("display_id", "")
                if any(p["display_id"] == display_id for p in ch.get("problems", [])):
                    return None, "Problem already in this chapter"
                entry = {
                    "display_id": display_id,
                    "type": problem_data.get("type", "exercise"),
                    "order": problem_data.get("order", 0),
                }
                ch.setdefault("problems", []).append(entry)
                _save()
                return entry, None
        return None, "Course not found"


def remove_problem_from_chapter(course_id, chapter_id, display_id):
    """从章节移除题目"""
    _ensure_loaded()
    with _lock:
        for c in _cache["courses"]:
            if c["id"] == course_id:
                ch, _ = _find_chapter(c, chapter_id)
                if ch is None:
                    return False
                ch["problems"] = [p for p in ch.get("problems", []) if p["display_id"] != display_id]
                _save()
                return True
        return False


def update_problem_in_chapter(course_id, chapter_id, display_id, updates):
    """更新章节中题目的属性（type, order）"""
    _ensure_loaded()
    with _lock:
        for c in _cache["courses"]:
            if c["id"] == course_id:
                ch, _ = _find_chapter(c, chapter_id)
                if ch is None:
                    return None
                for p in ch.get("problems", []):
                    if p["display_id"] == display_id:
                        for k in ("type", "order"):
                            if k in updates:
                                p[k] = updates[k]
                        _save()
                        return dict(p)
        return None
