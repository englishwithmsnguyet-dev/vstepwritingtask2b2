# -*- coding: utf-8 -*-
import re

with open("generate_b2_data.py", "r", encoding="utf-8") as f:
    content = f.read()

translations = {
    # Type 3 - Essay 1 (Household chores)
    "In recent years, the idea that <strong>children, especially girls, no longer need to learn how to cook or do household chores</strong> has attracted considerable public attention and discussion.":
    """Trong những năm gần đây, ý kiến cho rằng <strong>trẻ em, đặc biệt là bé gái, không cần phải học cách nấu ăn hay làm việc nhà nữa</strong> đã thu hút sự chú ý và thảo luận đáng kể từ công chúng. Từ góc độ của tôi, tôi hoàn toàn <strong>không đồng tình</strong> với quan điểm này vì một số lý do quan trọng. Bài luận này sẽ trình bày những lập luận chính ủng hộ quan điểm của tôi.<br><br>
                    Đầu tiên, <strong>làm việc nhà là một kỹ năng sống thiết yếu giúp trẻ em trở nên tự lập</strong>. Khi trẻ học cách nấu ăn, dọn dẹp và quản lý nhà cửa, chúng phát triển khả năng tự chăm sóc bản thân trong tương lai. Thiếu đi những kỹ năng cơ bản này, chúng có thể gặp khó khăn khi sống một mình hoặc khi đi học xa nhà. Ví dụ, một sinh viên biết cách chuẩn bị bữa ăn sẽ không phải phụ thuộc vào đồ ăn nhanh đắt đỏ, điều này có lợi cho sức khỏe và ngân sách của họ. Do đó, việc dạy trẻ những kỹ năng này là cần thiết cho sự phát triển cá nhân của chúng.<br><br>
                    Hơn nữa, <strong>việc chia sẻ việc nhà dạy cho trẻ em tinh thần trách nhiệm và làm việc nhóm</strong>. Khi cả bé trai và bé gái tham gia vào việc dọn dẹp hoặc nấu nướng, chúng hiểu được giá trị của sự chăm chỉ và học cách trân trọng những nỗ lực của cha mẹ mình. Điều này cũng thúc đẩy bình đẳng giới, vì nó cho thấy các nghĩa vụ trong gia đình không phải là trách nhiệm duy nhất của phụ nữ. Ví dụ, trong những gia đình nơi con trai và con gái chia sẻ việc nhà một cách bình đẳng, trẻ em có xu hướng lớn lên với ý thức cao hơn về sự công bằng và sự tôn trọng đối với người khác. Do đó, làm việc nhà là một cách có giá trị để xây dựng tính cách mạnh mẽ và sự gắn kết gia đình.<br><br>
                    Tóm lại, tôi hoàn toàn <strong>không đồng ý</strong> với ý kiến cho rằng trẻ em không còn cần phải học cách nấu ăn hay làm việc nhà nữa. <strong>Những kỹ năng này rất quan trọng để nuôi dưỡng tính tự lập, dạy tinh thần trách nhiệm và thúc đẩy bình đẳng giới</strong>. Vì vậy, cha mẹ nên tiếp tục khuyến khích con cái của họ, bất kể giới tính nào, tham gia vào các nghĩa vụ gia đình vì lợi ích dài hạn của chúng.""",

    # Type 4 - Essay 1 (Picture books)
    "In recent years, <strong>the use of picture books for children</strong> has become a subject of considerable debate.":
    """Trong những năm gần đây, <strong>việc sử dụng sách tranh cho trẻ em</strong> đã trở thành một chủ đề gây nhiều tranh luận. Một số người tin rằng <strong>trẻ em nên đọc sách tranh vì chúng dễ hiểu và thú vị hơn</strong>, trong khi những người khác cho rằng <strong>những cuốn sách này có thể ảnh hưởng tiêu cực đến trí tưởng tượng của trẻ giống như việc xem tivi</strong>. <strong>Bài luận này sẽ thảo luận về cả hai quan điểm và trình bày góc nhìn cá nhân của tôi.</strong><br><br>
                    Một mặt, có những lập luận xác đáng để ủng hộ ý kiến cho rằng <strong>sách tranh có lợi cho trẻ em</strong>. Lý do chính là <strong>các hình minh họa làm cho việc đọc trở nên dễ tiếp cận và hấp dẫn hơn đối với những người học nhỏ tuổi</strong>. Trẻ em, đặc biệt là những trẻ chưa đọc trôi chảy, dựa vào hình ảnh để theo dõi câu chuyện và hiểu các ý tưởng phức tạp. Các công cụ hỗ trợ hình ảnh giúp trẻ nắm bắt bối cảnh và duy trì sự tập trung trong thời gian dài hơn. Ví dụ, một đứa trẻ đọc một cuốn sách về động vật có thể dễ dàng nhận biết các loài khác nhau thông qua các bức tranh đầy màu sắc, điều này làm cho quá trình học tập vừa thú vị vừa hiệu quả.<br><br>
                    Mặt khác, một số người cho rằng <strong>sách tranh có thể hạn chế các kỹ năng tưởng tượng của một đứa trẻ</strong>. Họ tin rằng <strong>khi tất cả các chi tiết hình ảnh được cung cấp, trẻ em không cần phải sử dụng sự sáng tạo của mình để hình dung ra các nhân vật hoặc bối cảnh</strong>. Điều này thường được so sánh với việc xem tivi, nơi người xem là những người tiếp nhận thông tin thụ động. Không cần phải hình dung câu chuyện trong tâm trí, trẻ em có thể bỏ lỡ cơ hội phát triển tư duy sáng tạo của mình, điều vốn rất quan trọng đối với sự phát triển nhận thức.<br><br>
                    Theo quan điểm của tôi, <strong>mặc dù sách tranh có thể hạn chế một số khía cạnh của trí tưởng tượng, nhưng những lợi ích của chúng vượt xa nhược điểm này</strong>. <strong>Hình ảnh là những công cụ cần thiết để giới thiệu trẻ em đến với thế giới của việc đọc trước khi chúng có thể xử lý các cuốn sách nhiều chữ.</strong> Khi chúng lớn lên và kỹ năng đọc của chúng được cải thiện, chúng có thể chuyển tự nhiên sang những cuốn sách không có tranh ảnh, điều này sau đó sẽ phát triển hơn nữa trí tưởng tượng của chúng.<br><br>
                    Tóm lại, mặc dù một số người lo lắng rằng sách tranh có thể ảnh hưởng tiêu cực đến sự sáng tạo giống như tivi, tôi tin rằng <strong>chúng đóng một vai trò tích cực và thiết yếu trong nền giáo dục sớm của trẻ</strong>. Cha mẹ nên sử dụng chúng như một bước đệm để giúp trẻ hình thành thói quen đọc sách suốt đời."""
}

pattern = re.compile(r'<div class="sample-letter-box">\s+(.*?)\s+</div>', re.DOTALL)

def replace_match(match):
    original_block = match.group(0)
    inner_html = match.group(1)
    
    for key, vn_text in translations.items():
        if key in inner_html:
            button_html = f'''
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        {vn_text}
                    </div>
                </div>'''
            return f"{original_block}{button_html}"
    
    return original_block

new_content = pattern.sub(replace_match, content)

with open("generate_b2_data.py", "w", encoding="utf-8") as f:
    f.write(new_content)
    
print("Updated T3 & T4 successfully")
