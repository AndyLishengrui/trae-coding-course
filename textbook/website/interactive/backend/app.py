"""
剑道试炼 · 互动编程平台 - 后端 API
Flask-based backend for code execution and progress tracking
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import subprocess
import tempfile
import os
import json
import time
import hashlib
from datetime import datetime, timedelta

# ============================================================
# App Configuration
# ============================================================
app = Flask(__name__, static_folder='../')
CORS(app)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jd_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# ============================================================
# Database Models
# ============================================================

class User(db.Model):
    """User model for students and teachers"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default='student')  # student, teacher, admin
    sword_energy = db.Column(db.Integer, default=100)  # Gamification currency
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    submissions = db.relationship('Submission', backref='user', lazy=True)
    progress = db.relationship('UserProgress', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'sword_energy': self.sword_energy,
            'created_at': self.created_at.isoformat()
        }

class Problem(db.Model):
    """Problem model"""
    id = db.Column(db.Integer, primary_key=True)
    jd_id = db.Column(db.String(20), unique=True, nullable=False)  # JD001, JD002, etc.
    title = db.Column(db.String(200), nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    story = db.Column(db.Text)
    input_format = db.Column(db.Text)
    output_format = db.Column(db.Text)
    sample_input = db.Column(db.Text)
    sample_output = db.Column(db.Text)
    tags = db.Column(db.JSON)
    hints = db.Column(db.JSON)
    cpp_code = db.Column(db.Text)
    python_code = db.Column(db.Text)
    difficulty = db.Column(db.Integer, default=1)  # 1-5
    acwing_id = db.Column(db.Integer)

    # Relationships
    test_cases = db.relationship('TestCase', backref='problem', lazy=True)
    submissions = db.relationship('Submission', backref='problem', lazy=True)

    def to_dict(self, include_code=False):
        data = {
            'id': self.jd_id,
            'title': self.title,
            'chapter': self.chapter,
            'story': self.story,
            'inputFormat': self.input_format,
            'outputFormat': self.output_format,
            'sampleInput': self.sample_input,
            'sampleOutput': self.sample_output,
            'tags': self.tags or [],
            'hints': self.hints or [],
            'difficulty': self.difficulty,
            'testCases': [tc.to_dict() for tc in self.test_cases]
        }
        if include_code:
            data['cppCode'] = self.cpp_code
            data['pythonCode'] = self.python_code
        return data

class TestCase(db.Model):
    """Test case model"""
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)
    input_data = db.Column(db.Text, nullable=False)
    expected_output = db.Column(db.Text, nullable=False)
    is_sample = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer, default=1)

    def to_dict(self):
        return {
            'input': self.input_data,
            'output': self.expected_output
        }

class Submission(db.Model):
    """Submission model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)
    language = db.Column(db.String(20), nullable=False)  # cpp, python
    code = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20))  # AC, WA, TLE, RE, CE
    score = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    execution_time = db.Column(db.Float)  # seconds
    memory_used = db.Column(db.Integer)  # KB
    test_results = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'problemId': self.problem.jd_id,
            'language': self.language,
            'status': self.status,
            'score': self.score,
            'totalScore': self.total_score,
            'executionTime': self.execution_time,
            'createdAt': self.created_at.isoformat()
        }

class UserProgress(db.Model):
    """User progress tracking"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)
    status = db.Column(db.String(20), default='unsolved')  # unsolved, attempted, solved
    best_score = db.Column(db.Integer, default=0)
    attempts = db.Column(db.Integer, default=0)
    first_solved_at = db.Column(db.DateTime)
    last_attempted_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('user_id', 'problem_id'),)

    def to_dict(self):
        return {
            'problemId': self.problem.jd_id,
            'status': self.status,
            'bestScore': self.best_score,
            'attempts': self.attempts,
            'firstSolvedAt': self.first_solved_at.isoformat() if self.first_solved_at else None
        }

class HintUsage(db.Model):
    """Track hint usage for gamification"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)
    hint_level = db.Column(db.Integer, nullable=False)
    used_at = db.Column(db.DateTime, default=datetime.utcnow)

# ============================================================
# Code Execution Engine
# ============================================================

class CodeExecutor:
    """Sandboxed code execution engine"""

    TIMEOUT = 5  # seconds
    MAX_MEMORY = 256 * 1024 * 1024  # 256MB

    @staticmethod
    def execute_cpp(code, stdin_data):
        """Execute C++ code in a sandboxed environment"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Write code to file
            code_file = os.path.join(tmpdir, 'solution.cpp')
            exec_file = os.path.join(tmpdir, 'solution')

            with open(code_file, 'w') as f:
                f.write(code)

            # Compile
            try:
                compile_result = subprocess.run(
                    ['g++', '-o', exec_file, code_file, '-std=c++17', '-O2'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                if compile_result.returncode != 0:
                    return {
                        'status': 'CE',
                        'stderr': compile_result.stderr,
                        'stdout': '',
                        'time': 0,
                        'memory': 0
                    }
            except subprocess.TimeoutExpired:
                return {'status': 'CE', 'stderr': 'Compilation timeout', 'stdout': '', 'time': 0, 'memory': 0}

            # Execute
            try:
                start_time = time.time()
                exec_result = subprocess.run(
                    [exec_file],
                    input=stdin_data,
                    capture_output=True,
                    text=True,
                    timeout=CodeExecutor.TIMEOUT
                )
                execution_time = time.time() - start_time

                return {
                    'status': 'OK' if exec_result.returncode == 0 else 'RE',
                    'stdout': exec_result.stdout,
                    'stderr': exec_result.stderr,
                    'time': execution_time,
                    'memory': 0  # Would need psutil for actual memory tracking
                }
            except subprocess.TimeoutExpired:
                return {'status': 'TLE', 'stdout': '', 'stderr': 'Time Limit Exceeded', 'time': CodeExecutor.TIMEOUT, 'memory': 0}

    @staticmethod
    def execute_python(code, stdin_data):
        """Execute Python code in a sandboxed environment"""
        with tempfile.TemporaryDirectory() as tmpdir:
            code_file = os.path.join(tmpdir, 'solution.py')

            with open(code_file, 'w') as f:
                f.write(code)

            try:
                start_time = time.time()
                exec_result = subprocess.run(
                    ['python3', code_file],
                    input=stdin_data,
                    capture_output=True,
                    text=True,
                    timeout=CodeExecutor.TIMEOUT
                )
                execution_time = time.time() - start_time

                return {
                    'status': 'OK' if exec_result.returncode == 0 else 'RE',
                    'stdout': exec_result.stdout,
                    'stderr': exec_result.stderr,
                    'time': execution_time,
                    'memory': 0
                }
            except subprocess.TimeoutExpired:
                return {'status': 'TLE', 'stdout': '', 'stderr': 'Time Limit Exceeded', 'time': CodeExecutor.TIMEOUT, 'memory': 0}

# ============================================================
# API Routes - Static Files
# ============================================================

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# ============================================================
# API Routes - Authentication
# ============================================================

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'student')

    if not username or not password:
        return jsonify({'error': '用户名和密码不能为空'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': '用户名已存在'}), 400

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user = User(username=username, password_hash=password_hash, role=role)
    db.session.add(user)
    db.session.commit()

    token = create_access_token(identity=user.id)
    return jsonify({'token': token, 'user': user.to_dict()})

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user = User.query.filter_by(username=username, password_hash=password_hash).first()

    if not user:
        return jsonify({'error': '用户名或密码错误'}), 401

    token = create_access_token(identity=user.id)
    return jsonify({'token': token, 'user': user.to_dict()})

@app.route('/api/auth/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user = User.query.get(get_jwt_identity())
    return jsonify(user.to_dict())

# ============================================================
# API Routes - Problems
# ============================================================

@app.route('/api/problems', methods=['GET'])
def get_problems():
    """Get all problems"""
    chapter = request.args.get('chapter')
    query = Problem.query

    if chapter:
        query = query.filter_by(chapter=int(chapter))

    problems = query.order_by(Problem.chapter, Problem.jd_id).all()
    return jsonify({p.jd_id: p.to_dict() for p in problems})

@app.route('/api/problems/<jd_id>', methods=['GET'])
def get_problem(jd_id):
    """Get a specific problem"""
    problem = Problem.query.filter_by(jd_id=jd_id).first_or_404()
    return jsonify(problem.to_dict(include_code=True))

# ============================================================
# API Routes - Code Execution
# ============================================================

@app.route('/api/run', methods=['POST'])
@jwt_required()
def run_code():
    """Run code with custom input"""
    data = request.get_json()
    code = data.get('code')
    language = data.get('language')
    stdin_data = data.get('stdin', '')

    if language == 'cpp':
        result = CodeExecutor.execute_cpp(code, stdin_data)
    elif language == 'python':
        result = CodeExecutor.execute_python(code, stdin_data)
    else:
        return jsonify({'error': '不支持的语言'}), 400

    return jsonify(result)

@app.route('/api/submit', methods=['POST'])
@jwt_required()
def submit_code():
    """Submit code for judging"""
    user_id = get_jwt_identity()
    data = request.get_json()

    jd_id = data.get('problemId')
    code = data.get('code')
    language = data.get('language')

    problem = Problem.query.filter_by(jd_id=jd_id).first_or_404()
    test_cases = TestCase.query.filter_by(problem_id=problem.id).all()

    if not test_cases:
        return jsonify({'error': '该题目暂无测试数据'}), 400

    # Run against all test cases
    total_score = sum(tc.score for tc in test_cases)
    earned_score = 0
    test_results = []
    max_time = 0
    all_passed = True

    for tc in test_cases:
        if language == 'cpp':
            result = CodeExecutor.execute_cpp(code, tc.input_data)
        else:
            result = CodeExecutor.execute_python(code, tc.input_data)

        passed = result['status'] == 'OK' and result['stdout'].strip() == tc.expected_output.strip()

        if passed:
            earned_score += tc.score
        else:
            all_passed = False

        test_results.append({
            'passed': passed,
            'input': tc.input_data,
            'expected': tc.expected_output,
            'actual': result['stdout'],
            'stderr': result['stderr'],
            'time': result['time'],
            'status': result['status']
        })

        max_time = max(max_time, result['time'])

    # Determine submission status
    if all_passed:
        status = 'AC'
    elif any(r['status'] == 'TLE' for r in test_results):
        status = 'TLE'
    elif any(r['status'] == 'RE' for r in test_results):
        status = 'RE'
    else:
        status = 'WA'

    # Save submission
    submission = Submission(
        user_id=user_id,
        problem_id=problem.id,
        language=language,
        code=code,
        status=status,
        score=earned_score,
        total_score=total_score,
        execution_time=max_time,
        test_results=test_results
    )
    db.session.add(submission)

    # Update progress
    progress = UserProgress.query.filter_by(user_id=user_id, problem_id=problem.id).first()
    if not progress:
        progress = UserProgress(user_id=user_id, problem_id=problem.id)
        db.session.add(progress)

    progress.attempts += 1
    progress.last_attempted_at = datetime.utcnow()

    if status == 'AC':
        progress.status = 'solved'
        progress.best_score = total_score
        if not progress.first_solved_at:
            progress.first_solved_at = datetime.utcnow()
            # Award sword energy
            user = User.query.get(user_id)
            user.sword_energy += 10
    elif progress.status != 'solved':
        progress.status = 'attempted'

    db.session.commit()

    return jsonify({
        'submissionId': submission.id,
        'status': status,
        'score': earned_score,
        'totalScore': total_score,
        'testResults': test_results
    })

# ============================================================
# API Routes - Progress
# ============================================================

@app.route('/api/progress', methods=['GET'])
@jwt_required()
def get_progress():
    """Get user's progress"""
    user_id = get_jwt_identity()
    progress = UserProgress.query.filter_by(user_id=user_id).all()

    # Get stats
    total = Problem.query.count()
    solved = sum(1 for p in progress if p.status == 'solved')
    attempted = sum(1 for p in progress if p.status == 'attempted')

    return jsonify({
        'problems': {p.problem.jd_id: p.to_dict() for p in progress},
        'stats': {
            'total': total,
            'solved': solved,
            'attempted': attempted,
            'unsolved': total - solved - attempted
        }
    })

@app.route('/api/submissions', methods=['GET'])
@jwt_required()
def get_submissions():
    """Get user's submissions"""
    user_id = get_jwt_identity()
    problem_id = request.args.get('problemId')

    query = Submission.query.filter_by(user_id=user_id)
    if problem_id:
        problem = Problem.query.filter_by(jd_id=problem_id).first()
        if problem:
            query = query.filter_by(problem_id=problem.id)

    submissions = query.order_by(Submission.created_at.desc()).limit(50).all()
    return jsonify([s.to_dict() for s in submissions])

# ============================================================
# API Routes - Hints
# ============================================================

@app.route('/api/hints/<jd_id>/<int:level>', methods=['POST'])
@jwt_required()
def use_hint(jd_id, level):
    """Use a hint (costs sword energy)"""
    user_id = get_jwt_identity()
    problem = Problem.query.filter_by(jd_id=jd_id).first_or_404()

    # Check if already used
    existing = HintUsage.query.filter_by(
        user_id=user_id,
        problem_id=problem.id,
        hint_level=level
    ).first()

    if existing:
        hints = problem.hints or []
        if level <= len(hints):
            return jsonify({'hint': hints[level - 1], 'cost': 0})
        return jsonify({'error': '提示不存在'}), 404

    # Deduct sword energy
    user = User.query.get(user_id)
    cost = 5
    if user.sword_energy < cost:
        return jsonify({'error': '剑气不足'}), 400

    user.sword_energy -= cost

    # Record hint usage
    hint_usage = HintUsage(user_id=user_id, problem_id=problem.id, hint_level=level)
    db.session.add(hint_usage)
    db.session.commit()

    hints = problem.hints or []
    if level <= len(hints):
        return jsonify({'hint': hints[level - 1], 'cost': cost, 'remaining_energy': user.sword_energy})

    return jsonify({'error': '提示不存在'}), 404

# ============================================================
# API Routes - Leaderboard
# ============================================================

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Get leaderboard"""
    # Get top users by solved problems
    from sqlalchemy import func

    leaderboard = db.session.query(
        User.username,
        func.count(UserProgress.id).label('solved_count'),
        User.sword_energy
    ).join(
        UserProgress, User.id == UserProgress.user_id
    ).filter(
        UserProgress.status == 'solved'
    ).group_by(
        User.id
    ).order_by(
        func.count(UserProgress.id).desc()
    ).limit(20).all()

    return jsonify([{
        'username': l.username,
        'solved': l.solved_count,
        'swordEnergy': l.sword_energy
    } for l in leaderboard])

# ============================================================
# API Routes - Teacher Dashboard
# ============================================================

@app.route('/api/teacher/students', methods=['GET'])
@jwt_required()
def get_students():
    """Get all students (teacher only)"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user.role != 'teacher' and user.role != 'admin':
        return jsonify({'error': '权限不足'}), 403

    students = User.query.filter_by(role='student').all()
    result = []

    for student in students:
        progress = UserProgress.query.filter_by(user_id=student.id).all()
        solved = sum(1 for p in progress if p.status == 'solved')
        total_submissions = Submission.query.filter_by(user_id=student.id).count()

        result.append({
            **student.to_dict(),
            'solved': solved,
            'totalSubmissions': total_submissions,
            'progress': {p.problem.jd_id: p.to_dict() for p in progress}
        })

    return jsonify(result)

@app.route('/api/teacher/submissions', methods=['GET'])
@jwt_required()
def get_all_submissions():
    """Get all submissions (teacher only)"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user.role != 'teacher' and user.role != 'admin':
        return jsonify({'error': '权限不足'}), 403

    problem_id = request.args.get('problemId')
    student_id = request.args.get('studentId')

    query = Submission.query

    if problem_id:
        problem = Problem.query.filter_by(jd_id=problem_id).first()
        if problem:
            query = query.filter_by(problem_id=problem.id)

    if student_id:
        query = query.filter_by(user_id=int(student_id))

    submissions = query.order_by(Submission.created_at.desc()).limit(100).all()

    result = []
    for s in submissions:
        data = s.to_dict()
        data['username'] = s.user.username
        data['problemTitle'] = s.problem.title
        result.append(data)

    return jsonify(result)

@app.route('/api/teacher/stats', methods=['GET'])
@jwt_required()
def get_teacher_stats():
    """Get class statistics (teacher only)"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user.role != 'teacher' and user.role != 'admin':
        return jsonify({'error': '权限不足'}), 403

    total_students = User.query.filter_by(role='student').count()
    total_problems = Problem.query.count()
    total_submissions = Submission.query.count()

    # Problem solve rates
    problem_stats = []
    problems = Problem.query.all()
    for p in problems:
        solved_count = UserProgress.query.filter_by(problem_id=p.id, status='solved').count()
        attempted_count = UserProgress.query.filter_by(problem_id=p.id).count()
        problem_stats.append({
            'id': p.jd_id,
            'title': p.title,
            'chapter': p.chapter,
            'solvedCount': solved_count,
            'attemptedCount': attempted_count,
            'solveRate': round(solved_count / total_students * 100, 1) if total_students > 0 else 0
        })

    # Chapter completion rates
    chapter_stats = {}
    for p in problems:
        if p.chapter not in chapter_stats:
            chapter_stats[p.chapter] = {'total': 0, 'solved': 0}
        chapter_stats[p.chapter]['total'] += 1
        solved = UserProgress.query.filter_by(problem_id=p.id, status='solved').count()
        chapter_stats[p.chapter]['solved'] += solved

    return jsonify({
        'totalStudents': total_students,
        'totalProblems': total_problems,
        'totalSubmissions': total_submissions,
        'problemStats': problem_stats,
        'chapterStats': chapter_stats
    })

# ============================================================
# Database Initialization
# ============================================================

def init_db():
    """Initialize database with problem data"""
    db.create_all()

    # Check if problems already loaded
    if Problem.query.count() > 0:
        return

    # Load from JSON file
    json_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '剑道试炼', 'jd_mapping.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            mapping = json.load(f)

        for jd_id, data in mapping.items():
            problem = Problem(
                jd_id=jd_id,
                title=data.get('title', ''),
                chapter=data.get('ch', 1),
                tags=data.get('tags', []),
                acwing_id=data.get('acw')
            )
            db.session.add(problem)

        db.session.commit()
    else:
        # Insert sample problems
        sample_problems = [
            Problem(
                jd_id='JD001',
                title='铁令求和',
                chapter=1,
                story='李少白第一次来到剑道宗山门前。梁嘉峰递给他两枚铁令，上面各刻着一个数。「加起来，报给我。」',
                input_format='一行，两个整数A和B，用空格隔开。',
                output_format='一个整数，即A+B的结果。',
                sample_input='3 4',
                sample_output='7',
                tags=['基础语法', '输入输出'],
                hints=['读入两个整数，输出它们的和。', '使用 cin 读入，cout 输出。Python 可以用 input().split()。', '定义两个变量，读入后直接相加输出即可。'],
                cpp_code='#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a + b << endl;\n    return 0;\n}',
                python_code='a, b = map(int, input().split())\nprint(a + b)',
                difficulty=1
            ),
            Problem(
                jd_id='JD002',
                title='铁令相乘',
                chapter=1,
                story='梁嘉峰又递来两枚铁令。这一次他竖起两根手指——乘起来。',
                input_format='一行，两个整数A和B，用空格隔开。',
                output_format='输出 PROD = 后跟A×B的结果。',
                sample_input='3 9',
                sample_output='PROD = 27',
                tags=['基础语法', '输入输出'],
                hints=['读入两个整数，输出它们的乘积。', '注意输出格式，需要先输出 "PROD = "。', '使用 printf 或 cout 格式化输出。'],
                cpp_code='#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << "PROD = " << a * b << endl;\n    return 0;\n}',
                python_code='a, b = map(int, input().split())\nprint(f"PROD = {a * b}")',
                difficulty=1
            )
        ]

        db.session.add_all(sample_problems)

        # Add test cases
        for problem in sample_problems:
            if problem.jd_id == 'JD001':
                test_cases = [
                    TestCase(problem_id=problem.id, input_data='3 4', expected_output='7', is_sample=True),
                    TestCase(problem_id=problem.id, input_data='10 20', expected_output='30'),
                    TestCase(problem_id=problem.id, input_data='-5 5', expected_output='0')
                ]
            elif problem.jd_id == 'JD002':
                test_cases = [
                    TestCase(problem_id=problem.id, input_data='3 9', expected_output='PROD = 27', is_sample=True),
                    TestCase(problem_id=problem.id, input_data='5 5', expected_output='PROD = 25')
                ]
            db.session.add_all(test_cases)

        db.session.commit()

# ============================================================
# Main Entry Point
# ============================================================

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True, port=5000)
