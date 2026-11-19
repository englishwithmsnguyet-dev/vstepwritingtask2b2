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
    const userClass = getUserClass();
    const isSingleTypeClass = (userClass === 'B212');
    const isTwoTypeClass = ['CB211', 'CB213', 'ONB103'].includes(userClass);
    const total = isSingleTypeClass ? 1 : (isTwoTypeClass ? 2 : 4);
    const validCompleted = isSingleTypeClass
        ? completed.filter(id => id === 'adv-disadv')
        : (isTwoTypeClass ? completed.filter(id => id === 'adv-disadv' || id === 'cause-effect') : completed);
    const count = validCompleted.length;
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
            dashStatus.textContent = (isSingleTypeClass || isTwoTypeClass)
                ? "🎉 TUYỆT VỜI! Bạn đã xuất sắc hoàn thành các dạng bài được mở cho lớp của mình!"
                : "🎉 TUYỆT VỜI! Bạn đã xuất sắc chinh phục tất cả 4 dạng luận VSTEP Writing Task 02!";
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

// Recitation Timer Variables & Functions
let recitationTimerBadge;
let recitationCountdown;
let timeSpentVal;
let recitationTimerInterval = null;
const RECITATION_TIME_LIMIT = 20 * 60; // 20 minutes = 1200 seconds
let recitationTimeRemaining = RECITATION_TIME_LIMIT;
let isRecitationTimerRunning = false;

function formatTimerString(totalSeconds) {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    const pad = (n) => (n < 10 ? '0' + n : n);
    return `${pad(mins)}:${pad(secs)}`;
}

function updateRecitationTimerDisplay() {
    if (recitationCountdown) {
        recitationCountdown.textContent = formatTimerString(recitationTimeRemaining);
    }

    if (recitationTimerBadge) {
        recitationTimerBadge.classList.remove('timer-normal', 'timer-warning', 'timer-urgent');
        if (recitationTimeRemaining > 300) {
            recitationTimerBadge.classList.add('timer-normal');
        } else if (recitationTimeRemaining > 60) {
            recitationTimerBadge.classList.add('timer-warning');
        } else {
            recitationTimerBadge.classList.add('timer-urgent');
        }
    }
}

function startRecitationTimer() {
    if (isRecitationTimerRunning) return;
    if (recitationTimeRemaining <= 0) {
        recitationTimeRemaining = RECITATION_TIME_LIMIT;
    }
    isRecitationTimerRunning = true;
    updateRecitationTimerDisplay();

    if (recitationTimerInterval) clearInterval(recitationTimerInterval);
    recitationTimerInterval = setInterval(() => {
        if (recitationTimeRemaining > 0) {
            recitationTimeRemaining--;
            updateRecitationTimerDisplay();
            if (recitationTimeRemaining % 3 === 0) {
                saveCurrentRecitationProgress();
            }
        } else {
            handleRecitationTimeUp();
        }
    }, 1000);
}

function stopRecitationTimer() {
    if (recitationTimerInterval) {
        clearInterval(recitationTimerInterval);
        recitationTimerInterval = null;
    }
    isRecitationTimerRunning = false;
}

function resetRecitationTimer() {
    stopRecitationTimer();
    recitationTimeRemaining = RECITATION_TIME_LIMIT;
    updateRecitationTimerDisplay();
}

function handleRecitationTimeUp() {
    stopRecitationTimer();
    if (recitationInput) recitationInput.disabled = true;
    const userAns = recitationInput ? recitationInput.value.trim() : '';
    if (userAns && (!recitationFeedback || recitationFeedback.classList.contains('hidden'))) {
        const q = activeQuestions[currentQuestionIndex];
        if (q) {
            const diffResult = diffWords(userAns, q.target);
            questionScores[currentQuestionIndex] = diffResult.accuracy;
        }
    }
    alert('⏰ ĐÃ HẾT THỜI GIAN 20 PHÚT LÀM BÀI!\nHệ thống tự động nộp bài và hiển thị kết quả đánh giá trả bài của bạn.');
    showEvaluationResult();
}

// --- Anti-Cheat & Auto-Save State ---
let violationCount = 0;
let isAntiCheatModalOpen = false;
let isTabHidden = false;

function isRecitationSessionActive() {
    const practicePanel = document.getElementById('writingPracticePanel');
    const isPracticeActive = practicePanel && practicePanel.classList.contains('active');
    const isQuizVisible = recitationQuizBox && !recitationQuizBox.classList.contains('hidden');
    const isResultHidden = recitationResultBox && recitationResultBox.classList.contains('hidden');
    return Boolean(activeEssayTypeId && isPracticeActive && isQuizVisible && isResultHidden);
}

function getRecitationStorageKey() {
    if (!activeEssayTypeId) return null;
    return `vstep_b2_recitation_save_${activeEssayTypeId}`;
}

// Save current recitation progress
function saveCurrentRecitationProgress() {
    if (!isRecitationSessionActive()) return;
    const key = getRecitationStorageKey();
    if (!key) return;

    const data = {
        essayTypeId: activeEssayTypeId,
        questionIndex: currentQuestionIndex,
        questionScores: questionScores,
        timeRemaining: recitationTimeRemaining,
        violationCount: violationCount,
        userDraft: recitationInput ? recitationInput.value : '',
        timestamp: Date.now()
    };
    try {
        localStorage.setItem(key, JSON.stringify(data));
    } catch (e) {
        console.error('Failed to auto-save progress', e);
    }
}

function loadSavedRecitationProgress() {
    const key = getRecitationStorageKey();
    if (!key) return null;
    try {
        const raw = localStorage.getItem(key);
        if (!raw) return null;
        const data = JSON.parse(raw);
        if (Date.now() - data.timestamp > 24 * 60 * 60 * 1000) {
            localStorage.removeItem(key);
            return null;
        }
        return data;
    } catch (e) {
        return null;
    }
}

function clearSavedRecitationProgress() {
    const key = getRecitationStorageKey();
    if (key) {
        try { localStorage.removeItem(key); } catch (e) {}
    }
}

function recordAntiCheatViolation(reason) {
    if (isAntiCheatModalOpen) return;
    violationCount++;
    saveCurrentRecitationProgress();
    showAntiCheatModal(reason);
}

function showAntiCheatModal(reason) {
    isAntiCheatModalOpen = true;
    const modal = document.getElementById('antiCheatModal');
    const countEl = document.getElementById('modalViolationCount');
    const reasonEl = document.getElementById('modalViolationReason');
    if (countEl) countEl.textContent = violationCount;
    if (reasonEl) reasonEl.textContent = reason || 'Hệ thống phát hiện hành vi rời khỏi bài thi hoặc chuyển tab tra cứu!';
    if (modal) modal.classList.remove('hidden');
}

function dismissAntiCheatModal() {
    const modal = document.getElementById('antiCheatModal');
    if (modal) modal.classList.add('hidden');
    isAntiCheatModalOpen = false;
    if (recitationInput && !recitationInput.disabled) {
        recitationInput.focus();
    }
}

// Exit Recitation Session cleanly (e.g. if student accidentally entered Trả Bài)
function exitRecitationSession(isAccidentalClick = false) {
    if (isAccidentalClick) {
        // Revert violation penalty since the student intended to exit
        if (violationCount > 0) {
            violationCount--;
        }
        dismissAntiCheatModal();
    } else {
        const confirmExit = confirm('Bạn có chắc chắn muốn THOÁT khỏi phiên Trả Bài không?\n\n• Tiến độ câu hỏi của bạn đã được tự động sao lưu.\n• Bạn sẽ quay lại tab Dàn ý chi tiết để ôn tập.');
        if (!confirmExit) return;
    }

    stopRecitationTimer();
    saveCurrentRecitationProgress();

    // Temporarily hide quiz box so isRecitationSessionActive() returns false
    if (recitationQuizBox) {
        recitationQuizBox.classList.add('hidden');
    }

    // Switch back to detailedOutline tab (or basicInfo if missing)
    const outlineTabBtn = document.querySelector('.tab-btn[data-tab="detailedOutline"]');
    if (outlineTabBtn) {
        outlineTabBtn.click();
    } else {
        const firstTabBtn = document.querySelector('.tab-btn[data-tab="basicInfo"]');
        if (firstTabBtn) firstTabBtn.click();
    }

    showToast('Đã thoát khỏi phiên Trả Bài thành công!', 'info');
}

function getStudentDisplayInfo() {
    try {
        const saved = JSON.parse(localStorage.getItem('vstep_student_info') || '{}');
        if (saved && saved.fullName) {
            if (saved.className && saved.className.trim()) {
                return `${saved.fullName} (${saved.className})`;
            }
            return saved.fullName;
        }
    } catch (e) {}
    const b2Name = localStorage.getItem('vstep_b2_student_name');
    const b2Cls = localStorage.getItem('vstep_b2_student_class');
    if (b2Name) {
        return b2Cls ? `${b2Name} (${b2Cls})` : b2Name;
    }
    const sessionClass = sessionStorage.getItem('current_user_class');
    if (sessionClass) {
        return `Học viên (${sessionClass})`;
    }
    return 'Học viên VSTEP B2';
}

// Reset Recitation State and UI - Supports Auto-Save restoration and fresh restart
function resetRecitationUI(isRestart = false) {
    activeQuestions = recitationQuestions[activeEssayTypeId] || [];
    let restoredDraft = '';

    if (isRestart) {
        clearSavedRecitationProgress();
        violationCount = 0;
        currentQuestionIndex = 0;
        questionScores = Array(activeQuestions.length).fill(0);
        recitationTimeRemaining = RECITATION_TIME_LIMIT;
    } else {
        const saved = loadSavedRecitationProgress();
        if (saved && typeof saved.questionIndex === 'number' && saved.questionIndex < activeQuestions.length) {
            currentQuestionIndex = saved.questionIndex;
            questionScores = (Array.isArray(saved.questionScores) && saved.questionScores.length === activeQuestions.length)
                ? saved.questionScores
                : Array(activeQuestions.length).fill(0);
            recitationTimeRemaining = (typeof saved.timeRemaining === 'number' && saved.timeRemaining > 0)
                ? saved.timeRemaining
                : RECITATION_TIME_LIMIT;
            violationCount = typeof saved.violationCount === 'number' ? saved.violationCount : 0;
            restoredDraft = saved.userDraft || '';
        } else {
            clearSavedRecitationProgress();
            violationCount = 0;
            currentQuestionIndex = 0;
            questionScores = Array(activeQuestions.length).fill(0);
            recitationTimeRemaining = RECITATION_TIME_LIMIT;
        }
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
    
    // Countdown timer
    stopRecitationTimer();
    updateRecitationTimerDisplay();
    startRecitationTimer();

    showRecitationQuestion();

    if (restoredDraft && recitationInput) {
        recitationInput.value = restoredDraft;
    }
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
    // Stop the timer
    stopRecitationTimer();
    const timeSpentSeconds = Math.max(0, RECITATION_TIME_LIMIT - recitationTimeRemaining);
    if (timeSpentVal) {
        timeSpentVal.textContent = formatTimerString(timeSpentSeconds);
    }

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

    // Populate student name in evaluation meta box
    const evalStudentName = document.getElementById('evalStudentName');
    if (evalStudentName) {
        evalStudentName.textContent = getStudentDisplayInfo();
    }

    // Populate anti-cheat violation count
    const violationValEl = document.getElementById('violationCountVal');
    if (violationValEl) {
        if (violationCount === 0) {
            violationValEl.innerHTML = `<span class="badge-violation badge-violation-clean"><i class="fa-solid fa-shield-check"></i> 0 lần (Trung thực)</span>`;
        } else {
            violationValEl.innerHTML = `<span class="badge-violation badge-violation-warning"><i class="fa-solid fa-triangle-exclamation"></i> ${violationCount} lần (Cảnh báo gian lận)</span>`;
        }
    }

    clearSavedRecitationProgress();
    
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

// User Class & Permission Helpers
function isTeacherUser() {
    try {
        const saved = JSON.parse(localStorage.getItem('vstep_student_info'));
        if (saved) {
            const cls = (saved.className || '').toUpperCase();
            const name = (saved.fullName || '').toUpperCase();
            if (cls === 'GV' || name === 'PTMN') return true;
        }
    } catch (e) {}
    const curCls = (sessionStorage.getItem('current_user_class') || '').toUpperCase();
    return curCls === 'GV';
}

function getUserClass() {
    try {
        const saved = JSON.parse(localStorage.getItem('vstep_student_info'));
        if (saved && saved.className) return saved.className.toUpperCase();
    } catch (e) {}
    return (sessionStorage.getItem('current_user_class') || '').toUpperCase();
}

function getTypeLockMessage(userClass) {
    if (userClass === 'B212') {
        return `🔒 Dạng luận này tạm thời chưa mở cho lớp ${userClass}. Lớp hiện mở dạng luận TYPE 01!`;
    }
    return `🔒 Dạng luận này tạm thời chưa mở cho lớp ${userClass || 'của bạn'}. Lớp hiện mở Dạng 01 và 2 dàn ý đầu của Dạng 02!`;
}

function getOutlineLockMessage(userClass) {
    if (userClass === 'B212') {
        return `🔒 Dàn ý này tạm thời chưa mở cho lớp ${userClass}. Lớp hiện mở dạng luận TYPE 01!`;
    }
    return `🔒 Dàn ý này tạm thời chưa mở cho lớp ${userClass || 'của bạn'}. Lớp hiện mở Dàn ý 01 và 2 dàn ý đầu của Dạng 02!`;
}

function isTypeLocked(typeId) {
    if (isTeacherUser()) return false;
    const userClass = getUserClass();
    if (userClass === 'B212') {
        return typeId !== 'adv-disadv';
    }
    if (['CB211', 'CB213', 'ONB103'].includes(userClass)) {
        return (typeId === 'opinion' || typeId === 'discussion');
    }
    return false;
}

function isOutlineLocked(typeId, outlineIndex) {
    if (isTeacherUser()) return false;
    const userClass = getUserClass();
    if (userClass === 'B212') {
        if (typeId !== 'adv-disadv') return true;
        return false;
    }
    if (['CB211', 'CB213', 'ONB103'].includes(userClass)) {
        if (typeId === 'cause-effect') {
            return outlineIndex >= 2; // Only first 2 outlines (index 0 and 1) are unlocked
        }
        if (typeId === 'opinion' || typeId === 'discussion') {
            return true;
        }
    }
    return false;
}

// Toast Notification
let toastNoticeTimeout = null;
function showToast(message, type = 'warning') {
    let container = document.getElementById('toastContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container';
        document.body.appendChild(container);
    }
    
    const toast = document.createElement('div');
    toast.className = `app-toast toast-${type}`;
    let icon = '<i class="fa-solid fa-triangle-exclamation"></i>';
    if (type === 'success') icon = '<i class="fa-solid fa-circle-check"></i>';
    if (type === 'danger' || type === 'lock') icon = '<i class="fa-solid fa-lock"></i>';
    
    toast.innerHTML = `${icon}<span>${message}</span>`;
    
    container.appendChild(toast);
    setTimeout(() => toast.classList.add('show'), 10);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3500);
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
    homeItem.addEventListener('click', (e) => {
        if (isRecitationSessionActive()) {
            e.preventDefault();
            e.stopPropagation();
            recordAntiCheatViolation('Rời khỏi bài thi để về trang chủ');
            return;
        }
        showWelcomeScreen();
    });
    essayNav.appendChild(homeItem);

    const completed = getCompletedEssays();

    essayTypes.forEach(type => {
        const isCompleted = completed.includes(type.id);
        const locked = isTypeLocked(type.id);
        const navItem = document.createElement('div');
        navItem.className = 'nav-item' + (locked ? ' is-locked' : '');
        navItem.dataset.id = type.id;

        let statusBadge = '';
        if (locked) {
            statusBadge = '<span class="nav-lock-badge" title="Dạng luận này tạm thời chưa mở cho lớp của bạn"><i class="fa-solid fa-lock"></i> Khoá</span>';
        } else if (isCompleted) {
            statusBadge = '<span class="nav-completed-badge" title="Đã chinh phục"><i class="fa-solid fa-circle-check"></i></span>';
        }

        navItem.innerHTML = `
            <i class="fa-solid ${locked ? 'fa-lock' : type.icon}"></i>
            <div class="nav-text">
                <div class="nav-title-en">${type.titleEn}</div>
                <div class="nav-title-vi">${type.titleVi}</div>
            </div>
            ${statusBadge}
        `;
        
        navItem.addEventListener('click', (e) => {
            if (isRecitationSessionActive()) {
                e.preventDefault();
                e.stopPropagation();
                recordAntiCheatViolation('Rời khỏi bài thi để chuyển sang dạng bài khác');
                return;
            }
            if (isTypeLocked(type.id)) {
                const userClass = getUserClass();
                showToast(getTypeLockMessage(userClass), 'warning');
                return;
            }
            selectEssayType(type.id);
        });
        essayNav.appendChild(navItem);
    });
}


/**
 * Sets up interactive sub-tabs for panels that contain multiple variants (e.g. Dàn ý 1, Dàn ý 2)
 * so users can switch between them instead of scrolling vertically.
 */
function setupVariantTabs(container, itemSelector = '.outline-variant', defaultPrefix = 'DÀN Ý') {
    if (!container) return;

    const variants = container.querySelectorAll(itemSelector);
    if (!variants || variants.length <= 1) {
        const oldNav = container.querySelector('.outline-variant-tabs-nav');
        if (oldNav) oldNav.remove();
        if (variants && variants.length === 1) {
            variants[0].style.display = 'block';
            variants[0].style.marginTop = '0';
        }
        return;
    }

    // Remove any existing variant navigation
    const oldNav = container.querySelector('.outline-variant-tabs-nav');
    if (oldNav) oldNav.remove();

    // Create tabs navigation
    const nav = document.createElement('div');
    nav.className = `outline-variant-tabs-nav ${variants.length === 2 ? 'nav-cols-2' : 'nav-cols-3'}`;

    variants.forEach((variant, index) => {
        const h3 = variant.querySelector('h3');
        const fullTitle = h3 ? h3.textContent.trim() : `${defaultPrefix} ${index + 1}`;

        let badgeText = `${defaultPrefix} 0${index + 1}`;
        let titleText = fullTitle;
        if (fullTitle.includes(':')) {
            const parts = fullTitle.split(':');
            badgeText = parts[0].trim();
            titleText = parts.slice(1).join(':').trim();
        } else if (fullTitle.includes('-')) {
            const parts = fullTitle.split('-');
            badgeText = parts[0].trim();
            titleText = parts.slice(1).join('-').trim();
        }

        const lowerWords = ['và', 'với', 'cho', 'của', 'trong', 'để', 'về'];
        const formattedTitle = titleText.trim().toLowerCase().split(/\s+/).map((w, i) => {
            if (i > 0 && lowerWords.includes(w)) return w;
            return w.charAt(0).toUpperCase() + w.slice(1);
        }).join(' ');

        const isLocked = isOutlineLocked(activeEssayTypeId, index);
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `outline-variant-tab-btn ${index === 0 ? 'active' : ''} ${isLocked ? 'is-locked' : ''}`;
        btn.innerHTML = `
            <div class="variant-tab-header">
                <span class="variant-tab-badge ${isLocked ? 'is-locked' : ''}">
                    <i class="fa-solid ${isLocked ? 'fa-lock' : 'fa-layer-group'}"></i> ${badgeText}
                </span>
                ${isLocked ? '<span class="tab-lock-badge"><i class="fa-solid fa-lock"></i> Khoá</span>' : ''}
            </div>
            <div class="variant-tab-title">${formattedTitle}</div>
        `;

        btn.addEventListener('click', () => {
            if (isOutlineLocked(activeEssayTypeId, index)) {
                const userClass = getUserClass();
                showToast(getOutlineLockMessage(userClass), 'warning');
                return;
            }
            nav.querySelectorAll('.outline-variant-tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            variants.forEach((v, vIdx) => {
                if (vIdx === index) {
                    v.style.display = 'block';
                    v.style.marginTop = '0';
                    v.classList.remove('fade-slide-in');
                    void v.offsetWidth;
                    v.classList.add('fade-slide-in');
                } else {
                    v.style.display = 'none';
                }
            });

            nav.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        });

        nav.appendChild(btn);

        // Initial display state
        if (index === 0) {
            variant.style.display = 'block';
            variant.style.marginTop = '0';
        } else {
            variant.style.display = 'none';
            variant.style.marginTop = '0';
        }
    });

    container.insertBefore(nav, container.firstChild);
}

// Select an Essay Type
function selectEssayType(id) {
    if (isTypeLocked(id)) {
        const userClass = getUserClass();
        showToast(getTypeLockMessage(userClass), 'warning');
        return;
    }
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
        detailedOutlinePanel.innerHTML = typeData.detailedOutline.replace(/\[([^\]]+)\]/g, '<span class="outline-tag">[$1]</span>');
        setupVariantTabs(detailedOutlinePanel, '.outline-variant', 'DÀN Ý');
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
    recitationTimerBadge = document.getElementById('recitationTimerBadge');
    recitationCountdown = document.getElementById('recitationCountdown');
    timeSpentVal = document.getElementById('timeSpentVal');

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
            const tabId = e.currentTarget.dataset.tab;

            // Anti-cheat: Block switching away from writingPractice while active
            if (isRecitationSessionActive() && tabId !== 'writingPractice') {
                e.preventDefault();
                e.stopPropagation();
                recordAntiCheatViolation('Chuyển sang tab nội dung khác (Dàn ý, Bài mẫu,...) để tra cứu trong khi đang làm bài');
                return;
            }

            // Remove active class from all buttons and panels
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            // Add active class to clicked button
            e.currentTarget.classList.add('active');

            // Show corresponding panel
            const panel = document.getElementById(`${tabId}Panel`);
            if (panel) panel.classList.add('active');

            if (tabId === 'writingPractice') {
                resetRecitationUI(false);
            }
        });
    });

    // Recitation Button Listeners
    if (btnPrevQuestion) btnPrevQuestion.addEventListener('click', prevRecitationQuestion);
    if (btnShowHint) btnShowHint.addEventListener('click', showRecitationHint);
    if (btnCheckAnswer) btnCheckAnswer.addEventListener('click', checkRecitationAnswer);
    if (btnNextQuestion) btnNextQuestion.addEventListener('click', nextRecitationQuestion);
    if (btnRestartRecitation) btnRestartRecitation.addEventListener('click', () => resetRecitationUI(true));

    if (recitationInput) {
        recitationInput.addEventListener('input', () => {
            saveCurrentRecitationProgress();
        });
    }

    // Anti-cheat window / tab switching detection
    document.addEventListener('visibilitychange', () => {
        if (!isRecitationSessionActive()) return;
        if (document.hidden) {
            isTabHidden = true;
        } else if (isTabHidden) {
            isTabHidden = false;
            recordAntiCheatViolation('Rời khỏi tab trình duyệt hoặc chuyển sang cửa sổ ứng dụng khác');
        }
    });

    window.addEventListener('blur', () => {
        if (!isRecitationSessionActive() || isAntiCheatModalOpen) return;
        setTimeout(() => {
            if (!document.hasFocus() && isRecitationSessionActive() && !isAntiCheatModalOpen) {
                isTabHidden = true;
            }
        }, 300);
    });

    window.addEventListener('focus', () => {
        if (!isRecitationSessionActive() || isAntiCheatModalOpen) return;
        if (isTabHidden) {
            isTabHidden = false;
            recordAntiCheatViolation('Rời khỏi tab trình duyệt hoặc chuyển sang cửa sổ ứng dụng khác');
        }
    });

    // Anti-cheat modal dismiss button
    const btnDismissAntiCheat = document.getElementById('btnDismissAntiCheat');
    if (btnDismissAntiCheat) {
        btnDismissAntiCheat.addEventListener('click', dismissAntiCheatModal);
    }

    // Exit Recitation button in header
    const btnExitRecitation = document.getElementById('btnExitRecitation');
    if (btnExitRecitation) {
        btnExitRecitation.addEventListener('click', () => exitRecitationSession(false));
    }

    // Modal Exit Recitation button ("Tôi lỡ bấm nhầm vào Trả bài")
    const btnModalExitRecitation = document.getElementById('btnModalExitRecitation');
    if (btnModalExitRecitation) {
        btnModalExitRecitation.addEventListener('click', () => exitRecitationSession(true));
    }

    document.addEventListener('keydown', (e) => {
        if (isAntiCheatModalOpen && (e.key === 'Escape' || e.key === 'Enter')) {
            dismissAntiCheatModal();
        }
    });

    // --- Anti-Copy & Anti-Paste Protection in Recitation ---
    if (recitationInput) {
        recitationInput.addEventListener('paste', (e) => {
            e.preventDefault();
            recordAntiCheatViolation('Cố tình dán (Paste) nội dung vào ô trả lời thay vì tự gõ thuộc lòng');
        });

        recitationInput.addEventListener('drop', (e) => {
            e.preventDefault();
            recordAntiCheatViolation('Cố tình kéo thả (Drag & Drop) văn bản vào ô trả lời');
        });

        recitationInput.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && (e.key.toLowerCase() === 'v')) {
                e.preventDefault();
                recordAntiCheatViolation('Cố tình dùng phím tắt dán (Ctrl+V / Cmd+V) vào bài thi');
            }
        });

        recitationInput.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            showToast('⚠️ Chuột phải đã bị vô hiệu hóa trong bài thi!', 'warning');
        });
    }

    // Block Copy / Cut during active recitation
    document.addEventListener('copy', (e) => {
        if (isRecitationSessionActive()) {
            e.preventDefault();
            showToast('⚠️ Tính năng sao chép (Copy) đã bị khóa trong bài thi!', 'warning');
        }
    });

    document.addEventListener('cut', (e) => {
        if (isRecitationSessionActive()) {
            e.preventDefault();
            showToast('⚠️ Tính năng cắt (Cut) đã bị khóa trong bài thi!', 'warning');
        }
    });

    const recitationContainer = document.querySelector('.recitation-container');
    if (recitationContainer) {
        recitationContainer.addEventListener('contextmenu', (e) => {
            if (isRecitationSessionActive()) {
                e.preventDefault();
                showToast('⚠️ Chuột phải đã bị vô hiệu hóa trong bài thi!', 'warning');
            }
        });
    }

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
    updateStudentProfileCard();

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
    updateStudentProfileCard(isTeacher ? 'Cô Nguyệt (PTMN)' : nameVal, finalClassVal);

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

function updateStudentProfileCard(name, cls) {
    const nameEl = document.getElementById('studentNameDisplay');
    const classEl = document.getElementById('studentClassDisplay');
    const avatarIcon = document.getElementById('studentAvatarIcon');
    
    if (!name) name = localStorage.getItem('vstep_b2_student_name') || '';
    if (!cls) cls = localStorage.getItem('vstep_b2_student_class') || '';
    
    const isTeacher = (cls === 'GV' || name === 'PTMN' || (cls && cls.toUpperCase() === 'GV'));
    
    if (nameEl) {
        nameEl.textContent = name || 'Chưa đăng nhập';
        nameEl.title = name || '';
    }
    if (classEl) {
        if (isTeacher) {
            classEl.innerHTML = '<span class="badge-class" style="background: rgba(16,185,129,0.15); color: #059669;">Giáo viên (GV)</span>';
        } else {
            classEl.innerHTML = `<span class="badge-class">${cls ? 'Lớp: ' + cls : 'Lớp: --'}</span>`;
        }
    }
    if (avatarIcon) {
        avatarIcon.innerHTML = isTeacher ? '<i class="fa-solid fa-chalkboard-user"></i>' : '<i class="fa-solid fa-user-graduate"></i>';
    }
}

window.reopenLoginOverlay = function() {
    if (confirm('Bạn có muốn đăng xuất và đổi thông tin tài khoản không?')) {
        sessionStorage.removeItem('vstep_b2_session_logged_in');
        const loginOverlay = document.getElementById('loginOverlay');
        const appContainer = document.getElementById('appContainer');
        if (loginOverlay) loginOverlay.style.display = 'flex';
        if (appContainer) appContainer.style.display = 'none';
        updateStudentProfileCard('', '');
    }
};

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

