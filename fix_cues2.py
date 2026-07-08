with open('/Users/nguyetpham/Desktop/WEBSITE/writing-essays-b1level/app.js', 'r') as f:
    content = f.read()

# Fix Viết câu dẫn dắt chủ đề
content = content.replace('2. THÂN BÀI<br>Viết câu dẫn dắt chủ đề:', '1. MỞ BÀI<br>Viết câu dẫn dắt chủ đề:')
content = content.replace('2. THÂN BÀI<br>(DÀN Ý 4: Chỉ Nguyên Nhân) Viết câu dẫn dắt chủ đề:', '1. MỞ BÀI<br>(DÀN Ý 4: Chỉ Nguyên Nhân) Viết câu dẫn dắt chủ đề:')
content = content.replace('2. THÂN BÀI<br>(DÀN Ý 5: Chỉ Ảnh Hưởng) Viết câu dẫn dắt chủ đề:', '1. MỞ BÀI<br>(DÀN Ý 5: Chỉ Ảnh Hưởng) Viết câu dẫn dắt chủ đề:')
content = content.replace('2. THÂN BÀI<br>(DÀN Ý 6: Chỉ Giải Pháp) Viết câu dẫn dắt chủ đề:', '1. MỞ BÀI<br>(DÀN Ý 6: Chỉ Giải Pháp) Viết câu dẫn dắt chủ đề:')

# Fix other Mở Bài that got misclassified as Thân Bài
content = content.replace('2. THÂN BÀI<br>(DÀN Ý 4: Chỉ Nguyên Nhân) Viết câu khẳng định tầm quan trọng:', '1. MỞ BÀI<br>(DÀN Ý 4: Chỉ Nguyên Nhân) Viết câu khẳng định tầm quan trọng:')
content = content.replace('2. THÂN BÀI<br>(DÀN Ý 5: Chỉ Ảnh Hưởng) Viết câu khẳng định mức độ tác động:', '1. MỞ BÀI<br>(DÀN Ý 5: Chỉ Ảnh Hưởng) Viết câu khẳng định mức độ tác động:')
content = content.replace('2. THÂN BÀI<br>(DÀN Ý 6: Chỉ Giải Pháp) Viết câu nêu tính cấp thiết:', '1. MỞ BÀI<br>(DÀN Ý 6: Chỉ Giải Pháp) Viết câu nêu tính cấp thiết:')
content = content.replace('2. THÂN BÀI<br>Viết câu kết nối dẫn dắt vào Thân bài:', '1. MỞ BÀI<br>Viết câu kết nối dẫn dắt vào Thân bài:')

# Fix Kết Bài that got misclassified as Thân Bài
content = content.replace('2. THÂN BÀI<br>(DÀN Ý 6: Chỉ Giải Pháp) Viết câu dự báo kết quả:', '3. KẾT BÀI<br>(DÀN Ý 6: Chỉ Giải Pháp) Viết câu dự báo kết quả:')

with open('/Users/nguyetpham/Desktop/WEBSITE/writing-essays-b1level/app.js', 'w') as f:
    f.write(content)
