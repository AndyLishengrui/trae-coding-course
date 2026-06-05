"""
教材模块 API Views — 公开API
- Public APIs: /api/courses, /api/course/detail
- Admin APIs: 已迁移至 problem/views/admin.py（基于Django ORM）
- 教材→章节→题目三级结构，使用 Course/Chapter/ChapterProblem 模型
"""
from django.db.models import Prefetch
from utils.api import APIView
from problem.models import Problem, Course, Chapter, ChapterProblem


class CourseListAPI(APIView):
    """公开API: 列出所有可见课程（含章节数、题目数统计）"""

    def get(self, request):
        courses = Course.objects.filter(visible=True).order_by("order", "id")
        result = []
        for c in courses:
            # 只统计可见章节及其题目数
            chapters = c.chapters.filter(visible=True)
            chapter_count = chapters.count()
            problem_count = ChapterProblem.objects.filter(
                chapter__course=c, chapter__visible=True
            ).count()
            result.append({
                "id": c.id,
                "title": c.title,
                "description": c.description or "",
                "order": c.order,
                "chapter_count": chapter_count,
                "problem_count": problem_count,
            })
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

        try:
            course = Course.objects.prefetch_related(
                Prefetch("chapters", queryset=Chapter.objects.filter(visible=True).order_by("order", "id")),
            ).get(id=course_id, visible=True)
        except Course.DoesNotExist:
            return self.error("Course not found")

        # 收集可见章节的所有题目关联
        chapters_data = []
        all_display_ids = []
        chapter_problems_map = {}  # chapter_id -> list of ChapterProblem

        for ch in course.chapters.all():
            cp_list = list(ChapterProblem.objects.filter(chapter=ch).order_by("order", "id"))
            chapter_problems_map[ch.id] = cp_list
            for cp in cp_list:
                all_display_ids.append(cp.display_id)

            chapters_data.append({
                "id": ch.id,
                "title": ch.title,
                "order": ch.order,
                "chapter_problems": cp_list,
            })

        # 批量从数据库获取题目信息
        problems_map = {}
        if all_display_ids:
            db_problems = Problem.objects.filter(
                _id__in=all_display_ids, visible=True
            ).only("_id", "id", "title", "submission_number", "accepted_number", "difficulty")
            problems_map = {p._id: p for p in db_problems}

        # 获取登录用户的AC状态：直接从Submission表查询
        ac_problem_ids = set()
        if request.user.is_authenticated:
            from submission.models import Submission
            db_ids = [p.id for p in problems_map.values()]
            if db_ids:
                ac_subs = Submission.objects.filter(
                    user_id=request.user.id,
                    problem_id__in=db_ids,
                    result=0  # ACCEPTED
                ).values_list("problem_id", flat=True).distinct()
                ac_problem_ids = set(ac_subs)

        # 构建响应
        chapters_result = []
        for ch_data in chapters_data:
            examples = []
            exercises = []
            for cp in ch_data["chapter_problems"]:
                db_problem = problems_map.get(cp.display_id)
                if not db_problem:
                    continue

                my_status = 0 if db_problem.id in ac_problem_ids else None

                entry = {
                    "_id": db_problem._id,
                    "id": db_problem.id,
                    "title": db_problem.title,
                    "submission_number": db_problem.submission_number,
                    "accepted_number": db_problem.accepted_number,
                    "difficulty": db_problem.difficulty,
                    "type": cp.type,
                    "order": cp.order,
                    "my_status": my_status,
                }
                if cp.type == "example":
                    examples.append(entry)
                else:
                    exercises.append(entry)

            chapters_result.append({
                "id": ch_data["id"],
                "title": ch_data["title"],
                "order": ch_data["order"],
                "examples": examples,
                "exercises": exercises,
            })

        return self.success({
            "id": course.id,
            "title": course.title,
            "description": course.description or "",
            "contest_id": course.contest_id,
            "chapters": chapters_result,
        })
