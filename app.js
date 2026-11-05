let essayNav;
let mainTitle;
let welcomeScreen;
let essayContent;
let themeToggle;
let isDarkMode = false;

// Recitation DOM Elements
let recitationInput;
let btnPrevQuestion;
let btnShowHint;
let btnCheckAnswer;
let btnNextQuestion;
let currentQuestionNum;
let totalQuestionsNum;
let progressBarFill;
let questionCueText;
let recitationFeedback;
let feedbackStatus;
let userDiffResult;
let correctTextResult;

// Evaluation DOM Elements
let recitationQuizBox;
let recitationResultBox;
let scorePercentageVal;
let resultStatusVal;
let resultMessageVal;
let btnRestartRecitation;
let evaluationIcon;

// Recitation State
let activeEssayTypeId = 'adv-disadv';
let currentQuestionIndex = 0;
let activeQuestions = [];
let questionScores = [];

// Word-by-word diff algorithm using LCS
function diffWords(userText, targetText) {
    const preProcess = (t) => t
        .replace(/…/g, '...')
        .replace(/\.\s*\.\s*\./g, '...')
        .replace(/[’‘]/g, "'")
        .replace(/[“”]/g, '"')
        .replace(/\s*[-\u2010\u2011\u2013\u2014\u2212]+\s*/g, ' - ');
        
    const clean = (w) => w.toLowerCase().trim();
    
    const uWords = preProcess(userText).trim().split(/\s+/).filter(w => w !== "");
    const tWords = preProcess(targetText).trim().split(/\s+/).filter(w => w !== "");
    
    const n = uWords.length;
    const m = tWords.length;
    const dp = Array(n + 1).fill(null).map(() => Array(m + 1).fill(0));
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            if (clean(uWords[i - 1]) === clean(tWords[j - 1])) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    let i = n, j = m;
    const diff = [];
    
    while (i > 0 || j > 0) {
        if (i > 0 && j > 0 && clean(uWords[i - 1]) === clean(tWords[j - 1])) {
            diff.unshift({ word: uWords[i - 1], type: 'match' });
            i--;
            j--;
        } else if (j > 0 && (i === 0 || dp[i][j - 1] >= dp[i - 1][j])) {
            diff.unshift({ word: tWords[j - 1], type: 'missing' });
            j--;
        } else {
            diff.unshift({ word: uWords[i - 1], type: 'extra' });
            i--;
        }
    }
    
    let matchCount = diff.filter(d => d.type === 'match').length;
    let maxWords = Math.max(tWords.length, uWords.length);
    let accuracy = maxWords > 0 ? Math.round((matchCount / maxWords) * 100) : 0;
    
    return {
        diff,
        accuracy,
        isPerfect: matchCount === tWords.length && uWords.length === tWords.length
    };
}

// Progress Tracking Helpers
function getCompletedEssays() {
    try {
        const completed = localStorage.getItem('vstep_b2_completed_essays');
        return completed ? JSON.parse(completed) : [];
    } catch (e) {
        return [];
    }
}

function markEssayCompleted(id) {
    if (!id) return;
    let completed = getCompletedEssays();
    if (!completed.includes(id)) {
        completed.push(id);
        try {
            localStorage.setItem('vstep_b2_completed_essays', JSON.stringify(completed));
        } catch (e) {
            console.error('Failed to write to localStorage:', e);
        }
    }
    updateGlobalProgress();
    renderNav();
}

function updateGlobalProgress() {
    const completed = getCompletedEssays();
    const total = 4;
    const count = completed.length;
    const percent = Math.round((count / total) * 100);

    // Update Sidebar progress
    const sidebarText = document.getElementById('sidebarProgressText');
    const sidebarFill = document.getElementById('sidebarProgressFill');
    if (sidebarText) sidebarText.textContent = `${count}/${total} ĐẠT`;
    if (sidebarFill) sidebarFill.style.width = `${percent}%`;

    // Update Dashboard progress
    const dashPercent = document.getElementById('dashboardProgressPercent');
    const dashFill = document.getElementById('dashboardProgressFill');
    const dashStatus = document.getElementById('dashboardProgressStatus');

    if (dashPercent) dashPercent.textContent = `${percent}%`;
    if (dashFill) dashFill.style.width = `${percent}%`;

    if (dashStatus) {
        if (count === 0) {
            dashStatus.textContent = "Chưa hoàn thành dạng bài nào. Hãy bắt đầu học tập!";
        } else if (count === total) {
            dashStatus.textContent = "🎉 TUYỆT VỜI! Bạn đã xuất sắc chinh phục tất cả 4 dạng luận VSTEP Writing Task 02!";
        } else {
            dashStatus.textContent = `Đã chinh phục ${count}/${total} dạng bài. Hãy tiếp tục nhiệm vụ tiếp theo!`;
        }
    }
}

function resetLearningProgress() {
    if (confirm('Bạn có chắc chắn muốn làm mới toàn bộ tiến độ học tập và các dạng bài đã đạt không?')) {
        try {
            localStorage.removeItem('vstep_b2_completed_essays');
        } catch (e) {
            console.error('Failed to clear localStorage:', e);
        }
        updateGlobalProgress();
        renderNav();
        alert('Đã làm mới tiến độ học tập thành công!');
    }
}

// Save current recitation progress
function saveCurrentRecitationProgress() {
    if (!activeEssayTypeId) return;
    try {
        localStorage.setItem('vstep_b2_recitation_' + activeEssayTypeId, JSON.stringify({
            currentQuestionIndex,
            questionScores
        }));
    } catch (e) {}
}

// Reset Recitation State and UI
function resetRecitationUI(isRestart = false) {
    if (isRestart === true && activeEssayTypeId) {
        try { localStorage.removeItem('vstep_b2_recitation_' + activeEssayTypeId); } catch (e) {}
    }

    activeQuestions = recitationQuestions[activeEssayTypeId] || [];
    let savedProgress = null;
    try {
        const data = localStorage.getItem('vstep_b2_recitation_' + activeEssayTypeId);
        if (data) savedProgress = JSON.parse(data);
    } catch (e) {}

    if (savedProgress && savedProgress.questionScores && savedProgress.questionScores.length === activeQuestions.length) {
        currentQuestionIndex = savedProgress.currentQuestionIndex || 0;
        questionScores = savedProgress.questionScores;
    } else {
        currentQuestionIndex = 0;
        questionScores = Array(activeQuestions.length).fill(0);
    }
    
    if (recitationInput) recitationInput.value = '';
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    if (btnNextQuestion) btnNextQuestion.classList.add('hidden');
    if (btnCheckAnswer) btnCheckAnswer.classList.remove('hidden');
    
    if (totalQuestionsNum) totalQuestionsNum.textContent = activeQuestions.length;
    
    // Toggle containers
    if (recitationResultBox) recitationResultBox.classList.add('hidden');
    if (recitationQuizBox) recitationQuizBox.classList.remove('hidden');
    
    const hintBox = document.getElementById('recitationHintBox');
    if (hintBox) hintBox.classList.add('hidden');
    
    // Restore header and progress bar wrapper visibility
    const recitationHeader = document.querySelector('.recitation-header');
    if (recitationHeader) recitationHeader.classList.remove('hidden');
    
    const progressWrapper = document.querySelector('.recitation-progress-wrapper');
    if (progressWrapper) progressWrapper.style.display = '';
    
    showRecitationQuestion();
}

// Show the current question
function showRecitationQuestion() {
    if (activeQuestions.length === 0) return;
    
    const q = activeQuestions[currentQuestionIndex];
    if (questionCueText) {
        let parts = q.cue.split('<br>');
        if (parts.length === 3) {
            questionCueText.innerHTML = `<span class="cue-part-1">${parts[0]}</span><br><span class="cue-part-2">${parts[1]}</span><br><span class="cue-part-3">${parts[2]}</span>`;
        } else if (parts.length === 2) {
            questionCueText.innerHTML = `<span class="cue-part-1">${parts[0]}</span><br><span class="cue-part-3">${parts[1]}</span>`;
        } else {
            questionCueText.innerHTML = q.cue;
        }
    }
    
    const questionHintVn = document.getElementById('questionHintVn');
    if (questionHintVn) {
        if (q.vn) {
            questionHintVn.textContent = 'Gợi ý: ' + q.vn;
            questionHintVn.style.display = 'block';
        } else {
            questionHintVn.style.display = 'none';
        }
    }
    if (currentQuestionNum) currentQuestionNum.textContent = currentQuestionIndex + 1;
    
    // Update progress bar
    if (progressBarFill) {
        const percent = ((currentQuestionIndex + 1) / activeQuestions.length) * 100;
        progressBarFill.style.width = `${percent}%`;
    }
    
    // Reset inputs & feedback for this question
    if (recitationInput) recitationInput.value = '';
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    
    const hintBox = document.getElementById('recitationHintBox');
    if (hintBox) hintBox.classList.add('hidden');
    
    // Manage buttons visibility
    if (btnCheckAnswer) btnCheckAnswer.classList.remove('hidden');
    if (btnNextQuestion) btnNextQuestion.classList.add('hidden');
    
    // Disable/enable Prev button
    if (btnPrevQuestion) {
        if (currentQuestionIndex === 0) {
            btnPrevQuestion.disabled = true;
            btnPrevQuestion.style.opacity = '0.5';
            btnPrevQuestion.style.cursor = 'not-allowed';
        } else {
            btnPrevQuestion.disabled = false;
            btnPrevQuestion.style.opacity = '1';
            btnPrevQuestion.style.cursor = 'pointer';
        }
    }
}

// Check recitation answer
function checkRecitationAnswer() {
    if (activeQuestions.length === 0) return;
    const q = activeQuestions[currentQuestionIndex];
    const userAns = recitationInput ? recitationInput.value.trim() : '';
    
    if (userAns === '') {
        alert('Vui lòng nhập câu trả lời của bạn trước khi kiểm tra!');
        return;
    }
    
    const diffResult = diffWords(userAns, q.target);
    
    // Track score
    questionScores[currentQuestionIndex] = diffResult.accuracy;
    saveCurrentRecitationProgress();
    
    if (recitationFeedback) recitationFeedback.classList.remove('hidden');
    
    // Build user diff display
    if (userDiffResult) {
        userDiffResult.innerHTML = '';
        diffResult.diff.forEach(d => {
            if (d.type === 'match') {
                const span = document.createElement('span');
                span.className = 'diff-word-match';
                span.textContent = d.word + ' ';
                userDiffResult.appendChild(span);
            } else if (d.type === 'extra') {
                const span = document.createElement('span');
                span.className = 'diff-word-extra';
                span.textContent = d.word + ' ';
                userDiffResult.appendChild(span);
            }
        });
        if (userDiffResult.innerHTML === '') {
            userDiffResult.innerHTML = '<em>(Bỏ trống)</em>';
        }
    }
    
    // Build correct text display
    if (correctTextResult) {
        correctTextResult.innerHTML = '';
        diffResult.diff.forEach(d => {
            if (d.type === 'match') {
                const span = document.createElement('span');
                span.className = 'diff-word-match';
                span.textContent = d.word + ' ';
                correctTextResult.appendChild(span);
            } else if (d.type === 'missing') {
                const span = document.createElement('span');
                span.className = 'diff-word-mismatch';
                span.textContent = d.word + ' ';
                correctTextResult.appendChild(span);
            }
        });
    }
    
    // Update status banner
    if (feedbackStatus) {
        feedbackStatus.className = 'feedback-status';
        if (diffResult.isPerfect) {
            feedbackStatus.classList.add('status-success');
            feedbackStatus.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>Chính xác tuyệt đối! (Độ chính xác: 100%)</span>`;
        } else {
            feedbackStatus.classList.add('status-error');
            feedbackStatus.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <span>Chưa chính xác! Độ chính xác: ${diffResult.accuracy}%. Xem phần so sánh bên dưới.</span>`;
        }
    }
    
    // Manage Next/Finish button
    if (btnNextQuestion) {
        btnNextQuestion.classList.remove('hidden');
        if (currentQuestionIndex === activeQuestions.length - 1) {
            btnNextQuestion.innerHTML = `Hoàn thành & Đánh giá <i class="fa-solid fa-chart-simple"></i>`;
            btnNextQuestion.className = 'btn btn-primary';
        } else {
            btnNextQuestion.innerHTML = `Câu tiếp theo <i class="fa-solid fa-chevron-right"></i>`;
            btnNextQuestion.className = 'btn btn-success';
        }
    }
}

// Show hint instead of full answer
function showRecitationHint() {
    if (activeQuestions.length === 0) return;
    const q = activeQuestions[currentQuestionIndex];
    
    const hintBox = document.getElementById('recitationHintBox');
    const hintText = document.getElementById('recitationHintText');
    
    if (hintBox && hintText) {
        hintBox.classList.remove('hidden');
        
        // Generate hint: Keep first 4 words, then just first letter of each subsequent word
        const words = q.target.split(' ');
        if (words.length <= 4) {
            hintText.textContent = words[0] + ' ...';
        } else {
            let hint = words.slice(0, 4).join(' ') + ' ';
            for (let i = 4; i < words.length; i++) {
                let word = words[i];
                if (word.startsWith('[')) {
                    hint += word + ' ';
                } else {
                    let firstLetter = word.charAt(0);
                    let rest = word.slice(1).replace(/[a-zA-ZÀ-ỹ]/g, '_');
                    hint += firstLetter + rest + ' ';
                }
            }
            hintText.textContent = hint.trim();
        }
    }
}


// Next recitation question
function nextRecitationQuestion() {
    if (currentQuestionIndex < activeQuestions.length - 1) {
        currentQuestionIndex++;
        saveCurrentRecitationProgress();
        showRecitationQuestion();
    } else {
        showEvaluationResult();
    }
}

// Show evaluation result screen
function showEvaluationResult() {
    // Hide quiz box and feedback panel
    if (recitationQuizBox) recitationQuizBox.classList.add('hidden');
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    
    // Hide header and progress bar wrapper during evaluation results
    const recitationHeader = document.querySelector('.recitation-header');
    if (recitationHeader) recitationHeader.classList.add('hidden');
    
    const progressWrapper = document.querySelector('.recitation-progress-wrapper');
    if (progressWrapper) progressWrapper.style.display = 'none';
    
    // Calculate average score
    const totalQuestions = activeQuestions.length;
    const totalScore = questionScores.reduce((sum, s) => sum + s, 0);
    const averageScore = totalQuestions > 0 ? Math.round(totalScore / totalQuestions) : 0;
    
    // Update score text
    if (scorePercentageVal) scorePercentageVal.textContent = averageScore;
    
    // Get active essay type data for dynamic title
    const typeData = essayTypes.find(t => t.id === activeEssayTypeId);
    const essayTitleEn = typeData ? typeData.titleEn : 'This Essay Type';
    
    const evalCard = document.querySelector('.evaluation-card');
    
    if (averageScore >= 90) {
        // Passed state
        if (resultStatusVal) {
            resultStatusVal.textContent = 'ĐẠT';
        }
        if (resultMessageVal) {
            resultMessageVal.textContent = `Chúc mừng bạn đã chinh phục được ${essayTitleEn}. Nhiệm vụ đã được hoàn thành, hãy tiếp tục với phần tiếp theo.`;
        }
        if (evaluationIcon) {
            evaluationIcon.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
        }
        if (evalCard) {
            evalCard.classList.remove('failed');
            evalCard.classList.add('passed');
        }
        markEssayCompleted(activeEssayTypeId);
    } else {
        // Failed state
        if (resultStatusVal) {
            resultStatusVal.textContent = 'KHÔNG ĐẠT';
        }
        if (resultMessageVal) {
            resultMessageVal.textContent = 'Xin vui lòng ôn lại bài thật kỹ và trả bài lại một lần nữa.';
        }
        if (evaluationIcon) {
            evaluationIcon.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i>';
        }
        if (evalCard) {
            evalCard.classList.remove('passed');
            evalCard.classList.add('failed');
        }
    }
    
    // Show result box
    if (recitationResultBox) recitationResultBox.classList.remove('hidden');
}

// Prev recitation question
function prevRecitationQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        saveCurrentRecitationProgress();
        showRecitationQuestion();
    }
}

// Show Welcome Screen
function showWelcomeScreen() {
    activeEssayTypeId = null;
    
    // Update active nav
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    const homeItem = document.querySelector('.home-nav-item');
    if (homeItem) homeItem.classList.add('active');

    // Show welcome, hide content
    if (welcomeScreen) welcomeScreen.style.display = 'flex';
    if (essayContent) essayContent.classList.add('hidden');

    // Reset Title
    if (mainTitle) {
        mainTitle.innerHTML = `
            <div class="main-title-en placeholder-blink">Chọn một dạng bài để bắt đầu NHIỆM VỤ HỆ THỐNG của bạn!</div>
        `;
    }
}

// Render Navigation
function renderNav() {
    if (!essayNav) return;
    essayNav.innerHTML = ''; // Clear existing
    
    // Add Home button first
    const homeItem = document.createElement('div');
    homeItem.className = 'nav-item home-nav-item active';
    homeItem.innerHTML = `
        <i class="fa-solid fa-house"></i>
        <div class="nav-text">
            <div class="nav-title-en" style="font-weight: bold;">TRANG CHỦ</div>
            <div class="nav-title-vi">Màn hình khởi đầu</div>
        </div>
    `;
    homeItem.addEventListener('click', showWelcomeScreen);
    essayNav.appendChild(homeItem);

    const completed = getCompletedEssays();

    essayTypes.forEach(type => {
        const isCompleted = completed.includes(type.id);
        const navItem = document.createElement('div');
        navItem.className = 'nav-item';
        navItem.dataset.id = type.id;
        navItem.innerHTML = `
            <i class="fa-solid ${type.icon}"></i>
            <div class="nav-text">
                <div class="nav-title-en">${type.titleEn}</div>
                <div class="nav-title-vi">${type.titleVi}</div>
            </div>
            ${isCompleted ? '<span class="nav-completed-badge" title="Đã chinh phục"><i class="fa-solid fa-circle-check"></i></span>' : ''}
        `;
        
        navItem.addEventListener('click', () => selectEssayType(type.id));
        essayNav.appendChild(navItem);
    });
}


// Select an Essay Type
function selectEssayType(id) {
    activeEssayTypeId = id;
    
    // Update active nav
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.dataset.id === id) item.classList.add('active');
    });

    const typeData = essayTypes.find(t => t.id === id);
    if (!typeData) return;

    // Hide welcome, show content
    if (welcomeScreen) welcomeScreen.style.display = 'none';
    if (essayContent) essayContent.classList.remove('hidden');

    // Set Title
    if (mainTitle) {
        mainTitle.innerHTML = `
            <div class="main-title-en">${typeData.titleEn}</div>
            <div class="main-title-vi">${typeData.titleVi}</div>
        `;
    }

    // Populate Content
    const basicInfoPanel = document.getElementById('basicInfoPanel');
    const identifyingSignsPanel = document.getElementById('identifyingSignsPanel');
    const detailedOutlinePanel = document.getElementById('detailedOutlinePanel');
    const sampleWritingPanel = document.getElementById('sampleWritingPanel');

    if (basicInfoPanel) basicInfoPanel.innerHTML = typeData.basicInfo;
    if (identifyingSignsPanel) identifyingSignsPanel.innerHTML = typeData.identifyingSigns;
    if (detailedOutlinePanel) {
        detailedOutlinePanel.innerHTML = typeData.detailedOutline.replace(/\[([^\]]+)\]/g, '[<strong>$1</strong>]');
    }
    if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;

    // Reset recitation for this type
    resetRecitationUI();

    // Reset tabs to first tab
    const firstTab = document.querySelector('.tab-btn[data-tab="basicInfo"]');
    if (firstTab) firstTab.click();
}

// Initialize application on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    // Query DOM Elements
    essayNav = document.getElementById('essayNav');
    mainTitle = document.getElementById('mainTitle');
    welcomeScreen = document.getElementById('welcomeScreen');
    essayContent = document.getElementById('essayContent');
    themeToggle = document.getElementById('themeToggle');

    // Query Recitation Elements
    recitationInput = document.getElementById('recitationInput');
    btnPrevQuestion = document.getElementById('btnPrevQuestion');
    btnShowHint = document.getElementById('btnShowHint');
    btnCheckAnswer = document.getElementById('btnCheckAnswer');
    btnNextQuestion = document.getElementById('btnNextQuestion');
    currentQuestionNum = document.getElementById('currentQuestionNum');
    totalQuestionsNum = document.getElementById('totalQuestionsNum');
    progressBarFill = document.getElementById('progressBarFill');
    questionCueText = document.getElementById('questionCueText');
    recitationFeedback = document.getElementById('recitationFeedback');
    feedbackStatus = document.getElementById('feedbackStatus');
    userDiffResult = document.getElementById('userDiffResult');
    correctTextResult = document.getElementById('correctTextResult');

    // Query Evaluation Elements
    recitationQuizBox = document.getElementById('recitationQuizBox');
    recitationResultBox = document.getElementById('recitationResultBox');
    scorePercentageVal = document.getElementById('scorePercentageVal');
    resultStatusVal = document.getElementById('resultStatusVal');
    resultMessageVal = document.getElementById('resultMessageVal');
    btnRestartRecitation = document.getElementById('btnRestartRecitation');
    evaluationIcon = document.getElementById('evaluationIcon');

    // Render navigation
    renderNav();

    // Update global progress on load
    updateGlobalProgress();

    // Reset progress button listener
    const btnResetProgress = document.getElementById('btnResetProgress');
    if (btnResetProgress) btnResetProgress.addEventListener('click', resetLearningProgress);

    // Handle Tabs
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Remove active class from all buttons and panels
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            // Add active class to clicked button
            e.currentTarget.classList.add('active');

            // Show corresponding panel
            const tabId = e.currentTarget.dataset.tab;
            const panel = document.getElementById(`${tabId}Panel`);
            if (panel) panel.classList.add('active');
        });
    });

    // Recitation Button Listeners
    if (btnPrevQuestion) btnPrevQuestion.addEventListener('click', prevRecitationQuestion);
    if (btnShowHint) btnShowHint.addEventListener('click', showRecitationHint);
    if (btnCheckAnswer) btnCheckAnswer.addEventListener('click', checkRecitationAnswer);
    if (btnNextQuestion) btnNextQuestion.addEventListener('click', nextRecitationQuestion);
    if (btnRestartRecitation) btnRestartRecitation.addEventListener('click', () => resetRecitationUI(true));

    // Theme Toggle
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            isDarkMode = !isDarkMode;
            if (isDarkMode) {
                document.documentElement.setAttribute('data-theme', 'dark');
                themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
            } else {
                document.documentElement.removeAttribute('data-theme');
                themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
            }
        });
    }

    // Initialize Login State
    initLoginState();
});

// =========================================
// LOGIN & ACCESS CONTROL
// =========================================
const ALLOWED_CLASSES = ['CB210', 'CB211', 'CB213', 'ONB103', 'B212', 'B2', 'GV'];
const BANNED_CLASSES = ['CB201', 'CB202', 'B220', 'CB206', 'CB196', 'B209'];

const STUDENTS_BY_CLASS = {
    'CB210': [
        "Nguyễn Võ Thành Đạt", "Lê Huỳnh Thanh Duy", "Nguyễn Cao Kỳ Duyên", "Đào Ngọc Hân",
        "Trần Văn Hữu", "Trần Văn Kim Khoa", "Nguyễn Thanh Nâng", "Huỳnh Kỳ Nguyên",
        "Võ Thị Kim Nguyên", "Võ Hùng Sanh", "Tiền Thị Thanh Thảo", "Trần Thị Thanh Thảo",
        "Đặng Thị Kim Thoa", "Trần Thị Tiên Tiên", "Lê Kim Tuyền"
    ],
    'CB211': [
        "Hồ Anh Quân", "Lê Thành Nghiệp", "Lê Khánh Lâm", "Huỳnh Thị Ngọc Thắm",
        "Mai Trần Xuân Mai", "Lê Thị Uyển Nhi", "Nguyễn Thụy Thanh Trúc"
    ],
    'CB213': [
        "Nguyễn Quốc Anh", "Hoàng Hợp Minh Châu", "Đặng Châu Gia Huy", "Trần Minh Tuệ Mẩn",
        "Trần Minh Tuệẫn", "Đặng Thị Trúc Măng", "Trương Thị Kha My", "Ngô Diễm My",
        "Chiêm Chúc Ngân", "Huỳnh Thị Yến Nhi", "Phạm Nguyễn Tâm Như", "Phạm Nhựt Tiến",
        "Phạm Nhật Tiến", "Lê Thị Tú Trinh", "Trần Ngọc Vinh"
    ],
    'ONB103': [
        "Nguyễn Thị Duy", "Phạm Trần Mỹ Hân", "Trịnh Thị Thu Hiền", "Nguyễn Hoàng Kha",
        "Phạm Thị Út Lụa", "Phạm Thị Út Lua", "Lê Huỳnh Diễm My", "Nguyễn Thị Ngọc Mỹ",
        "Huỳnh Thị Kim Ngân", "Trần Thị Kim Ngân", "Nguyễn Thị Tiểu Phụng", "Trần Yến Phụng",
        "Phạm Ngọc Thạch", "Cao Thị Thu Trang", "Nguyễn Thị Thanh Tuyền", "Trần Phạm Phương Uyên",
        "Trần Ngô Mỹ Vy"
    ],
    'B212': [
        "Nguyễn Duy Hồng Anh", "Nguyễn Ngọc Minh Anh", "Nguyễn Lê Mỹ Hân", "Nguyễn Hồng Minh Huy",
        "Nguyễn Quốc Khải", "Đoàn Nguyễn Đình Khang", "Lê Nguyễn Gia Khánh", "Nguyễn Hữu Khánh",
        "Hồ Thị Ngọc Lan", "Trần Thị Hồng Lỉnh", "Trần Thị Hồng Lĩnh", "Võ Thị Triệu Minh",
        "Hứa Đình Nghi", "Võ Thị Bảo Ngọc", "Lê Tiến Phát", "Nguyễn Hoàng Thông",
        "Trần Hoàng Thông", "Nguyễn Kim Tiền", "Lê Thị Bảo Trân", "Võ Thị Diễm Trinh",
        "Nguyễn Tấn Trung", "Nguyễn Tiến Trung", "Trần Thị Ánh Tuyết", "Đặng Nguyễn Khánh Uyên",
        "Nguyễn Thị Chúc Yến"
    ],
    'B2': [
        "Gia Tuệ", "Gia Tuê", "Nguyễn Gia Tuệ", "Trần Gia Tuệ", "Lê Gia Tuệ"
    ]
};

function removeVietnameseTonesB2(str) {
    return (str || '')
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .replace(/đ/g, 'd').replace(/Đ/g, 'D');
}

function normalizeNameB2(str) {
    return (str || '')
        .normalize('NFC')
        .toLowerCase()
        .replace(/\s+/g, ' ')
        .trim();
}

function cleanAccessPassword(pwd) {
    return (pwd || '')
        .trim()
        .toUpperCase()
        .replace(/\s+/g, '')
        .replace(/Ư/g, 'W')
        .replace(/Ơ/g, 'OW')
        .replace(/Ê/g, 'E');
}

function initLoginState() {
    const loginOverlay = document.getElementById('loginOverlay');
    const appContainer = document.getElementById('appContainer');
    const studentNameInput = document.getElementById('studentName');
    const studentClassInput = document.getElementById('studentClass');
    const studentPasswordInput = document.getElementById('studentPassword');
    const btnLogin = document.getElementById('btnLogin');
    const btnTogglePwd = document.getElementById('btnTogglePwd');
    const togglePwdIcon = document.getElementById('togglePwdIcon');

    if (!loginOverlay || !appContainer) return;

    // Password toggle
    if (btnTogglePwd && studentPasswordInput) {
        btnTogglePwd.addEventListener('click', () => {
            const isPwd = (studentPasswordInput.type === 'password');
            studentPasswordInput.type = isPwd ? 'text' : 'password';
            btnTogglePwd.title = isPwd ? 'Ẩn mật khẩu' : 'Hiện mật khẩu';
            if (togglePwdIcon) {
                if (isPwd) {
                    togglePwdIcon.innerHTML = `<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line>`;
                } else {
                    togglePwdIcon.innerHTML = `<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>`;
                }
            }
        });
    }

    // Pre-fill previously saved info if any
    const savedName = localStorage.getItem('vstep_b2_student_name') || '';
    const savedClass = localStorage.getItem('vstep_b2_student_class') || '';
    if (studentNameInput && savedName) studentNameInput.value = savedName;
    if (studentClassInput && savedClass) studentClassInput.value = savedClass;

    // Check session login state
    const isSessionLoggedIn = sessionStorage.getItem('vstep_b2_session_logged_in');
    if (isSessionLoggedIn === 'true') {
        loginOverlay.style.display = 'none';
        appContainer.style.display = 'flex';
    } else {
        loginOverlay.style.display = 'flex';
        appContainer.style.display = 'none';
    }

    if (btnLogin) {
        btnLogin.addEventListener('click', handleLogin);
    }

    if (studentNameInput) {
        studentNameInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                if (studentClassInput && !studentClassInput.value.trim()) {
                    studentClassInput.focus();
                } else if (studentPasswordInput && !studentPasswordInput.value.trim()) {
                    studentPasswordInput.focus();
                } else {
                    handleLogin();
                }
            }
        });
    }

    if (studentClassInput) {
        studentClassInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                if (studentPasswordInput && !studentPasswordInput.value.trim()) {
                    studentPasswordInput.focus();
                } else {
                    handleLogin();
                }
            }
        });
    }

    if (studentPasswordInput) {
        studentPasswordInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                handleLogin();
            }
        });
    }
}

function handleLogin() {
    const studentNameInput = document.getElementById('studentName');
    const studentClassInput = document.getElementById('studentClass');
    const studentPasswordInput = document.getElementById('studentPassword');
    const loginError = document.getElementById('loginError');
    const btnLogin = document.getElementById('btnLogin');
    const loginOverlay = document.getElementById('loginOverlay');
    const appContainer = document.getElementById('appContainer');

    const nameVal = studentNameInput ? studentNameInput.value.trim() : '';
    const rawClassVal = studentClassInput ? studentClassInput.value.trim().toUpperCase().replace(/\s+/g, '') : '';
    const passwordVal = studentPasswordInput ? studentPasswordInput.value.trim() : '';

    if (!nameVal) {
        showLoginError('Vui lòng nhập đầy đủ Họ và tên.');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    const normName = nameVal.toUpperCase();
    const noToneName = removeVietnameseTonesB2(normalizeNameB2(nameVal));
    let finalClassVal = rawClassVal.replace(/^(LỚP|LOP|CLASS)\s*/i, '');
    const noToneClass = removeVietnameseTonesB2(finalClassVal.toLowerCase()).replace(/[^a-z0-9]/g, '').toUpperCase();
    if (noToneClass === 'B2' || noToneClass.includes('GIATUE')) {
        finalClassVal = 'B2';
    } else {
        finalClassVal = noToneClass;
    }

    const isTeacher = (
        normName === 'PTMN' ||
        noToneName.includes('co nguyet') ||
        noToneName.includes('miss nguyet') ||
        noToneName.includes('pham thi minh nguyet') ||
        finalClassVal === 'GV' ||
        cleanAccessPassword(passwordVal) === 'PTMN'
    );
    let finalStudentName = isTeacher ? (nameVal || 'PTMN') : nameVal;

    if (isTeacher) {
        if (!finalClassVal) finalClassVal = 'GV';
    } else {
        if (!finalClassVal || !ALLOWED_CLASSES.includes(finalClassVal)) {
            showLoginError('Hệ thống hiện chỉ mở cho các lớp: CB210, CB211, CB213, ONB103, B212 và Gia Tuệ (B2)!');
            if (studentClassInput) studentClassInput.focus();
            return;
        }

        const isGiaTue = noToneName.includes('gia tue') || noToneName.replace(/\s+/g, '').includes('giatue');
        if (finalClassVal === 'B2') {
            if (!isGiaTue) {
                showLoginError('Mã lớp B2 hiện chỉ dành riêng cho học viên Gia Tuệ (B2)!');
                if (studentNameInput) studentNameInput.focus();
                return;
            }
            finalStudentName = 'Gia Tuệ';
        } else {
            const roster = STUDENTS_BY_CLASS[finalClassVal] || [];
            const normInp = normalizeNameB2(nameVal);
            const matched = roster.find(st => {
                const nSt = normalizeNameB2(st);
                return nSt === normInp || removeVietnameseTonesB2(nSt) === noToneName;
            });

            if (matched) {
                finalStudentName = matched;
            } else if (finalClassVal === 'B212' && isGiaTue) {
                finalStudentName = 'Gia Tuệ';
                finalClassVal = 'B2';
            } else {
                showLoginError(`Họ và tên "${nameVal}" không có trong danh sách lớp ${finalClassVal}.`);
                if (studentNameInput) studentNameInput.focus();
                return;
            }
        }

        if (!passwordVal) {
            showLoginError('Vui lòng nhập Mật khẩu.');
            if (studentPasswordInput) studentPasswordInput.focus();
            return;
        }

        const cleanedPwd = cleanAccessPassword(passwordVal);
        if (!['STUDYHARD', 'VSTEPWRITING', 'VSTEOWRITING', 'PRACTICEWRITING', 'PTMN'].includes(cleanedPwd)) {
            showLoginError('Mật khẩu không đúng. Vui lòng kiểm tra lại!');
            if (studentPasswordInput) {
                studentPasswordInput.focus();
                studentPasswordInput.select();
            }
            return;
        }
    }

    if (loginError) loginError.style.display = 'none';

    if (btnLogin) {
        btnLogin.innerHTML = '<span>ĐANG ĐĂNG NHẬP...</span>';
        btnLogin.disabled = true;
    }

    // Prepare Google Form submission
    const formEntryInfo = document.getElementById('formEntryInfo');
    const googleForm = document.getElementById('googleForm');
    const combinedData = `${nameVal} - Lớp ${rawClassVal}`;

    if (formEntryInfo) formEntryInfo.value = combinedData;

    // Submit via hidden form iframe
    try {
        if (googleForm) googleForm.submit();
    } catch (err) {
        console.warn('Form submit error:', err);
    }

    // Submit via fetch no-cors as additional reliable channel
    try {
        const formData = new FormData();
        formData.append('entry.388968236', combinedData);
        fetch('https://docs.google.com/forms/d/e/1FAIpQLSdbWEXCNWwUKM5B1gVK889PvPpYdmJ6wTERVcyplNHE0CUbEw/formResponse', {
            method: 'POST',
            mode: 'no-cors',
            body: formData
        }).catch(() => {});
    } catch (e) {}

    // Save info
    localStorage.setItem('vstep_b2_student_name', isTeacher ? 'PTMN' : nameVal);
    localStorage.setItem('vstep_b2_student_class', finalClassVal);
    localStorage.setItem('vstep_b2_student_info', `${isTeacher ? 'PTMN' : nameVal} - Lớp ${finalClassVal}`);
    sessionStorage.setItem('vstep_b2_session_logged_in', 'true');

    // Unlock App
    setTimeout(() => {
        if (loginOverlay) loginOverlay.style.display = 'none';
        if (appContainer) appContainer.style.display = 'flex';
        if (btnLogin) {
            btnLogin.innerHTML = '<span>BẮT ĐẦU HỌC</span> <i class="fa-solid fa-arrow-right"></i>';
            btnLogin.disabled = false;
        }
    }, 300);
}

function showLoginError(msg) {
    const loginError = document.getElementById('loginError');
    if (loginError) {
        loginError.textContent = msg;
        loginError.style.display = 'block';
    }
}

// Hàm hiển thị bản dịch tiếng Việt
window.toggleTranslation = function(btn) {
    const content = btn.nextElementSibling;
    if (content.style.display === 'none') {
        content.style.display = 'block';
        btn.innerHTML = '<i class="fa-solid fa-eye-slash"></i> Ẩn bản dịch tiếng Việt';
    } else {
        content.style.display = 'none';
        btn.innerHTML = '<i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt';
    }
};

