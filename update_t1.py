import re

with open("generate_b2_data.py", "r", encoding="utf-8") as f:
    content = f.read()

translations = {
    # Type 1 - Essay 1
    "In recent years, <strong>online education</strong> has become increasingly prevalent in modern society. Although it brings certain benefits, there are also some negative aspects. This essay will examine both the advantages and disadvantages.<br><br>":
    "Trong những năm gần đây, <strong>giáo dục trực tuyến</strong> ngày càng trở nên phổ biến trong xã hội hiện đại. Mặc dù nó mang lại những lợi ích nhất định, nhưng cũng có một số khía cạnh tiêu cực. Bài luận này sẽ xem xét cả những thuận lợi và bất lợi.<br><br>",

    "On the one hand, <strong>this form of education</strong> offers several advantages. One major benefit is that <strong>it provides a high level of convenience and flexibility</strong>. This is because learners can attend courses anytime and anywhere, as long as they have suitable devices and a stable Internet connection. As a result, they can organize their study schedules more effectively, especially those with busy lifestyles. Another positive effect is that <strong>e-learning helps save both time and money</strong>. Learners do not need to travel to school, which reduces transportation costs and other related expenses. Consequently, they can use the time saved for studying or personal activities, improving their overall time efficiency. A further aspect to consider is that <strong>distance learning allows learners to study at their own pace</strong>. They can pause, rewind, or review lessons multiple times, which helps them understand the content better. Therefore, they may feel less pressure compared to traditional classroom learning.<br><br>":
    "Một mặt, <strong>hình thức giáo dục này</strong> mang lại một số thuận lợi. Một lợi ích chính là <strong>nó cung cấp mức độ tiện lợi và linh hoạt cao</strong>. Điều này là do người học có thể tham gia các khóa học mọi lúc, mọi nơi, miễn là họ có thiết bị phù hợp và kết nối Internet ổn định. Kết quả là, họ có thể sắp xếp lịch học hiệu quả hơn, đặc biệt là những người có lối sống bận rộn. Một tác động tích cực khác là <strong>học trực tuyến giúp tiết kiệm cả thời gian và tiền bạc</strong>. Người học không cần phải di chuyển đến trường, điều này làm giảm chi phí đi lại và các chi phí liên quan khác. Do đó, họ có thể sử dụng thời gian tiết kiệm được cho việc học hoặc các hoạt động cá nhân, cải thiện hiệu quả thời gian tổng thể. Một khía cạnh khác cần xem xét là <strong>học từ xa cho phép người học học theo tốc độ của riêng mình</strong>. Họ có thể tạm dừng, tua lại hoặc xem lại bài học nhiều lần, điều này giúp họ hiểu nội dung tốt hơn. Vì vậy, họ có thể cảm thấy bớt áp lực hơn so với lớp học truyền thống.<br><br>",

    "On the other hand, there are some disadvantages that should be considered. One possible drawback is that <strong>this learning method can make learners easily distracted</strong>. Studying at home without supervision makes them easily distracted by social media, noise, or other activities. As a result, their concentration may decrease, which can negatively affect their learning performance. Another negative aspect is that <strong>direct interaction between learners and teachers is limited</strong>. Communication through screens reduces opportunities to have natural discussions and receive immediate feedback. Therefore, learners may find it difficult to fully understand lessons and feel less engaged. A further concern is that <strong>learning via digital platforms requires a high level of self-discipline</strong>. Due to the lack of direct supervision, learners may delay their study tasks or fail to maintain regular study habits. Consequently, they may not complete courses or achieve the desired results.<br><br>":
    "Mặt khác, có một số bất lợi cần được xem xét. Một nhược điểm có thể xảy ra là <strong>phương pháp học này có thể khiến người học dễ bị phân tâm</strong>. Học ở nhà mà không có sự giám sát khiến họ dễ bị phân tâm bởi mạng xã hội, tiếng ồn hoặc các hoạt động khác. Kết quả là, sự tập trung của họ có thể giảm sút, điều này có thể ảnh hưởng tiêu cực đến hiệu suất học tập. Một khía cạnh tiêu cực khác là <strong>sự tương tác trực tiếp giữa người học và giáo viên bị hạn chế</strong>. Việc giao tiếp qua màn hình làm giảm cơ hội có những cuộc thảo luận tự nhiên và nhận được phản hồi ngay lập tức. Vì vậy, người học có thể cảm thấy khó hiểu bài học một cách trọn vẹn và cảm thấy ít gắn kết hơn. Một mối lo ngại khác là <strong>học qua các nền tảng kỹ thuật số đòi hỏi mức độ kỷ luật tự giác cao</strong>. Do thiếu sự giám sát trực tiếp, người học có thể trì hoãn các nhiệm vụ học tập hoặc không duy trì được thói quen học tập đều đặn. Hậu quả là, họ có thể không hoàn thành các khóa học hoặc đạt được kết quả mong muốn.<br><br>",

    "In conclusion, <strong>online education</strong> presents both advantages and disadvantages. The points discussed above highlight its key aspects. Overall, understanding these factors helps provide a more balanced view of this topic.":
    "Tóm lại, <strong>giáo dục trực tuyến</strong> thể hiện cả những thuận lợi và bất lợi. Những điểm được thảo luận ở trên nêu bật các khía cạnh chính của nó. Nhìn chung, việc hiểu rõ những yếu tố này giúp mang lại cái nhìn cân bằng hơn về chủ đề này.",

    # Type 1 - Essay 2
    "In recent years, <strong>doing volunteer work</strong> has become increasingly prevalent in modern society. This has led to a range of benefits across different contexts. This essay will focus on the main advantages associated with it.<br><br>":
    "Trong những năm gần đây, <strong>làm công việc tình nguyện</strong> ngày càng trở nên phổ biến trong xã hội hiện đại. Điều này đã dẫn đến một loạt các lợi ích trong nhiều bối cảnh khác nhau. Bài luận này sẽ tập trung vào những lợi ích chính liên quan đến nó.<br><br>",

    "One major benefit is that <strong>participating in volunteer activities helps individuals develop valuable life skills</strong>. When engaging in community service, people often have to work in teams, communicate with different groups, and solve unexpected problems. This helps them improve teamwork, communication, and problem-solving skills. For example, a student volunteering at a local charity event can learn how to organize activities and interact with the public. These skills are highly beneficial for their future careers and personal development.<br><br>":
    "Một lợi ích chính là <strong>việc tham gia vào các hoạt động tình nguyện giúp cá nhân phát triển các kỹ năng sống có giá trị</strong>. Khi tham gia phục vụ cộng đồng, mọi người thường phải làm việc theo nhóm, giao tiếp với các nhóm khác nhau và giải quyết các vấn đề bất ngờ. Điều này giúp họ cải thiện kỹ năng làm việc nhóm, giao tiếp và giải quyết vấn đề. Ví dụ, một sinh viên làm tình nguyện viên tại một sự kiện từ thiện địa phương có thể học được cách tổ chức các hoạt động và tương tác với công chúng. Những kỹ năng này rất có lợi cho sự nghiệp tương lai và sự phát triển cá nhân của họ.<br><br>",

    "Another positive effect is that <strong>volunteering brings a sense of purpose and personal satisfaction</strong>. Helping others and contributing to the community allows individuals to feel that they are making a positive difference. This can increase their self-esteem and reduce stress or negative emotions. For instance, many young people who teach free classes for underprivileged children report feeling happier and more fulfilled. As a result, this promotes better mental health and overall well-being.<br><br>":
    "Một tác động tích cực khác là <strong>tình nguyện mang lại ý thức về mục đích và sự hài lòng cá nhân</strong>. Giúp đỡ người khác và đóng góp cho cộng đồng cho phép các cá nhân cảm thấy rằng họ đang tạo ra sự khác biệt tích cực. Điều này có thể nâng cao lòng tự trọng và giảm bớt căng thẳng hoặc những cảm xúc tiêu cực. Chẳng hạn, nhiều bạn trẻ dạy các lớp học miễn phí cho trẻ em nghèo cho biết họ cảm thấy hạnh phúc và trọn vẹn hơn. Nhờ đó, điều này thúc đẩy sức khỏe tinh thần và sức khỏe tổng thể tốt hơn.<br><br>",

    "A further aspect to consider is that <strong>volunteer work helps build a stronger and more supportive community</strong>. By volunteering, individuals help address social problems such as poverty, education inequality, and environmental issues. This creates a stronger connection among people from different backgrounds. For example, when residents work together to clean up their neighborhood, they not only improve the local environment but also build stronger community relationships. This ultimately leads to a safer and more united society.<br><br>":
    "Một khía cạnh khác cần xem xét là <strong>công việc tình nguyện giúp xây dựng một cộng đồng vững mạnh và gắn kết hơn</strong>. Bằng cách làm tình nguyện, các cá nhân giúp giải quyết các vấn đề xã hội như nghèo đói, bất bình đẳng giáo dục và các vấn đề môi trường. Điều này tạo ra sự kết nối mạnh mẽ hơn giữa những người có hoàn cảnh khác nhau. Ví dụ, khi cư dân cùng nhau dọn dẹp khu phố của họ, họ không chỉ cải thiện môi trường địa phương mà còn xây dựng các mối quan hệ cộng đồng bền chặt hơn. Điều này cuối cùng dẫn đến một xã hội an toàn và đoàn kết hơn.<br><br>",

    "In conclusion, <strong>doing volunteer work</strong> offers several notable advantages. These positive aspects highlight its value in various areas of life. Overall, examining these factors provides a clearer understanding of the topic.":
    "Tóm lại, <strong>làm công việc tình nguyện</strong> mang lại một số lợi ích đáng chú ý. Những khía cạnh tích cực này nêu bật giá trị của nó trong nhiều lĩnh vực khác nhau của cuộc sống. Nhìn chung, việc xem xét các yếu tố này cung cấp một sự hiểu biết rõ ràng hơn về chủ đề."
}

def inject_translation(text, paragraphs):
    # Find the block inside <div class="sample-letter-box">...</div> that matches all paragraphs
    # Instead of regex, we'll just locate the full string in the file.
    full_en = "".join(paragraphs)
    full_vn = "".join([translations[p] for p in paragraphs])
    
    if full_en in text:
        replacement = f"""{full_en}
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        {full_vn}"""
        # Note: the original text ends just before `</div>`. Wait, actually it does include </div> ? No.
        # My replacement assumes full_en is just before `</div>`.
        # Let's do a strict replace:
        text = text.replace(full_en + "\n                </div>", replacement)
    else:
        print("COULD NOT FIND:", repr(full_en[:100]))
    return text

# Essay 1
e1_paras = [
    "In recent years, <strong>online education</strong> has become increasingly prevalent in modern society. Although it brings certain benefits, there are also some negative aspects. This essay will examine both the advantages and disadvantages.<br><br>",
    "On the one hand, <strong>this form of education</strong> offers several advantages. One major benefit is that <strong>it provides a high level of convenience and flexibility</strong>. This is because learners can attend courses anytime and anywhere, as long as they have suitable devices and a stable Internet connection. As a result, they can organize their study schedules more effectively, especially those with busy lifestyles. Another positive effect is that <strong>e-learning helps save both time and money</strong>. Learners do not need to travel to school, which reduces transportation costs and other related expenses. Consequently, they can use the time saved for studying or personal activities, improving their overall time efficiency. A further aspect to consider is that <strong>distance learning allows learners to study at their own pace</strong>. They can pause, rewind, or review lessons multiple times, which helps them understand the content better. Therefore, they may feel less pressure compared to traditional classroom learning.<br><br>",
    "On the other hand, there are some disadvantages that should be considered. One possible drawback is that <strong>this learning method can make learners easily distracted</strong>. Studying at home without supervision makes them easily distracted by social media, noise, or other activities. As a result, their concentration may decrease, which can negatively affect their learning performance. Another negative aspect is that <strong>direct interaction between learners and teachers is limited</strong>. Communication through screens reduces opportunities to have natural discussions and receive immediate feedback. Therefore, learners may find it difficult to fully understand lessons and feel less engaged. A further concern is that <strong>learning via digital platforms requires a high level of self-discipline</strong>. Due to the lack of direct supervision, learners may delay their study tasks or fail to maintain regular study habits. Consequently, they may not complete courses or achieve the desired results.<br><br>",
    "In conclusion, <strong>online education</strong> presents both advantages and disadvantages. The points discussed above highlight its key aspects. Overall, understanding these factors helps provide a more balanced view of this topic."
]
content = inject_translation(content, e1_paras)

# Essay 2
e2_paras = [
    "In recent years, <strong>doing volunteer work</strong> has become increasingly prevalent in modern society. This has led to a range of benefits across different contexts. This essay will focus on the main advantages associated with it.<br><br>",
    "One major benefit is that <strong>participating in volunteer activities helps individuals develop valuable life skills</strong>. When engaging in community service, people often have to work in teams, communicate with different groups, and solve unexpected problems. This helps them improve teamwork, communication, and problem-solving skills. For example, a student volunteering at a local charity event can learn how to organize activities and interact with the public. These skills are highly beneficial for their future careers and personal development.<br><br>",
    "Another positive effect is that <strong>volunteering brings a sense of purpose and personal satisfaction</strong>. Helping others and contributing to the community allows individuals to feel that they are making a positive difference. This can increase their self-esteem and reduce stress or negative emotions. For instance, many young people who teach free classes for underprivileged children report feeling happier and more fulfilled. As a result, this promotes better mental health and overall well-being.<br><br>",
    "A further aspect to consider is that <strong>volunteer work helps build a stronger and more supportive community</strong>. By volunteering, individuals help address social problems such as poverty, education inequality, and environmental issues. This creates a stronger connection among people from different backgrounds. For example, when residents work together to clean up their neighborhood, they not only improve the local environment but also build stronger community relationships. This ultimately leads to a safer and more united society.<br><br>",
    "In conclusion, <strong>doing volunteer work</strong> offers several notable advantages. These positive aspects highlight its value in various areas of life. Overall, examining these factors provides a clearer understanding of the topic."
]
content = inject_translation(content, e2_paras)

with open("generate_b2_data.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Type 1")
