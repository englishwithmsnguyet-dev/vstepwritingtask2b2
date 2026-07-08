import re

with open('/Users/nguyetpham/Desktop/WEBSITE/writing-essays-b1level/app.js', 'r') as f:
    lines = f.readlines()

in_questions = False
for i, line in enumerate(lines):
    if 'const recitationQuestions = {' in line:
        in_questions = True
    
    if in_questions and '{cue:' in line:
        # Extract the cue text
        match = re.search(r"{cue:\s*'(.*?)',", line)
        if match:
            cue_text = match.group(1)
            
            # Skip if already formatted with 1. MỞ BÀI, etc.
            if '1. MỞ BÀI' in cue_text or '2. THÂN BÀI' in cue_text or '3. KẾT BÀI' in cue_text:
                pass # Wait, let's re-process them to be safe if we need to remove suffixes?
                # Actually, I already manually formatted some, let's let the script format everything safely.
                
            # Remove any existing headers
            cue_text = cue_text.replace('1. MỞ BÀI<br>', '')
            cue_text = cue_text.replace('2. THÂN BÀI<br>', '')
            cue_text = cue_text.replace('3. KẾT BÀI<br>', '')
            
            # Identify prefix if any
            prefix = ""
            main_text = cue_text
            prefix_match = re.search(r"^(\[DÀN Ý.*?\]<br>)(.*)$", cue_text)
            if prefix_match:
                prefix = prefix_match.group(1)
                main_text = prefix_match.group(2)
            
            # Remove (Mở bài), (Kết bài) etc from the end
            main_text = re.sub(r'\s*\(Mở bài\):?$', ':', main_text)
            main_text = re.sub(r'\s*\(Kết bài\):?$', ':', main_text)
            main_text = re.sub(r'\s*ở Kết bài:?$', ':', main_text)
            main_text = re.sub(r'\s*\(Thân bài\):?$', ':', main_text)
            
            # Make sure it ends with a colon if it's a prompt
            if not main_text.endswith(':') and not main_text.endswith('?'):
                main_text += ':'
            
            # Determine section
            lower_text = main_text.lower()
            if 'mở bài' in lower_text or 'giới thiệu chủ đề' in lower_text or 'giới thiệu mục đích' in lower_text or 'góc nhìn tích cực' in lower_text or 'nêu mức độ' in lower_text or 'khẳng định vấn đề' in lower_text or 'đồng ý / không đồng ý' in lower_text or 'thể hiện quan điểm' in lower_text:
                section = '1. MỞ BÀI<br>'
                # Special cases where 'mở bài' might be in a Thân bài context? No.
            elif 'kết bài' in lower_text or 'tóm tắt' in lower_text or 'tóm lại' in lower_text or 'khẳng định giá trị' in lower_text or 'chốt lại' in lower_text or 'khẳng định tính' in lower_text or 'hướng cải thiện' in lower_text or 'nhận xét chung' in lower_text or 'lời khuyên' in lower_text or 'nhấn mạnh lại' in lower_text:
                section = '3. KẾT BÀI<br>'
            else:
                section = '2. THÂN BÀI<br>'
                
            new_cue = prefix + section + main_text
            
            # Replace in line
            line = line.replace(f"'{match.group(1)}'", f"'{new_cue}'")
            lines[i] = line

with open('/Users/nguyetpham/Desktop/WEBSITE/writing-essays-b1level/app.js', 'w') as f:
    f.writelines(lines)
