with open("app.js", "a", encoding="utf-8") as f:
    f.write("\n// Hàm hiển thị bản dịch tiếng Việt\nwindow.toggleTranslation = function(btn) {\n    const content = btn.nextElementSibling;\n    if (content.style.display === 'none') {\n        content.style.display = 'block';\n        btn.innerHTML = '<i class=\"fa-solid fa-eye-slash\"></i> Ẩn bản dịch tiếng Việt';\n    } else {\n        content.style.display = 'none';\n        btn.innerHTML = '<i class=\"fa-solid fa-language\"></i> Xem bản dịch tiếng Việt';\n    }\n};\n")

with open("style.css", "a", encoding="utf-8") as f:
    f.write("""
/* Translation Button & Content */
.translation-toggle-btn {
    background-color: var(--bg-card);
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 15px;
    font-weight: 500;
    font-family: var(--font-body);
    margin-top: 15px;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.translation-toggle-btn:hover {
    background-color: var(--primary-color);
    color: white;
}

[data-theme="dark"] .translation-toggle-btn {
    background-color: var(--bg-card);
    color: var(--primary-color);
}
[data-theme="dark"] .translation-toggle-btn:hover {
    background-color: var(--primary-color);
    color: #fff;
}

.translation-content .sample-letter-box {
    margin-top: 15px;
    border-top: 4px solid #10b981;
    background-color: var(--bg-body);
    color: var(--text-muted);
}
[data-theme="dark"] .translation-content .sample-letter-box {
    background-color: #1e293b;
    color: #cbd5e1;
}
""")
