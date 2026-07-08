import re

with open('/Users/nguyetpham/Desktop/WEBSITE/writing-essays-b1level/app.js', 'r') as f:
    content = f.read()

# 1. Change textContent to innerHTML for questionCueText
content = content.replace("if (questionCueText) questionCueText.textContent = q.cue;", "if (questionCueText) questionCueText.innerHTML = q.cue;")

# 2. Replace adv-disadv (DÀN Ý 1) and (DÀN Ý 2)
# But wait, some have spaces, some don't.
# Let's do string replacements.
content = content.replace("'(DÀN Ý 1) Viết câu khẳng định vấn đề có hai mặt (lợi và hại):'", "'[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>Viết câu khẳng định vấn đề có hai mặt (lợi và hại) (Mở bài):'")
content = content.replace("'(DÀN Ý 1) Viết câu giới thiệu mục đích bài viết:'", "'[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>Viết câu giới thiệu mục đích bài viết (Mở bài):'")
content = content.replace("'(DÀN Ý 1) ", "'[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>")

content = content.replace("'(DÀN Ý 2) ", "'[DÀN Ý 02 - CHỈ THUẬN LỢI]<br>")

content = content.replace("'(DÀN Ý 1: Nguyên nhân & Giải pháp) ", "'[DÀN Ý 01 - NGUYÊN NHÂN & GIẢI PHÁP]<br>")
content = content.replace("'(DÀN Ý 2: Nguyên nhân & Ảnh hưởng) ", "'[DÀN Ý 02 - NGUYÊN NHÂN & ẢNH HƯỞNG]<br>")
content = content.replace("'(DÀN Ý 3: Ảnh hưởng & Giải pháp) ", "'[DÀN Ý 03 - ẢNH HƯỞNG & GIẢI PHÁP]<br>")

with open('/Users/nguyetpham/Desktop/WEBSITE/writing-essays-b1level/app.js', 'w') as f:
    f.write(content)
