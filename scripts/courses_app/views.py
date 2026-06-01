"""
课程模块 API Views
- Admin APIs: /api/admin/groups/courses, /chapters, /problems
- Public APIs: /api/courses, /api/course/detail
- 每个课程自动创建一个隐藏的OI比赛，复用contest基础设施来支撑刷题、提交、AC跟踪
"""
import datetime
from django.utils import timezone
from utils.api import APIView
from problem.models import Problem
from contest.models import Contest
from . import config_manager as cm


def _get_or_create_contest(course_id, title, user):
    """获取或创建课程关联的比赛。如果已有contest_id则复用，否则创建新的隐藏OI比赛。"""
    course = cm.get_course(course_id)
    if not course:
        return None

    existing_id = course.get("contest_id")
    if existing_id:
        try:
            return Contest.objects.get(id=existing_id)
        except Contest.DoesNotExist:
            pass

    # 创建新的隐藏OI比赛
    contest = Contest.objects.create(
        title=f"[课程] {title}",
        description=f"课程「{title}」配套练习",
        start_time=timezone.now(),
        end_time=timezone.now() + datetime.timedelta(days=365 * 10),
        rule_type="OI",
        visible=True,  # 必须为True才能通过check_contest_permission
        password=None,
        created_by=user,
        real_time_rank=False,
    )
    # 记录contest_id到课程配置
    cm.update_course(course_id, {"contest_id": contest.id})
    return contest


def _sync_problem_to_contest(display_id, contest):
    """将题目关联到比赛"""
    try:
        prob = Problem.objects.get(_id=display_id, visible=True)
        prob.contest_id = contest.id
        prob.save(update_fields=["contest_id"])
        return True
    except Problem.DoesNotExist:
        return False


def _unsync_problem_from_contest(display_id, contest):
    """将题目从比赛解绑（如果它当前属于该比赛）"""
    try:
        prob = Problem.objects.get(_id=display_id, contest_id=contest.id)
        prob.contest_id = None
        prob.save(update_fields=["contest_id"])
        return True
    except Problem.DoesNotExist:
        return False


def _is_problem_in_any_chapter(course_id, display_id):
    """检查题目是否还在该课程的任意章节中"""
    chapters = cm.get_chapters(course_id)
    for ch in chapters:
        for p in ch.get("problems", []):
            if p["display_id"] == display_id:
                return True
    return False


def _sync_all_problems_to_contest(course_id, contest):
    """将课程中所有章节的题目同步到比赛"""
    display_ids = set()
    chapters = cm.get_chapters(course_id)
    for ch in chapters:
        for p in ch.get("problems", []):
            display_ids.add(p["display_id"])
    for did in display_ids:
        _sync_problem_to_contest(did, contest)


# ==================== Admin APIs ====================

class CourseAdminAPI(APIView):
    """课程管理 CRUD: GET list/single, POST create, PUT update, DELETE"""

    def get(self, request):
        course_id = request.GET.get("id")
        if course_id:
            try:
                course_id = int(course_id)
            except (ValueError, TypeError):
                return self.error("Invalid course id")
            course = cm.get_course(course_id)
            if not course:
                return self.error("Course not found")
            return self.success(course)

        courses = cm.get_all_courses()
        courses.sort(key=lambda c: (c.get("order", 0), c.get("id", 0)))
        return self.success(courses)

    def post(self, request):
        data = request.data
        title = (data.get("title") or "").strip()
        if not title:
            return self.error("title is required")
        course = cm.create_course({
            "title": title,
            "description": data.get("description", ""),
            "visible": data.get("visible", True),
            "order": data.get("order", 0),
        })
        # 自动创建对应的隐藏OI比赛
        contest = _get_or_create_contest(course["id"], title, request.user)
        course["contest_id"] = contest.id if contest else None
        return self.success(course)

    def put(self, request):
        data = request.data
        course_id = data.get("id")
        if not course_id:
            return self.error("id required")
        course = cm.update_course(course_id, data)
        if not course:
            return self.error("Course not found")
        return self.success(course)

    def delete(self, request):
        course_id = request.GET.get("id")
        if not course_id:
            return self.error("id required")
        try:
            course_id = int(course_id)
        except (ValueError, TypeError):
            return self.error("Invalid course id")

        # 删除关联的比赛
        course = cm.get_course(course_id)
        if course and course.get("contest_id"):
            try:
                contest = Contest.objects.get(id=course["contest_id"])
                # 解绑题目
                Problem.objects.filter(contest_id=contest.id).update(contest_id=None)
                contest.delete()
            except Contest.DoesNotExist:
                pass

        cm.delete_course(course_id)
        return self.success()


class ChapterAdminAPI(APIView):
    """章节管理 CRUD: GET list, POST create, PUT update, DELETE"""

    def get(self, request):
        course_id = request.GET.get("course_id")
        if not course_id:
            return self.error("course_id required")
        try:
            course_id = int(course_id)
        except (ValueError, TypeError):
            return self.error("Invalid course_id")
        chapters = cm.get_chapters(course_id)
        chapters.sort(key=lambda ch: (ch.get("order", 0), ch.get("id", 0)))
        return self.success(chapters)

    def post(self, request):
        data = request.data
        course_id = data.get("course_id")
        title = (data.get("title") or "").strip()
        if not course_id or not title:
            return self.error("course_id and title required")
        chapter = cm.create_chapter(course_id, {
            "title": title,
            "visible": data.get("visible", True),
            "order": data.get("order", 0),
        })
        if not chapter:
            return self.error("Course not found")
        return self.success(chapter)

    def put(self, request):
        data = request.data
        course_id = data.get("course_id")
        chapter_id = data.get("id")
        if not course_id or not chapter_id:
            return self.error("course_id and id required")
        chapter = cm.update_chapter(course_id, chapter_id, data)
        if not chapter:
            return self.error("Chapter not found")
        return self.success(chapter)

    def delete(self, request):
        course_id = request.GET.get("course_id")
        chapter_id = request.GET.get("id")
        if not course_id or not chapter_id:
            return self.error("course_id and id required")
        try:
            course_id = int(course_id)
            chapter_id = int(chapter_id)
        except (ValueError, TypeError):
            return self.error("Invalid id")
        ok = cm.delete_chapter(course_id, chapter_id)
        if not ok:
            return self.error("Chapter not found")
        return self.success()


class ProblemAssignmentAdminAPI(APIView):
    """章节题目关联管理: GET list, POST add, PUT update, DELETE remove"""

    def get(self, request):
        course_id = request.GET.get("course_id")
        chapter_id = request.GET.get("chapter_id")
        if not course_id or not chapter_id:
            return self.error("course_id and chapter_id required")
        try:
            course_id = int(course_id)
            chapter_id = int(chapter_id)
        except (ValueError, TypeError):
            return self.error("Invalid id")
        problems = cm.get_chapter_problems(course_id, chapter_id)
        return self.success(problems)

    def post(self, request):
        data = request.data
        course_id = data.get("course_id")
        chapter_id = data.get("chapter_id")
        display_id = (data.get("display_id") or "").strip()
        if not all([course_id, chapter_id, display_id]):
            return self.error("course_id, chapter_id, display_id required")

        # 验证题目在数据库中存在
        prob = Problem.objects.filter(_id=display_id, visible=True).first()
        if not prob:
            return self.error(f"Problem {display_id} not found in database")

        result, err = cm.add_problem_to_chapter(course_id, chapter_id, {
            "display_id": display_id,
            "type": data.get("type", "example"),
            "order": data.get("order", 0),
        })
        if err:
            return self.error(err)

        # 同步到课程关联的比赛
        course = cm.get_course(course_id)
        if course and course.get("contest_id"):
            try:
                contest = Contest.objects.get(id=course["contest_id"])
                _sync_problem_to_contest(display_id, contest)
            except Contest.DoesNotExist:
                pass

        return self.success(result)

    def put(self, request):
        data = request.data
        course_id = data.get("course_id")
        chapter_id = data.get("chapter_id")
        display_id = (data.get("display_id") or "").strip()
        if not all([course_id, chapter_id, display_id]):
            return self.error("course_id, chapter_id, display_id required")
        result = cm.update_problem_in_chapter(course_id, chapter_id, display_id, data)
        if not result:
            return self.error("Problem not found in chapter")
        return self.success(result)

    def delete(self, request):
        course_id = request.GET.get("course_id")
        chapter_id = request.GET.get("chapter_id")
        display_id = request.GET.get("display_id")
        if not all([course_id, chapter_id, display_id]):
            return self.error("course_id, chapter_id, display_id required")
        try:
            course_id = int(course_id)
            chapter_id = int(chapter_id)
        except (ValueError, TypeError):
            return self.error("Invalid id")
        ok = cm.remove_problem_from_chapter(course_id, chapter_id, display_id)
        if not ok:
            return self.error("Problem not found in chapter")

        # 如果题目已不在该课程任何章节中，从比赛解绑
        if not _is_problem_in_any_chapter(course_id, display_id):
            course = cm.get_course(course_id)
            if course and course.get("contest_id"):
                try:
                    contest = Contest.objects.get(id=course["contest_id"])
                    _unsync_problem_from_contest(display_id, contest)
                except Contest.DoesNotExist:
                    pass

        return self.success()


class MoveProblemAdminAPI(APIView):
    """移动题目到另一章节"""

    def post(self, request):
        data = request.data
        course_id = data.get("course_id")
        from_chapter_id = data.get("from_chapter_id")
        to_chapter_id = data.get("to_chapter_id")
        display_id = (data.get("display_id") or "").strip()

        if not all([course_id, from_chapter_id, to_chapter_id, display_id]):
            return self.error("course_id, from_chapter_id, to_chapter_id, display_id required")

        if from_chapter_id == to_chapter_id:
            return self.error("Source and target chapter are the same")

        problems = cm.get_chapter_problems(course_id, from_chapter_id)
        problem_data = None
        for p in problems:
            if p["display_id"] == display_id:
                problem_data = dict(p)
                break
        if not problem_data:
            return self.error("Problem not found in source chapter")

        cm.remove_problem_from_chapter(course_id, from_chapter_id, display_id)

        problem_data["type"] = data.get("type", problem_data.get("type", "exercise"))
        problem_data["order"] = data.get("order", problem_data.get("order", 0))

        result, err = cm.add_problem_to_chapter(course_id, to_chapter_id, problem_data)
        if err:
            cm.add_problem_to_chapter(course_id, from_chapter_id, {
                "display_id": display_id,
                "type": problem_data.get("type", "exercise"),
                "order": problem_data.get("order", 0),
            })
            return self.error(err)
        return self.success(result)


class SyncCourseContestAPI(APIView):
    """同步课程所有题目到关联比赛"""

    def post(self, request):
        course_id = request.data.get("course_id")
        if not course_id:
            return self.error("course_id required")
        course = cm.get_course(course_id)
        if not course:
            return self.error("Course not found")
        contest = _get_or_create_contest(course_id, course["title"], request.user)
        if not contest:
            return self.error("Failed to create/find contest")
        _sync_all_problems_to_contest(course_id, contest)
        return self.success({
            "contest_id": contest.id,
            "message": "All problems synced to contest"
        })


# ==================== Public APIs ====================

class CourseListAPI(APIView):
    """公开API: 列出所有可见课程（含章节数、题目数统计）"""

    def get(self, request):
        courses = cm.get_all_courses()
        result = []
        for c in courses:
            if not c.get("visible", True):
                continue
            chapter_count = len(c.get("chapters", []))
            problem_count = sum(
                len(ch.get("problems", [])) for ch in c.get("chapters", [])
            )
            result.append({
                "id": c["id"],
                "title": c["title"],
                "description": c.get("description", ""),
                "order": c.get("order", 0),
                "chapter_count": chapter_count,
                "problem_count": problem_count,
            })
        result.sort(key=lambda x: x["order"])
        return self.success(result)


class CourseDetailAPI(APIView):
    """公开API: 获取课程详情，包含章节、题目（从DB补充题目信息及AC状态）"""

    def get(self, request):
        course_id = request.GET.get("id")
        if not course_id:
            return self.error("course id required")
        try:
            course_id = int(course_id)
        except (ValueError, TypeError):
            return self.error("Invalid course id")

        course = cm.get_course(course_id)
        if not course or not course.get("visible", True):
            return self.error("Course not found")

        # 收集所有 display_id
        all_display_ids = []
        for ch in course.get("chapters", []):
            for p in ch.get("problems", []):
                all_display_ids.append(p["display_id"])

        # 批量从数据库获取题目信息
        problems_map = {}
        if all_display_ids:
            db_problems = Problem.objects.filter(
                _id__in=all_display_ids, visible=True
            ).only("_id", "id", "title", "submission_number", "accepted_number", "difficulty")
            problems_map = {p._id: p for p in db_problems}

        # 获取登录用户的OI AC状态
        status_map = {}
        if request.user.is_authenticated:
            try:
                profile = request.user.userprofile
                oi_status = profile.oi_problems_status or {}
                status_map = oi_status.get("problems", {})
            except Exception:
                pass

        # 构建响应
        chapters_result = []
        for ch in course.get("chapters", []):
            if not ch.get("visible", True):
                continue
            chapter_data = {
                "id": ch["id"],
                "title": ch["title"],
                "order": ch.get("order", 0),
                "examples": [],
                "exercises": [],
            }
            sorted_problems = sorted(
                ch.get("problems", []), key=lambda x: x.get("order", 0)
            )
            for p in sorted_problems:
                db_problem = problems_map.get(p["display_id"])
                if not db_problem:
                    continue

                my_status = None
                if status_map:
                    problem_status = status_map.get(str(db_problem.id))
                    if problem_status and isinstance(problem_status, dict):
                        my_status = problem_status.get("status")

                entry = {
                    "_id": db_problem._id,
                    "id": db_problem.id,
                    "title": db_problem.title,
                    "submission_number": db_problem.submission_number,
                    "accepted_number": db_problem.accepted_number,
                    "difficulty": db_problem.difficulty,
                    "type": p.get("type", "exercise"),
                    "order": p.get("order", 0),
                    "my_status": my_status,
                }
                if p.get("type") == "example":
                    chapter_data["examples"].append(entry)
                else:
                    chapter_data["exercises"].append(entry)

            chapters_result.append(chapter_data)

        chapters_result.sort(key=lambda x: x["order"])
        return self.success({
            "id": course["id"],
            "title": course["title"],
            "description": course.get("description", ""),
            "contest_id": course.get("contest_id"),  # 返回比赛ID供前端导航
            "chapters": chapters_result,
        })
