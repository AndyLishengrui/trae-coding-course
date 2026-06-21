/**
 * 剑道试炼 · 互动编程平台
 * Main Application Logic
 */

// ============================================================
// Configuration
// ============================================================
const CONFIG = {
    API_BASE: '/api',  // Backend API base URL
    JUDGE0_URL: 'https://judge0-ce.p.rapidapi.com',  // Judge0 API for code execution
    LANGUAGES: {
        cpp: { id: 54, name: 'C++ (GCC 9.2.0)', monacoId: 'cpp' },
        python: { id: 71, name: 'Python (3.8.1)', monacoId: 'python' }
    },
    STORAGE_KEYS: {
        USER: 'jd_user',
        PROGRESS: 'jd_progress',
        CODE: 'jd_code_',
        THEME: 'jd-theme'
    }
};

// ============================================================
// State Management
// ============================================================
const state = {
    user: null,
    currentProblem: null,
    currentLang: 'cpp',
    editor: null,
    problems: [],
    progress: {},
    submissions: []
};

// ============================================================
// Problem Data (loaded from JSON)
// ============================================================
let PROBLEMS_DATA = {};

async function loadProblems() {
    try {
        // Try to load from API first
        const response = await fetch(`${CONFIG.API_BASE}/problems`);
        if (response.ok) {
            PROBLEMS_DATA = await response.json();
        } else {
            // Fallback to embedded data
            PROBLEMS_DATA = getEmbeddedProblems();
        }
    } catch (e) {
        // Use embedded data as fallback
        PROBLEMS_DATA = getEmbeddedProblems();
    }
    state.problems = Object.entries(PROBLEMS_DATA).map(([id, data]) => ({
        id,
        ...data
    }));
    renderProblemList();
}

function getEmbeddedProblems() {
    // Embedded problem data for offline use
    return {
        'JD001': {
            title: '铁令求和',
            chapter: 1,
            story: '李少白第一次来到剑道宗山门前。梁嘉峰递给他两枚铁令，上面各刻着一个数。「加起来，报给我。」',
            inputFormat: '一行，两个整数A和B，用空格隔开。',
            outputFormat: '一个整数，即A+B的结果。',
            sampleInput: '3 4',
            sampleOutput: '7',
            tags: ['基础语法', '输入输出'],
            hints: [
                '读入两个整数，输出它们的和。',
                '使用 cin 读入，cout 输出。Python 可以用 input().split()。',
                '定义两个变量，读入后直接相加输出即可。'
            ],
            testCases: [
                { input: '3 4', output: '7' },
                { input: '10 20', output: '30' },
                { input: '-5 5', output: '0' }
            ],
            cppCode: `#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}`,
            pythonCode: `a, b = map(int, input().split())
print(a + b)`
        },
        'JD002': {
            title: '铁令相乘',
            chapter: 1,
            story: '梁嘉峰又递来两枚铁令。这一次他竖起两根手指——乘起来。',
            inputFormat: '一行，两个整数A和B，用空格隔开。',
            outputFormat: '输出 PROD = 后跟A×B的结果。',
            sampleInput: '3 9',
            sampleOutput: 'PROD = 27',
            tags: ['基础语法', '输入输出'],
            hints: [
                '读入两个整数，输出它们的乘积。',
                '注意输出格式，需要先输出 "PROD = "。',
                '使用 printf 或 cout 格式化输出。'
            ],
            testCases: [
                { input: '3 9', output: 'PROD = 27' },
                { input: '5 5', output: 'PROD = 25' }
            ],
            cppCode: `#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << "PROD = " << a * b << endl;
    return 0;
}`,
            pythonCode: `a, b = map(int, input().split())
print(f"PROD = {a * b}")`
        },
        'JD003': {
            title: '四令求差',
            chapter: 1,
            story: '四枚铁令摆在桌上，前两枚相乘，后两枚相乘，再求差。',
            inputFormat: '一行，四个整数A、B、C、D，用空格隔开。',
            outputFormat: '输出 DIFFERENCE = 后跟 A×B - C×D 的结果。',
            sampleInput: '3 5 2 4',
            sampleOutput: 'DIFFERENCE = 7',
            tags: ['基础语法', '运算'],
            hints: [
                '先分别计算 A×B 和 C×D，再求差。',
                '注意运算符优先级。',
                '直接用表达式 a*b - c*d 即可。'
            ],
            testCases: [
                { input: '3 5 2 4', output: 'DIFFERENCE = 7' },
                { input: '1 1 1 1', output: 'DIFFERENCE = 0' }
            ],
            cppCode: `#include <cstdio>

int main() {
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    printf("DIFFERENCE = %d\\n", a * b - c * d);
    return 0;
}`,
            pythonCode: `a, b, c, d = map(int, input().split())
print(f"DIFFERENCE = {a * b - c * d}")`
        }
        // More problems would be loaded from API
    };
}

// ============================================================
// Monaco Editor Initialization
// ============================================================
function initEditor() {
    require.config({ paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs' } });

    require(['vs/editor/editor.main'], function () {
        state.editor = monaco.editor.create(document.getElementById('editorContainer'), {
            value: '',
            language: 'cpp',
            theme: document.documentElement.getAttribute('data-theme') === 'dark' ? 'vs-dark' : 'vs',
            fontSize: 14,
            fontFamily: '"JetBrains Mono", "Fira Code", Consolas, monospace',
            lineNumbers: 'on',
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            automaticLayout: true,
            tabSize: 4,
            renderWhitespace: 'selection',
            bracketPairColorization: { enabled: true },
            padding: { top: 12, bottom: 12 }
        });

        // Load saved code or default
        loadProblemCode();

        // Save code on change
        state.editor.onDidChangeModelContent(() => {
            saveCurrentCode();
        });

        // Keyboard shortcuts
        state.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, () => {
            saveCurrentCode();
        });

        state.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
            submitCode();
        });
    });
}

// ============================================================
// Problem Rendering
// ============================================================
function renderProblemList() {
    const list = document.getElementById('problemList');
    const chapterFilter = document.getElementById('chapterSelect').value;

    const filtered = state.problems.filter(p => {
        if (chapterFilter === 'all') return true;
        return p.chapter === parseInt(chapterFilter);
    });

    list.innerHTML = filtered.map(p => {
        const status = getProblemStatus(p.id);
        const statusClass = status === 'solved' ? 'solved' : status === 'attempted' ? 'attempted' : '';
        const statusIcon = status === 'solved' ? '✓' : status === 'attempted' ? '◐' : '○';

        return `
            <div class="problem-item ${state.currentProblem?.id === p.id ? 'active' : ''}"
                 data-id="${p.id}" onclick="selectProblem('${p.id}')">
                <div class="problem-item-status ${statusClass}">${statusIcon}</div>
                <div class="problem-item-info">
                    <div class="problem-item-id">${p.id}</div>
                    <div class="problem-item-title">${p.title}</div>
                </div>
            </div>
        `;
    }).join('');
}

function selectProblem(problemId) {
    const problem = PROBLEMS_DATA[problemId];
    if (!problem) return;

    state.currentProblem = { id: problemId, ...problem };

    // Update problem display
    document.getElementById('problemId').textContent = problemId;
    document.getElementById('problemTitle').textContent = problem.title;
    document.getElementById('problemStory').innerHTML = `<p>${problem.story}</p>`;
    document.getElementById('inputFormat').textContent = problem.inputFormat;
    document.getElementById('outputFormat').textContent = problem.outputFormat;
    document.getElementById('sampleInput').textContent = problem.sampleInput;
    document.getElementById('sampleOutput').textContent = problem.sampleOutput;

    // Update tags
    document.getElementById('problemTags').innerHTML = problem.tags.map(t =>
        `<span class="tag">${t}</span>`
    ).join('');

    // Update status
    const status = getProblemStatus(problemId);
    const statusEl = document.getElementById('problemStatus');
    if (status === 'solved') {
        statusEl.className = 'problem-status solved';
        statusEl.innerHTML = '<span class="status-icon">✓</span><span class="status-text">已通过</span>';
    } else if (status === 'attempted') {
        statusEl.className = 'problem-status attempted';
        statusEl.innerHTML = '<span class="status-icon">◐</span><span class="status-text">已尝试</span>';
    } else {
        statusEl.className = 'problem-status unsolved';
        statusEl.innerHTML = '<span class="status-icon">○</span><span class="status-text">未完成</span>';
    }

    // Reset hint
    document.getElementById('hintContent').style.display = 'none';
    document.getElementById('hintLevel1').style.display = '';
    document.getElementById('hintLevel2').style.display = 'none';
    document.getElementById('hintLevel3').style.display = 'none';

    // Load code
    loadProblemCode();

    // Update problem list highlighting
    renderProblemList();

    // Load submissions
    loadSubmissions(problemId);
}

// ============================================================
// Code Management
// ============================================================
function loadProblemCode() {
    if (!state.currentProblem || !state.editor) return;

    const key = `${CONFIG.STORAGE_KEYS.CODE}${state.currentProblem.id}_${state.currentLang}`;
    const saved = localStorage.getItem(key);

    if (saved) {
        state.editor.setValue(saved);
    } else {
        const defaultCode = state.currentLang === 'cpp'
            ? state.currentProblem.cppCode
            : state.currentProblem.pythonCode;
        state.editor.setValue(defaultCode || getDefaultCode(state.currentLang));
    }

    // Update language
    monaco.editor.setModelLanguage(state.editor.getModel(), CONFIG.LANGUAGES[state.currentLang].monacoId);
}

function saveCurrentCode() {
    if (!state.currentProblem || !state.editor) return;

    const key = `${CONFIG.STORAGE_KEYS.CODE}${state.currentProblem.id}_${state.currentLang}`;
    localStorage.setItem(key, state.editor.getValue());
}

function getDefaultCode(lang) {
    if (lang === 'cpp') {
        return `#include <iostream>
using namespace std;

int main() {
    // 在此编写代码

    return 0;
}`;
    } else {
        return `# 在此编写代码

`;
    }
}

function resetCode() {
    if (!state.currentProblem) return;

    const defaultCode = state.currentLang === 'cpp'
        ? state.currentProblem.cppCode
        : state.currentProblem.pythonCode;

    if (confirm('确定要重置代码吗？当前代码将被覆盖。')) {
        state.editor.setValue(defaultCode || getDefaultCode(state.currentLang));
    }
}

// ============================================================
// Code Execution (Judge0 API)
// ============================================================
async function runCode() {
    if (!state.editor) return;

    const code = state.editor.getValue();
    const stdin = document.getElementById('stdinInput').value;

    showLoading(true);
    switchTab('stdout');

    try {
        // Try Judge0 API first
        const result = await executeWithJudge0(code, state.currentLang, stdin);

        document.getElementById('stdoutOutput').textContent = result.stdout || '';
        document.getElementById('stderrOutput').textContent = result.stderr || result.compile_output || '';

        if (result.status?.id === 3) {
            // Accepted (ran successfully)
            document.getElementById('stdoutOutput').textContent = result.stdout || '(无输出)';
        } else {
            switchTab('stderr');
        }
    } catch (error) {
        // Fallback: simple client-side execution for Python
        if (state.currentLang === 'python') {
            try {
                const output = executePythonSimple(code, stdin);
                document.getElementById('stdoutOutput').textContent = output;
            } catch (e) {
                document.getElementById('stderrOutput').textContent = e.message;
                switchTab('stderr');
            }
        } else {
            document.getElementById('stderrOutput').textContent = '代码执行服务暂不可用。请稍后重试。\n\n' + error.message;
            switchTab('stderr');
        }
    } finally {
        showLoading(false);
    }
}

async function executeWithJudge0(code, lang, stdin) {
    const langId = CONFIG.LANGUAGES[lang].id;

    const response = await fetch(`${CONFIG.JUDGE0_URL}/submissions?base64_encoded=false&wait=true`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com',
            'X-RapidAPI-Key': 'YOUR_API_KEY' // Replace with actual key
        },
        body: JSON.stringify({
            source_code: code,
            language_id: langId,
            stdin: stdin
        })
    });

    if (!response.ok) throw new Error('API request failed');
    return await response.json();
}

function executePythonSimple(code, stdin) {
    // Simple Python execution simulation
    // In production, this would use a sandboxed environment
    const lines = code.split('\n');
    let output = '';
    const inputs = stdin.split(/\s+/);
    let inputIndex = 0;

    // Very basic Python interpreter simulation
    // This is a placeholder - real implementation would use Pyodide or a backend
    throw new Error('Python 执行需要后端服务支持');
}

// ============================================================
// Code Submission & Testing
// ============================================================
async function submitCode() {
    if (!state.currentProblem || !state.editor) return;

    const code = state.editor.getValue();
    const testCases = state.currentProblem.testCases || [];

    if (testCases.length === 0) {
        alert('该题目暂无测试数据');
        return;
    }

    showLoading(true);
    switchTab('result');

    const resultContainer = document.getElementById('resultContent');
    resultContainer.innerHTML = '<p>正在运行测试...</p>';

    let passed = 0;
    let results = [];

    for (let i = 0; i < testCases.length; i++) {
        const tc = testCases[i];
        try {
            const result = await executeWithJudge0(code, state.currentLang, tc.input);
            const actualOutput = (result.stdout || '').trim();
            const expectedOutput = tc.output.trim();

            if (actualOutput === expectedOutput) {
                passed++;
                results.push({ index: i + 1, status: 'pass', expected: expectedOutput, actual: actualOutput });
            } else {
                results.push({ index: i + 1, status: 'fail', expected: expectedOutput, actual: actualOutput });
            }
        } catch (error) {
            results.push({ index: i + 1, status: 'error', error: error.message });
        }
    }

    // Render results
    resultContainer.innerHTML = results.map(r => `
        <div class="result-item ${r.status}">
            <span class="result-icon">${r.status === 'pass' ? '✓' : r.status === 'fail' ? '✗' : '⚠'}</span>
            <span>测试点 ${r.index}: ${r.status === 'pass' ? '通过' : r.status === 'fail' ? '答案错误' : '运行错误'}</span>
        </div>
        ${r.status === 'fail' ? `
            <div style="margin-left: 28px; font-size: 0.85em; color: var(--color-text-muted);">
                <div>期望: ${escapeHtml(r.expected)}</div>
                <div>实际: ${escapeHtml(r.actual)}</div>
            </div>
        ` : ''}
    `).join('');

    // Update progress
    const allPassed = passed === testCases.length;
    saveSubmission(state.currentProblem.id, code, allPassed, passed, testCases.length);

    if (allPassed) {
        updateProgress(state.currentProblem.id, 'solved');
        resultContainer.innerHTML += `
            <div class="result-item pass" style="margin-top: 16px; font-weight: bold;">
                <span class="result-icon">🎉</span>
                <span>恭喜！所有测试点通过！</span>
            </div>
        `;
    } else {
        updateProgress(state.currentProblem.id, 'attempted');
        resultContainer.innerHTML += `
            <div class="result-item fail" style="margin-top: 16px; font-weight: bold;">
                <span class="result-icon">💪</span>
                <span>通过 ${passed}/${testCases.length} 个测试点，继续努力！</span>
            </div>
        `;
    }

    showLoading(false);
    renderProblemList();
    updateProgressDisplay();
}

// ============================================================
// Hint System
// ============================================================
function toggleHint() {
    const content = document.getElementById('hintContent');
    if (content.style.display === 'none') {
        content.style.display = 'block';
        showHintLevel(1);
    } else {
        content.style.display = 'none';
    }
}

function showHintLevel(level) {
    if (!state.currentProblem) return;

    const hints = state.currentProblem.hints || [];
    if (level > hints.length) return;

    // Show hint
    document.getElementById(`hintLevel${level}`).style.display = '';

    // Update button
    const nextBtn = document.getElementById('hintNext');
    if (level < hints.length) {
        nextBtn.style.display = '';
        nextBtn.onclick = () => showHintLevel(level + 1);
    } else {
        nextBtn.style.display = 'none';
    }

    // Deduct points (gamification)
    deductPoints(5);
}

// ============================================================
// Code Comparison
// ============================================================
function showComparison() {
    if (!state.currentProblem || !state.editor) return;

    const section = document.getElementById('comparisonSection');
    section.style.display = 'block';

    const myCode = state.editor.getValue();
    const refCode = state.currentLang === 'cpp'
        ? state.currentProblem.cppCode
        : state.currentProblem.pythonCode;

    document.getElementById('myCodePreview').textContent = myCode;
    document.getElementById('refCodePreview').textContent = refCode;

    // Simple diff stats
    const myLines = myCode.split('\n').length;
    const refLines = refCode.split('\n').length;
    document.getElementById('diffStats').textContent =
        `我的代码: ${myLines} 行 | 参考代码: ${refLines} 行`;
}

// ============================================================
// Progress Management
// ============================================================
function loadProgress() {
    const saved = localStorage.getItem(CONFIG.STORAGE_KEYS.PROGRESS);
    state.progress = saved ? JSON.parse(saved) : {};
    updateProgressDisplay();
}

function saveProgress() {
    localStorage.setItem(CONFIG.STORAGE_KEYS.PROGRESS, JSON.stringify(state.progress));
}

function updateProgress(problemId, status) {
    const current = state.progress[problemId];
    if (status === 'solved' || (status === 'attempted' && current !== 'solved')) {
        state.progress[problemId] = status;
    }
    saveProgress();
}

function getProblemStatus(problemId) {
    return state.progress[problemId] || 'unsolved';
}

function updateProgressDisplay() {
    const total = state.problems.length || 172;
    const solved = Object.values(state.progress).filter(s => s === 'solved').length;
    const percentage = Math.round((solved / total) * 100);

    document.getElementById('solvedCount').textContent = solved;
    document.getElementById('totalCount').textContent = total;
    document.getElementById('progressText').textContent = `${percentage}%`;

    // Update progress ring
    const arc = document.getElementById('progressArc');
    if (arc) {
        arc.setAttribute('stroke-dasharray', `${percentage}, 100`);
    }
}

function deductPoints(points) {
    // Gamification: deduct hint points
    let swordEnergy = parseInt(localStorage.getItem('jd_sword_energy') || '100');
    swordEnergy = Math.max(0, swordEnergy - points);
    localStorage.setItem('jd_sword_energy', swordEnergy.toString());
}

// ============================================================
// Submission Management
// ============================================================
function saveSubmission(problemId, code, passed, score, total) {
    const submission = {
        id: Date.now(),
        problemId,
        code,
        language: state.currentLang,
        passed,
        score,
        total,
        timestamp: new Date().toISOString()
    };

    const submissions = JSON.parse(localStorage.getItem('jd_submissions') || '[]');
    submissions.unshift(submission);
    if (submissions.length > 100) submissions.pop(); // Keep last 100
    localStorage.setItem('jd_submissions', JSON.stringify(submissions));

    loadSubmissions(problemId);
}

function loadSubmissions(problemId) {
    const submissions = JSON.parse(localStorage.getItem('jd_submissions') || '[]');
    const filtered = submissions.filter(s => s.problemId === problemId).slice(0, 10);

    const list = document.getElementById('submissionList');
    list.innerHTML = filtered.map(s => `
        <div class="submission-item" onclick="loadSubmission(${s.id})">
            <div class="submission-status ${s.passed ? 'ac' : 'wa'}"></div>
            <span>${s.passed ? '通过' : '未通过'}</span>
            <span class="submission-time">${formatTime(s.timestamp)}</span>
        </div>
    `).join('');

    if (filtered.length === 0) {
        list.innerHTML = '<div style="color: var(--color-text-muted); font-size: 0.85em; text-align: center;">暂无提交记录</div>';
    }
}

function loadSubmission(submissionId) {
    const submissions = JSON.parse(localStorage.getItem('jd_submissions') || '[]');
    const submission = submissions.find(s => s.id === submissionId);
    if (submission && state.editor) {
        state.currentLang = submission.language;
        state.editor.setValue(submission.code);
        updateLanguageButtons();
    }
}

// ============================================================
// User Management
// ============================================================
function loadUser() {
    const saved = localStorage.getItem(CONFIG.STORAGE_KEYS.USER);
    if (saved) {
        state.user = JSON.parse(saved);
        updateUserDisplay();
    }
}

function login(username, password) {
    // Simple client-side auth (would be replaced with real auth)
    const users = JSON.parse(localStorage.getItem('jd_users') || '{}');
    if (users[username] && users[username].password === password) {
        state.user = { username, role: users[username].role };
        localStorage.setItem(CONFIG.STORAGE_KEYS.USER, JSON.stringify(state.user));
        updateUserDisplay();
        closeModal('loginModal');
        return true;
    }
    return false;
}

function register(username, password, role) {
    const users = JSON.parse(localStorage.getItem('jd_users') || '{}');
    if (users[username]) {
        return false; // User exists
    }
    users[username] = { password, role };
    localStorage.setItem('jd_users', JSON.stringify(users));
    state.user = { username, role };
    localStorage.setItem(CONFIG.STORAGE_KEYS.USER, JSON.stringify(state.user));
    updateUserDisplay();
    closeModal('loginModal');
    return true;
}

function logout() {
    state.user = null;
    localStorage.removeItem(CONFIG.STORAGE_KEYS.USER);
    updateUserDisplay();
}

function updateUserDisplay() {
    const userName = document.getElementById('userName');
    const userAvatar = document.querySelector('.user-avatar');

    if (state.user) {
        userName.textContent = state.user.username;
        userAvatar.textContent = state.user.username[0];
    } else {
        userName.textContent = '未登录';
        userAvatar.textContent = '剑';
    }
}

// ============================================================
// UI Helpers
// ============================================================
function showLoading(show) {
    document.getElementById('loadingOverlay').classList.toggle('show', show);
}

function switchTab(tabName) {
    document.querySelectorAll('.io-tab').forEach(tab => {
        tab.classList.toggle('active', tab.dataset.tab === tabName);
    });
    document.querySelectorAll('.io-pane').forEach(pane => {
        pane.classList.toggle('active', pane.id === `${tabName}Pane`);
    });
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('show');
}

function openModal(modalId) {
    document.getElementById(modalId).classList.add('show');
}

function updateLanguageButtons() {
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === state.currentLang);
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatTime(isoString) {
    const date = new Date(isoString);
    const now = new Date();
    const diff = now - date;

    if (diff < 60000) return '刚刚';
    if (diff < 3600000) return `${Math.floor(diff / 60000)}分钟前`;
    if (diff < 86400000) return `${Math.floor(diff / 3600000)}小时前`;
    return `${Math.floor(diff / 86400000)}天前`;
}

// ============================================================
// Dark Mode
// ============================================================
function initDarkMode() {
    const toggle = document.querySelector('.dark-toggle');
    const saved = localStorage.getItem(CONFIG.STORAGE_KEYS.THEME);

    if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.setAttribute('data-theme', 'dark');
        toggle.textContent = '☀';
    }

    toggle.addEventListener('click', () => {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {
            document.documentElement.removeAttribute('data-theme');
            toggle.textContent = '☾';
            localStorage.setItem(CONFIG.STORAGE_KEYS.THEME, 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            toggle.textContent = '☀';
            localStorage.setItem(CONFIG.STORAGE_KEYS.THEME, 'dark');
        }

        // Update Monaco theme
        if (state.editor) {
            monaco.editor.setTheme(isDark ? 'vs' : 'vs-dark');
        }
    });
}

// ============================================================
// Event Listeners
// ============================================================
function initEventListeners() {
    // Language switcher
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            state.currentLang = btn.dataset.lang;
            updateLanguageButtons();
            loadProblemCode();
        });
    });

    // Editor actions
    document.getElementById('runBtn').addEventListener('click', runCode);
    document.getElementById('submitBtn').addEventListener('click', submitCode);
    document.getElementById('resetBtn').addEventListener('click', resetCode);
    document.getElementById('formatBtn').addEventListener('click', () => {
        if (state.editor) {
            state.editor.getAction('editor.action.formatDocument')?.run();
        }
    });

    // Hint
    document.getElementById('hintToggle').addEventListener('click', toggleHint);

    // I/O tabs
    document.querySelectorAll('.io-tab').forEach(tab => {
        tab.addEventListener('click', () => switchTab(tab.dataset.tab));
    });

    // Chapter filter
    document.getElementById('chapterSelect').addEventListener('change', renderProblemList);

    // Copy sample buttons
    document.querySelectorAll('.copy-sample').forEach(btn => {
        btn.addEventListener('click', () => {
            const target = document.getElementById(btn.dataset.target);
            navigator.clipboard.writeText(target.textContent).then(() => {
                btn.textContent = '已复制';
                setTimeout(() => btn.textContent = '复制', 2000);
            });
        });
    });

    // User menu
    document.getElementById('userBtn').addEventListener('click', () => {
        document.getElementById('userDropdown').classList.toggle('show');
    });

    document.getElementById('logoutBtn').addEventListener('click', (e) => {
        e.preventDefault();
        logout();
    });

    // Login modal
    document.querySelectorAll('.login-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.login-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            document.getElementById('loginForm').style.display = tab.dataset.tab === 'login' ? '' : 'none';
            document.getElementById('registerForm').style.display = tab.dataset.tab === 'register' ? '' : 'none';
        });
    });

    document.getElementById('loginForm').addEventListener('submit', (e) => {
        e.preventDefault();
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;
        if (!login(username, password)) {
            alert('用户名或密码错误');
        }
    });

    document.getElementById('registerForm').addEventListener('submit', (e) => {
        e.preventDefault();
        const username = document.getElementById('regUsername').value;
        const password = document.getElementById('regPassword').value;
        const confirm = document.getElementById('regPasswordConfirm').value;
        const role = document.getElementById('regRole').value;

        if (password !== confirm) {
            alert('两次输入的密码不一致');
            return;
        }
        if (!register(username, password, role)) {
            alert('用户名已存在');
        }
    });

    document.getElementById('closeLogin').addEventListener('click', () => {
        closeModal('loginModal');
    });

    // Mobile menu
    document.querySelector('.menu-toggle').addEventListener('click', () => {
        document.querySelector('.nav-links').classList.toggle('open');
    });

    // Close dropdowns on outside click
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.user-menu')) {
            document.getElementById('userDropdown').classList.remove('show');
        }
    });
}

// ============================================================
// Initialization
// ============================================================
async function init() {
    initDarkMode();
    initEventListeners();
    loadUser();
    loadProgress();
    await loadProblems();
    initEditor();

    // Select first problem by default
    if (state.problems.length > 0) {
        selectProblem(state.problems[0].id);
    }
}

// Start the application
document.addEventListener('DOMContentLoaded', init);
