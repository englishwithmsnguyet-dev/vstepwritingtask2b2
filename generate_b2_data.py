# -*- coding: utf-8 -*-
import json

essayTypes = [
    {
        "id": "adv-disadv",
        "icon": "fa-scale-balanced",
        "titleEn": "ADVANTAGES AND DISADVANTAGES",
        "titleVi": "Thảo Luận Thuận Lợi & Bất Lợi",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích</h3>
                <p>Dạng bài Advantages and Disadvantages yêu cầu thí sinh <strong>phân tích một cách cân bằng các mặt tích cực và tiêu cực</strong> của một hiện tượng, hành vi hoặc xu hướng trong xã hội hiện đại. Trong một số biến thể, đề bài có thể chỉ tập trung vào một khía cạnh duy nhất, chẳng hạn như chỉ phân tích lợi ích hoặc chỉ phân tích hạn chế.</p>
            </div>
            <div class="content-block">
                <h3>Đặc điểm của dạng bài</h3>
                <p>Về bản chất, đây là dạng bài <strong>mang tính trung lập</strong>. Thí sinh không bị bắt buộc phải bày tỏ quan điểm cá nhân rõ ràng như trong OPINION ESSAY. Tuy nhiên, việc đưa ra một nhận định tổng quát hoặc đánh giá mang tính tổng kết ở phần kết luận được xem là phù hợp và giúp bài viết hoàn chỉnh hơn về mặt lập luận.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Dạng bài này thường được nhận diện thông qua các cấu trúc và cụm từ quen thuộc trong đề thi:</h3>
                <ul>
                    <li>What are the advantages and disadvantages of…?</li>
                    <li>Discuss the benefits and drawbacks of…</li>
                    <li>Discuss the benefits/advantages of….</li>
                    <li>Discuss the importance of …</li>
                    <li>Do the advantages outweigh the disadvantages?</li>
                    <li>What are the positive and negative aspects of …?</li>
                </ul>
                <p><em>Lưu ý: Việc xác định chính xác yêu cầu của đề (phân tích hai mặt hay chỉ một mặt, có yêu cầu so sánh mức độ hay không) là yếu tố then chốt để lựa chọn cấu trúc bài viết phù hợp.</em></p>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-variant">
                <h3 style="color: var(--primary-color); border-bottom: 2px solid var(--primary-light); padding-bottom: 10px; margin-bottom: 15px;">DÀN Ý 1: ĐỀ THUẬN LỢI VÀ BẤT LỢI</h3>
                <div class="outline-step">
                    <h4>1. MỞ BÀI</h4>
                    <p>↳ <span class="outline-phrase">In recent years, [chủ đề - danh từ / cụm danh từ] has become increasingly prevalent in modern society. Although it brings certain benefits, there are also some negative aspects. This essay will examine both the advantages and disadvantages.</span></p>
                </div>
                <div class="outline-step">
                    <h4>2. THÂN BÀI</h4>
                    <p><strong>THÂN BÀI 1: advantages – lợi ích</strong></p>
                    <p>↳ <span class="outline-phrase">On the one hand, [chủ đề - danh từ / cụm danh từ] offers several advantages.</span></p>
                    <ul>
                        <li><span class="outline-phrase">One major benefit is that [lợi ích 1].</span> → [luận cứ 1] → [luận cứ 2]</li>
                        <li><span class="outline-phrase">Another positive effect is that [lợi ích 2].</span> → [luận cứ 1] → [luận cứ 2]</li>
                        <li><span class="outline-phrase">A further aspect to consider is that [lợi ích 3].</span> → [luận cứ 1] → [luận cứ 2]</li>
                    </ul>
                    <p><strong>THÂN BÀI 2: disadvantages – bất lợi</strong></p>
                    <p>↳ <span class="outline-phrase">On the other hand, there are some disadvantages that should be considered.</span></p>
                    <ul>
                        <li><span class="outline-phrase">One possible drawback is that [bất lợi 1].</span> → [luận cứ 1] → [luận cứ 2]</li>
                        <li><span class="outline-phrase">Another negative aspect is that [bất lợi 2].</span> → [luận cứ 1] → [luận cứ 2]</li>
                        <li><span class="outline-phrase">A further concern is that [bất lợi 3].</span> → [luận cứ 1] → [luận cứ 2]</li>
                    </ul>
                </div>
                <div class="outline-step">
                    <h4>3. KẾT BÀI</h4>
                    <p>↳ <span class="outline-phrase">In conclusion, [chủ đề - danh từ / cụm danh từ] presents both advantages and disadvantages. The points discussed above highlight its key aspects. Overall, understanding these factors helps provide a more balanced view of this topic.</span></p>
                </div>
            </div>

            <div class="outline-variant" style="margin-top: 40px;">
                <h3 style="color: var(--primary-color); border-bottom: 2px solid var(--primary-light); padding-bottom: 10px; margin-bottom: 15px;">DÀN Ý 2: ĐỀ CHỈ THUẬN LỢI</h3>
                <div class="outline-step">
                    <h4>1. MỞ BÀI</h4>
                    <p>↳ <span class="outline-phrase">In recent years, [chủ đề - danh từ / cụm danh từ] has become increasingly prevalent in modern society. This has led to a range of benefits across different contexts. This essay will focus on the main advantages associated with it.</span></p>
                </div>
                <div class="outline-step">
                    <h4>2. THÂN BÀI</h4>
                    <ul>
                        <li><strong>THÂN BÀI 1:</strong> <span class="outline-phrase">One major benefit is that [lợi ích 1].</span> → [Luận cứ 1: giải thích] → [Luận cứ 2: hệ quả trực tiếp] → [Luận cứ 3: ví dụ] → [Luận cứ 4: mở rộng]</li>
                        <li><strong>THÂN BÀI 2:</strong> <span class="outline-phrase">Another positive effect is that [lợi ích 2].</span> → [Luận cứ 1: giải thích] → [Luận cứ 2: hệ quả trực tiếp] → [Luận cứ 3: ví dụ] → [Luận cứ 4: mở rộng]</li>
                        <li><strong>THÂN BÀI 3:</strong> <span class="outline-phrase">A further aspect to consider is that [lợi ích 3].</span> → [Luận cứ 1: giải thích] → [Luận cứ 2: hệ quả trực tiếp] → [Luận cứ 3: ví dụ] → [Luận cứ 4: mở rộng]</li>
                    </ul>
                </div>
                <div class="outline-step">
                    <h4>3. KẾT BÀI</h4>
                    <p>↳ <span class="outline-phrase">In conclusion, [chủ đề] offers several notable advantages. These positive aspects highlight its value in various areas of life. Overall, examining these factors provides a clearer understanding of the topic.</span></p>
                </div>
            </div>
        """,
        "sampleWriting": """
            <div class="content-block">
                <h3>ĐỀ BÀI 1: THUẬN LỢI & BẤT LỢI (TASK 02)</h3>
                <div class="prompt-box">
                    <p>Online learning is a great, revolutionary alternative to traditional training. Online learning is a form of distance learning that takes place over the Internet, including online courses, exams, gamified quizzes, and certification training. Some people believe that e-learning will replace traditional classes in the future.<br><br><strong>Write an essay to discuss the advantages and disadvantages of online learning.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>online education</strong> has become increasingly prevalent in modern society. Although it brings certain benefits, there are also some negative aspects. This essay will examine both the advantages and disadvantages.<br><br>
                    On the one hand, this form of education offers several advantages. One major benefit is that <strong>it provides a high level of convenience and flexibility</strong>. This is because learners can attend courses anytime and anywhere, as long as they have suitable devices and a stable Internet connection. As a result, they can organize their study schedules more effectively, especially those with busy lifestyles. Another positive effect is that <strong>e-learning helps save both time and money</strong>. Learners do not need to travel to school, which reduces transportation costs and other related expenses. Consequently, they can use the time saved for studying or personal activities, improving their overall time efficiency. A further aspect to consider is that <strong>distance learning allows learners to study at their own pace</strong>. They can pause, rewind, or review lessons multiple times, which helps them understand the content better. Therefore, they may feel less pressure compared to traditional classroom learning.<br><br>
                    On the other hand, there are some disadvantages that should be considered. One possible drawback is that <strong>this learning method can make learners easily distracted</strong>. Studying at home without supervision makes them easily distracted by social media, noise, or other activities. As a result, their concentration may decrease, which can negatively affect their learning performance. Another negative aspect is that <strong>direct interaction between learners and teachers is limited</strong>. Communication through screens reduces opportunities to have natural discussions and receive immediate feedback. Therefore, learners may find it difficult to fully understand lessons and feel less engaged. A further concern is that <strong>learning via digital platforms requires a high level of self-discipline</strong>. Due to the lack of direct supervision, learners may delay their study tasks or fail to maintain regular study habits. Consequently, they may not complete courses or achieve the desired results.<br><br>
                    In conclusion, <strong>online education</strong> presents both advantages and disadvantages. The points discussed above highlight its key aspects. Overall, understanding these factors helps provide a more balanced view of this topic.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>giáo dục trực tuyến</strong> ngày càng trở nên phổ biến trong xã hội hiện đại. Mặc dù nó mang lại những lợi ích nhất định, nhưng cũng có một số khía cạnh tiêu cực. Bài luận này sẽ xem xét cả những thuận lợi và bất lợi.<br><br>
                    Một mặt, <strong>hình thức giáo dục này</strong> mang lại một số thuận lợi. Một lợi ích chính là <strong>nó cung cấp mức độ tiện lợi và linh hoạt cao</strong>. Điều này là do người học có thể tham gia các khóa học mọi lúc, mọi nơi, miễn là họ có thiết bị phù hợp và kết nối Internet ổn định. Kết quả là, họ có thể sắp xếp lịch học hiệu quả hơn, đặc biệt là những người có lối sống bận rộn. Một tác động tích cực khác là <strong>học trực tuyến giúp tiết kiệm cả thời gian và tiền bạc</strong>. Người học không cần phải di chuyển đến trường, điều này làm giảm chi phí đi lại và các chi phí liên quan khác. Do đó, họ có thể sử dụng thời gian tiết kiệm được cho việc học hoặc các hoạt động cá nhân, cải thiện hiệu quả thời gian tổng thể. Một khía cạnh khác cần xem xét là <strong>học từ xa cho phép người học học theo tốc độ của riêng mình</strong>. Họ có thể tạm dừng, tua lại hoặc xem lại bài học nhiều lần, điều này giúp họ hiểu nội dung tốt hơn. Vì vậy, họ có thể cảm thấy bớt áp lực hơn so với lớp học truyền thống.<br><br>
                    Mặt khác, có một số bất lợi cần được xem xét. Một nhược điểm có thể xảy ra là <strong>phương pháp học này có thể khiến người học dễ bị phân tâm</strong>. Học ở nhà mà không có sự giám sát khiến họ dễ bị phân tâm bởi mạng xã hội, tiếng ồn hoặc các hoạt động khác. Kết quả là, sự tập trung của họ có thể giảm sút, điều này có thể ảnh hưởng tiêu cực đến hiệu suất học tập. Một khía cạnh tiêu cực khác là <strong>sự tương tác trực tiếp giữa người học và giáo viên bị hạn chế</strong>. Việc giao tiếp qua màn hình làm giảm cơ hội có những cuộc thảo luận tự nhiên và nhận được phản hồi ngay lập tức. Vì vậy, người học có thể cảm thấy khó hiểu bài học một cách trọn vẹn và cảm thấy ít gắn kết hơn. Một mối lo ngại khác là <strong>học qua các nền tảng kỹ thuật số đòi hỏi mức độ kỷ luật tự giác cao</strong>. Do thiếu sự giám sát trực tiếp, người học có thể trì hoãn các nhiệm vụ học tập hoặc không duy trì được thói quen học tập đều đặn. Hậu quả là, họ có thể không hoàn thành các khóa học hoặc đạt được kết quả mong muốn.<br><br>
                    Tóm lại, <strong>giáo dục trực tuyến</strong> thể hiện cả những thuận lợi và bất lợi. Những điểm được thảo luận ở trên nêu bật các khía cạnh chính của nó. Nhìn chung, việc hiểu rõ những yếu tố này giúp mang lại cái nhìn cân bằng hơn về chủ đề này.
                    </div>
                </div>

                <h3 style="margin-top: 40px;">ĐỀ BÀI 2: CHỈ THUẬN LỢI (TASK 02)</h3>
                <div class="prompt-box">
                    <p>Volunteer work is becoming increasingly popular among students and young adults. Participating in volunteer activities is believed to bring various benefits to individuals and the community.<br><br><strong>Write an essay to discuss the benefits of doing volunteer work.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>volunteer work</strong> has become increasingly prevalent in modern society. This has led to a range of benefits across different contexts. This essay will focus on the main advantages associated with it.<br><br>
                    One major benefit is that <strong>participating in volunteer activities helps young people develop essential personal skills</strong>. This is because participants often have to communicate, work in teams, and deal with real-life situations while helping others. As a result, they can improve soft skills such as communication, time management, and problem-solving. For example, when organizing a community event, volunteers need to collaborate with many people and handle different tasks. These skills are not only useful in academic settings but also offer advantages in future workplaces.<br><br>
                    Another positive effect is that <strong>volunteering allows the young to expand social relationships</strong>. This happens because participants have opportunities to meet and work with people from different backgrounds and fields. Therefore, they can build valuable personal and professional relationships for the future. For instance, students who take part in volunteer programs can connect with new friends or even potential employers. In the long run, these relationships can support them in finding educational and career opportunities.<br><br>
                    A further aspect to consider is that <strong>voluntary activities positively contribute to the community</strong>. This can be explained by the fact that volunteer activities often focus on helping disadvantaged people or improving living conditions in society. Consequently, the quality of life of many individuals can be improved, and social problems can be reduced. For example, charity gift-giving programs and free teaching activities can support people in need. This contributes to building a more equal and humane society.<br><br>
                    In conclusion, <strong>volunteer work</strong> offers several notable advantages. These positive aspects highlight its value in various areas of life. Overall, examining these factors provides a clearer understanding of the topic.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>làm công việc tình nguyện</strong> ngày càng trở nên phổ biến trong xã hội hiện đại. Điều này đã dẫn đến một loạt các lợi ích trong nhiều bối cảnh khác nhau. Bài luận này sẽ tập trung vào những lợi ích chính liên quan đến nó.<br><br>
                    Một lợi ích chính là <strong>việc tham gia vào các hoạt động tình nguyện giúp cá nhân phát triển các kỹ năng sống có giá trị</strong>. Khi tham gia phục vụ cộng đồng, mọi người thường phải làm việc theo nhóm, giao tiếp với các nhóm khác nhau và giải quyết các vấn đề bất ngờ. Điều này giúp họ cải thiện kỹ năng làm việc nhóm, giao tiếp và giải quyết vấn đề. Ví dụ, một sinh viên làm tình nguyện viên tại một sự kiện từ thiện địa phương có thể học được cách tổ chức các hoạt động và tương tác với công chúng. Những kỹ năng này rất có lợi cho sự nghiệp tương lai và sự phát triển cá nhân của họ.<br><br>
                    Một tác động tích cực khác là <strong>tình nguyện mang lại ý thức về mục đích và sự hài lòng cá nhân</strong>. Giúp đỡ người khác và đóng góp cho cộng đồng cho phép các cá nhân cảm thấy rằng họ đang tạo ra sự khác biệt tích cực. Điều này có thể nâng cao lòng tự trọng và giảm bớt căng thẳng hoặc những cảm xúc tiêu cực. Chẳng hạn, nhiều bạn trẻ dạy các lớp học miễn phí cho trẻ em nghèo cho biết họ cảm thấy hạnh phúc và trọn vẹn hơn. Nhờ đó, điều này thúc đẩy sức khỏe tinh thần và sức khỏe tổng thể tốt hơn.<br><br>
                    Một khía cạnh khác cần xem xét là <strong>công việc tình nguyện giúp xây dựng một cộng đồng vững mạnh và gắn kết hơn</strong>. Bằng cách làm tình nguyện, các cá nhân giúp giải quyết các vấn đề xã hội như nghèo đói, bất bình đẳng giáo dục và các vấn đề môi trường. Điều này tạo ra sự kết nối mạnh mẽ hơn giữa những người có hoàn cảnh khác nhau. Ví dụ, khi cư dân cùng nhau dọn dẹp khu phố của họ, họ không chỉ cải thiện môi trường địa phương mà còn xây dựng các mối quan hệ cộng đồng bền chặt hơn. Điều này cuối cùng dẫn đến một xã hội an toàn và đoàn kết hơn.<br><br>
                    Tóm lại, <strong>làm công việc tình nguyện</strong> mang lại một số lợi ích đáng chú ý. Những khía cạnh tích cực này nêu bật giá trị của nó trong nhiều lĩnh vực khác nhau của cuộc sống. Nhìn chung, việc xem xét các yếu tố này cung cấp một sự hiểu biết rõ ràng hơn về chủ đề.
                    </div>
                </div>
            </div>
        """
    },
    {
        "id": "cause-effect",
        "icon": "fa-link",
        "titleEn": "CAUSES – EFFECTS – SOLUTIONS",
        "titleVi": "Nguyên Nhân, Hậu Quả & Giải Pháp",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích</h3>
                <p>Dạng bài Causes – Effects – Solutions yêu cầu thí sinh phân tích một vấn đề xã hội bằng cách xác định <strong>nguyên nhân, hậu quả, giải pháp</strong> liên quan đến vấn đề đó.</p>
            </div>
            <div class="content-block">
                <h3>Đặc điểm của dạng bài</h3>
                <p>Về bản chất, đây là dạng bài <strong>mang tính phân tích và giải thích</strong>. Thí sinh không cần thể hiện quan điểm cá nhân mạnh mẽ như trong Opinion Essay. Thay vào đó, bài viết cần thể hiện khả năng <strong>giải thích mối quan hệ giữa vấn đề – nguyên nhân – hậu quả – giải pháp</strong> một cách logic và rõ ràng.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Dạng đề có thể xuất hiện dưới nhiều biến thể, bao gồm:</h3>
                <ul>
                    <li><strong>Yêu cầu phân tích nguyên nhân và hậu quả:</strong> What are the causes and effects of this problem? / What factors lead to this issue and what are its consequences?</li>
                    <li><strong>Yêu cầu phân tích nguyên nhân và giải pháp:</strong> What are the causes of this issue and how can it be solved? / Why is this happening and what can be done to tackle it?</li>
                    <li><strong>Yêu cầu phân tích hậu quả và giải pháp:</strong> What problems does this issue cause and what are the possible solutions? / What are the effects and how can we deal with them?</li>
                    <li><strong>Yêu cầu phân tích một yếu tố duy nhất:</strong> What are the main reasons/causes for this trend? / What are the impacts/negative effects of this issue on society? / What should be done to solve this problem?</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-variant">
                <h3 style="color: var(--primary-color); border-bottom: 2px solid var(--primary-light); padding-bottom: 10px; margin-bottom: 15px;">DÀN Ý CƠ BẢN TỔNG HỢP (6 BIẾN THỂ)</h3>
                
                <div class="outline-step">
                    <h4>1. MỞ BÀI (Ví dụ: ĐỀ NGUYÊN NHÂN VÀ GIẢI PHÁP)</h4>
                    <p>↳ <span class="outline-phrase">In recent years, [chủ đề] has become a growing concern in many parts of the world. This issue has created several challenges for both individuals and society. This essay will examine the main causes of this problem and suggest possible solutions.</span></p>
                </div>
                <div class="outline-step">
                    <h4>2. THÂN BÀI</h4>
                    <p><strong>CÁCH VIẾT ĐOẠN NGUYÊN NHÂN (Causes)</strong></p>
                    <p>↳ <span class="outline-phrase">This issue can be attributed to several key factors.</span> One major cause is that [nguyên nhân 1] → [luận cứ 1] → [luận cứ 2]. Another contributing factor is that [nguyên nhân 2] → [luận cứ 1] → [luận cứ 2]. A further reason is that [nguyên nhân 3] → [luận cứ 1] → [luận cứ 2].</p>
                    <p><strong>CÁCH VIẾT ĐOẠN ẢNH HƯỞNG (Effects)</strong></p>
                    <p>↳ <span class="outline-phrase">This problem can lead to several significant consequences.</span> One negative effect is that [ảnh hưởng 1] → [luận cứ 1] → [luận cứ 2]. Another serious impact is that [ảnh hưởng 2] → [luận cứ 1] → [luận cứ 2]. A further consequence is that [ảnh hưởng 3] → [luận cứ 1] → [luận cứ 2].</p>
                    <p><strong>CÁCH VIẾT ĐOẠN GIẢI PHÁP (Solutions)</strong></p>
                    <p>↳ <span class="outline-phrase">To address this problem, several practical solutions can be implemented.</span> One effective solution is to [giải pháp 1] → [luận cứ 1] → [luận cứ 2]. Another possible measure is to [giải pháp 2] → [luận cứ 1] → [luận cứ 2]. Finally, it is necessary to [giải pháp 3] → [luận cứ 1] → [luận cứ 2].</p>
                </div>
                <div class="outline-step">
                    <h4>3. KẾT BÀI (Ví dụ: ĐỀ NGUYÊN NHÂN VÀ GIẢI PHÁP)</h4>
                    <p>↳ <span class="outline-phrase">In conclusion, [chủ đề] is caused by several factors and requires practical solutions to address it effectively. Addressing these causes is essential to improve the situation in the future. With appropriate measures, this issue can be reduced, leading to positive changes in society.</span></p>
                </div>
            </div>
        """,
        "sampleWriting": """
            <div class="content-block">
                <h3>ĐỀ BÀI 1: NGUYÊN NHÂN & GIẢI PHÁP (TASK 02)</h3>
                <div class="prompt-box">
                    <p>Obesity is a serious global problem in today's society, especially among young people. More than one-third of adults and 17% of youth in the United States are obese, although the prevalence remained stable between 2003-2004 and 2009-2010. Obesity causes a lot of conditions, including heart disease, stroke, type 2 diabetes, and certain types of cancer, some of the leading causes of preventable death.<br><br><strong>Write an essay to discuss the causes of obesity among young people and suggest possible solutions.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>obesity among young people</strong> has become a growing concern in many parts of the world. This issue has created several challenges for both individuals and society. This essay will examine the main causes of this problem and suggest possible solutions.<br><br>
                    This issue can be attributed to several key factors. One major cause is that <strong>young people tend to consume unhealthy food regularly</strong>. Many young individuals frequently eat fast food, processed meals, and sugary drinks, which are high in calories but low in nutritional value. Over time, this habit leads to excessive energy intake and fat accumulation in the body. Another contributing factor is that <strong>many young people often have a sedentary lifestyle</strong>. They spend a significant amount of time using smartphones, computers, and engaging in passive forms of entertainment. This reduces the number of calories burned, which contributes to weight gain. A further reason is that <strong>the youth lack sufficient knowledge about nutrition</strong>. Many individuals are unaware of what constitutes a balanced diet or how to make healthy food choices. As a result, they develop poor eating habits without fully understanding the long-term consequences.<br><br>
                    To address this problem, several practical solutions can be implemented. One effective solution is to <strong>encourage young people to adopt a healthy and well-balanced diet</strong>. This can be achieved by limiting the consumption of fast food and sugary drinks through awareness-raising campaigns. As a result, young people can lower their excessive calorie intake and improve their overall health. Another possible measure is to <strong>promote regular participation in physical activities among the youth</strong>. Schools should organize more sports activities and encourage students to exercise regularly. This helps burn excess energy and maintain a healthy body weight. Finally, it is necessary to <strong>enhance young people's understanding of proper nutrition</strong>. Schools can integrate nutrition education into the formal curriculum to provide essential knowledge. As a result, learners are more likely to make healthier food choices in their daily lives.<br><br>
                    In conclusion, <strong>obesity among young people</strong> is primarily driven by the consumption of unhealthy food, a sedentary lifestyle, and a lack of nutritional knowledge. However, by implementing targeted measures such as encouraging young people to adopt a healthy diet, promoting regular participation in physical activities, and enhancing nutritional awareness, this issue can be effectively addressed. These actions can help improve the situation in the long term.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>tình trạng béo phì ở giới trẻ</strong> đã trở thành một mối lo ngại ngày càng tăng ở nhiều nơi trên thế giới. Vấn đề này đã tạo ra một số thách thức cho cả cá nhân và xã hội. Bài luận này sẽ xem xét những nguyên nhân chính của vấn đề này và đề xuất các giải pháp khả thi.<br><br>
                    Vấn đề này có thể bắt nguồn từ một số yếu tố chính. Một nguyên nhân chính là <strong>người trẻ có xu hướng tiêu thụ thực phẩm không lành mạnh thường xuyên</strong>. Nhiều cá nhân trẻ thường xuyên ăn thức ăn nhanh, bữa ăn chế biến sẵn và đồ uống có đường, những thứ chứa nhiều calo nhưng ít giá trị dinh dưỡng. Theo thời gian, thói quen này dẫn đến việc nạp quá nhiều năng lượng và tích tụ mỡ trong cơ thể. Một yếu tố góp phần khác là <strong>nhiều người trẻ thường có lối sống ít vận động</strong>. Họ dành một lượng thời gian đáng kể để sử dụng điện thoại thông minh, máy tính và tham gia vào các hình thức giải trí thụ động. Điều này làm giảm lượng calo được đốt cháy, góp phần gây tăng cân. Một lý do khác là <strong>giới trẻ thiếu kiến thức đầy đủ về dinh dưỡng</strong>. Nhiều người trong số họ không biết cách cân bằng chế độ ăn uống hoặc phân biệt giữa thực phẩm lành mạnh và không lành mạnh. Do đó, họ đưa ra những lựa chọn thực phẩm tồi tệ, làm tăng nguy cơ béo phì.<br><br>
                    Để giải quyết vấn đề này, một số giải pháp thiết thực có thể được thực hiện. Một giải pháp hiệu quả là <strong>khuyến khích giới trẻ duy trì một chế độ ăn uống lành mạnh và cân bằng</strong>. Cha mẹ và nhà trường nên cung cấp những bữa ăn bổ dưỡng với nhiều rau xanh và ít đồ ăn nhanh hơn. Điều này giúp giới trẻ kiểm soát lượng calo nạp vào và cải thiện sức khỏe thể chất của họ. Một biện pháp khả thi khác là <strong>thúc đẩy các hoạt động thể chất thường xuyên trong giới trẻ</strong>. Các trường học và cộng đồng nên tổ chức nhiều sự kiện thể thao hơn và khuyến khích các cá nhân trẻ tập thể dục hàng ngày. Kết quả là, họ có thể đốt cháy nhiều calo hơn và duy trì cân nặng khỏe mạnh. Cuối cùng, điều cần thiết là <strong>giáo dục giới trẻ về tầm quan trọng của dinh dưỡng</strong>. Các chương trình giáo dục nên được đưa ra để giúp họ hiểu lợi ích của những thói quen ăn uống lành mạnh. Về lâu dài, điều này có thể giúp họ đưa ra những lựa chọn thực phẩm tốt hơn và ngăn ngừa béo phì.<br><br>
                    Tóm lại, <strong>tình trạng béo phì ở giới trẻ</strong> được gây ra bởi một số yếu tố và đòi hỏi các giải pháp thiết thực để giải quyết nó một cách hiệu quả. Việc giải quyết các nguyên nhân này là điều cần thiết để cải thiện tình hình trong tương lai. Với các biện pháp phù hợp, vấn đề này có thể được giảm thiểu, dẫn đến những thay đổi tích cực trong xã hội.
                    </div>
                </div>

                <h3 style="margin-top: 40px;">ĐỀ BÀI 2: NGUYÊN NHÂN & ẢNH HƯỞNG (TASK 02)</h3>
                <div class="prompt-box">
                    <p>In many countries, the number of single-parent families has been rising steadily in recent decades. This trend has raised concerns about its possible causes and effects on individuals and society.<br><br><strong>Write an essay to discuss the causes of this trend and its effects.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>the increasing number of single-parent families</strong> has become a growing concern in many parts of the world. This issue has created several challenges for both individuals and society. This essay will examine the main causes of this problem and discuss its possible effects.<br><br>
                    This issue can be attributed to several key factors. One major cause is that <strong>many couples nowadays choose to get divorced</strong>, which contributes to the increasing number of single-parent families. In modern society, couples often face difficulties in maintaining long-term relationships due to work pressure, financial problems, and differences in lifestyle. When marriages break down, children often live with only one parent, which leads to single-parent households. Another contributing factor is that <strong>the death of one parent due to illness or accidents</strong> can result in single-parent families. In some cases, serious diseases or unexpected accidents may leave one parent responsible for raising children alone. This causes the remaining parent to take on full responsibility for both financial support and childcare. A further reason is that <strong>unplanned pregnancies are becoming increasingly common</strong>, especially among young people. A number of young people lack proper knowledge about reproductive health and contraception, which may result in unplanned decisions about having children. In many cases, children are born to parents who do not have a stable relationship, meaning that child-rearing responsibilities are often taken on by only one parent.<br><br>
                    This problem can lead to several significant consequences. One negative effect is that <strong>single parents often face significant pressure in terms of both finances and time</strong>. There is only one person earning an income while also having to pay for all living expenses and raise children. In addition, they have to balance work and childcare responsibilities, which can lead to exhaustion and leave them with little time to rest. Another serious impact is that <strong>children in single-parent families may lack full support and guidance from both parents</strong>. With only one parent, children may not receive enough care and guidance. This can negatively affect their emotional, cognitive, and behavioral development in the long term. A further consequence is that <strong>the increasing number of single-parent families can create long-term challenges for society</strong>. Financial and educational difficulties in these families may lead to greater inequality in society. Moreover, this may place a greater burden on social welfare and education systems in the future.<br><br>
                    In conclusion, <strong>the increasing number of single-parent families</strong> is mainly caused by the rising divorce rate, the death of one parent, and unplanned pregnancies. It leads to several negative effects on both individuals and society, including financial and time pressure, a lack of parental support and guidance, and long-term social challenges. By addressing these underlying factors, this issue can be effectively reduced, improving the situation in the long term.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>số lượng ngày càng tăng của các gia đình cha/mẹ đơn thân</strong> đã trở thành một mối lo ngại ngày càng lớn ở nhiều nơi trên thế giới. Vấn đề này đã tạo ra một số thách thức cho cả cá nhân và xã hội. Bài luận này sẽ xem xét các nguyên nhân chính của vấn đề này và thảo luận về các tác động có thể có của nó.<br><br>
                    Vấn đề này có thể bắt nguồn từ một số yếu tố chính. Một nguyên nhân chính là <strong>nhiều cặp vợ chồng hiện nay chọn ly hôn</strong>, điều này góp phần làm gia tăng số lượng các gia đình đơn thân. Trong xã hội hiện đại, các cặp đôi thường gặp khó khăn trong việc duy trì các mối quan hệ lâu dài do áp lực công việc, vấn đề tài chính và sự khác biệt về lối sống. Khi hôn nhân tan vỡ, trẻ em thường sống với chỉ một phụ huynh, điều này dẫn đến các hộ gia đình đơn thân. Một yếu tố góp phần khác là <strong>sự qua đời của một phụ huynh do bệnh tật hoặc tai nạn</strong> có thể dẫn đến các gia đình đơn thân. Trong một số trường hợp, các căn bệnh nghiêm trọng hoặc tai nạn bất ngờ có thể khiến một phụ huynh phải chịu trách nhiệm một mình nuôi nấng con cái. Sự mất mát bất ngờ này tạo ra một tình huống đầy thách thức cho người cha/mẹ còn lại để xoay sở cả công việc và nhiệm vụ gia đình. Một lý do nữa là <strong>một số cá nhân cố ý chọn nuôi con độc lập mà không kết hôn</strong>. Do sự thay đổi trong thái độ của xã hội, nhiều người không còn coi kết hôn là điều kiện cần thiết để xây dựng gia đình. Hậu quả là, họ quyết định trở thành cha/mẹ đơn thân theo sự lựa chọn, điều này làm tăng thêm xu hướng đang gia tăng này.<br><br>
                    Vấn đề này có thể dẫn đến một số hệ quả đáng kể. Một tác động tiêu cực là <strong>các cha/mẹ đơn thân thường trải qua những khó khăn tài chính nghiêm trọng</strong>. Nuôi một đứa trẻ một mình có nghĩa là một người phải trang trải mọi chi phí sinh hoạt, bao gồm nhà ở, thức ăn và giáo dục. Điều này có thể gây ra áp lực tài chính đáng kể, đặc biệt là đối với những người có thu nhập thấp. Một tác động nghiêm trọng khác là <strong>trẻ em trong các gia đình đơn thân có thể phải đối mặt với các thách thức về tâm lý và cảm xúc</strong>. Sự vắng bóng của người cha hoặc mẹ có thể khiến trẻ cảm thấy cô đơn hoặc bất an so với bạn bè đồng trang lứa. Một hệ quả nữa là <strong>các cha/mẹ đơn thân thường bị kiệt sức và thiếu thời gian cá nhân</strong>. Việc cân bằng giữa công việc toàn thời gian và chăm sóc con cái khiến họ gần như không có thời gian để nghỉ ngơi hoặc tham gia các hoạt động xã hội. Theo thời gian, điều này có thể dẫn đến mức độ căng thẳng cao và ảnh hưởng tiêu cực đến sức khỏe thể chất và tinh thần của họ.<br><br>
                    Tóm lại, <strong>số lượng ngày càng tăng của các gia đình cha/mẹ đơn thân</strong> được gây ra bởi một số yếu tố và dẫn đến một loạt các tác động tiêu cực đối với cá nhân và xã hội. Việc giải quyết những nguyên nhân cơ bản này là điều cần thiết để cải thiện tình hình trong tương lai. Với sự quan tâm nhiều hơn, vấn đề này có thể được quản lý tốt hơn theo thời gian.
                    </div>
                </div>

                <h3 style="margin-top: 40px;">ĐỀ BÀI 3: ẢNH HƯỞNG & GIẢI PHÁP (TASK 02)</h3>
                <div class="prompt-box">
                    <p>In recent years, the rapid growth of technology has led to a significant increase in cybercrime. This trend is causing growing concern globally about its impacts on both individuals and organizations.<br><br><strong>Write an essay to discuss the effects of cybercrime and suggest possible solutions.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>cybercrime</strong> has become a growing concern in many parts of the world. This issue has created several challenges for both individuals and society. This essay will examine the main effects of this problem and suggest possible solutions.<br><br>
                    This issue can lead to several significant consequences. One negative effect is that <strong>cybercrime can cause serious financial losses for both individuals and organizations</strong>. Activities such as online scams, stealing banking information, or hacking accounts can cause users to lose a large amount of money. For businesses, cyber attacks can disrupt operations and result in significant revenue losses. Another serious impact is that <strong>online crime can seriously violate personal privacy and personal data</strong>. Hackers can gain unauthorized access to personal information such as accounts, passwords, or sensitive data. This may lead to the misuse of information for illegal purposes such as fraud or identity theft. A further consequence is that <strong>digital crime can have negative psychological effects and reduce people’s trust in technology</strong>. Victims of cyber attacks may feel anxious, stressed, and unsafe when using the Internet. In addition, this can reduce their trust in online platforms and limit their use of technology.<br><br>
                    To address this problem, several practical solutions can be implemented. One effective solution is to <strong>strengthen security measures and cybersecurity systems</strong>. Governments and businesses should invest in advanced security technologies to prevent cyber attacks. This helps protect user data and minimize the risk of unauthorized access. Another possible measure is to <strong>raise users’ awareness of online safety</strong>. Users need to be educated about online risks and how to protect their personal information. As a result, they can avoid scams and reduce the risk of becoming victims of cybercrime. Finally, it is necessary to <strong>implement stricter regulations and strengthen law enforcement</strong>. Governments should introduce stricter laws and apply appropriate penalties to cybercriminals. This can help deter illegal activities and create a safer online environment.<br><br>
                    In conclusion, <strong>cybercrime</strong> results in several negative consequences for both individuals and society, including financial losses, the violation of privacy and personal data, and psychological impact and loss of trust. However, by implementing targeted measures such as strengthening security measures and cybersecurity systems, raising users’ awareness of online safety, and implementing stricter regulations and strengthening law enforcement, this issue can be effectively addressed. Ultimately, these concerted efforts will help improve the situation in the long term.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>tội phạm mạng</strong> đã trở thành một mối lo ngại ngày càng tăng ở nhiều nơi trên thế giới. Vấn đề này đã tạo ra một số thách thức cho cả cá nhân và xã hội. Bài luận này sẽ xem xét những tác động chính của vấn đề này và đề xuất các giải pháp khả thi.<br><br>
                    Vấn đề này có thể dẫn đến một số hệ quả đáng kể. Một tác động tiêu cực là <strong>tội phạm mạng có thể gây ra tổn thất tài chính nghiêm trọng cho cả cá nhân và tổ chức</strong>. Các hoạt động như lừa đảo trực tuyến, đánh cắp thông tin ngân hàng hoặc hack tài khoản có thể khiến người dùng mất một số tiền lớn. Đối với các doanh nghiệp, các cuộc tấn công mạng có thể làm gián đoạn hoạt động và dẫn đến tổn thất doanh thu đáng kể. Một tác động nghiêm trọng khác là <strong>tội phạm trực tuyến có thể xâm phạm nghiêm trọng quyền riêng tư cá nhân và dữ liệu cá nhân</strong>. Tin tặc có thể truy cập trái phép vào thông tin cá nhân như tài khoản, mật khẩu hoặc dữ liệu nhạy cảm. Điều này có thể dẫn đến việc lạm dụng thông tin cho các mục đích bất hợp pháp như lừa đảo hoặc đánh cắp danh tính. Một hệ quả nữa là <strong>các loại tội phạm kỹ thuật số có thể ảnh hưởng tiêu cực đến tâm lý của mọi người và gây ra sự mất niềm tin vào môi trường trực tuyến</strong>. Các nạn nhân của tội phạm mạng thường trải qua lo âu, sợ hãi hoặc căng thẳng sau khi bị tấn công. Về lâu dài, điều này khiến người dùng ngần ngại sử dụng các dịch vụ kỹ thuật số hoặc tham gia vào các hoạt động trực tuyến.<br><br>
                    Để giải quyết vấn đề này, một số giải pháp thiết thực có thể được thực hiện. Một giải pháp hiệu quả là <strong>tăng cường các biện pháp bảo mật và hệ thống an ninh mạng</strong>. Các chính phủ và doanh nghiệp nên đầu tư vào các công nghệ bảo mật tiên tiến để ngăn chặn các cuộc tấn công mạng. Điều này giúp bảo vệ dữ liệu người dùng và giảm thiểu rủi ro truy cập trái phép. Một biện pháp khả thi khác là <strong>nâng cao nhận thức của người dùng về an toàn trực tuyến</strong>. Người dùng cần được giáo dục về các rủi ro trực tuyến và cách bảo vệ thông tin cá nhân của họ. Kết quả là, họ có thể tránh bị lừa đảo và giảm nguy cơ trở thành nạn nhân của tội phạm mạng. Cuối cùng, điều cần thiết là <strong>thực thi các quy định nghiêm ngặt hơn và tăng cường thực thi pháp luật</strong>. Các chính phủ nên đưa ra các đạo luật khắt khe hơn và áp dụng các hình phạt thích đáng cho tội phạm mạng. Điều này có thể giúp răn đe các hoạt động phi pháp và tạo ra một môi trường trực tuyến an toàn hơn.<br><br>
                    Tóm lại, <strong>tội phạm mạng</strong> dẫn đến một số hệ quả tiêu cực cho cả cá nhân và xã hội, bao gồm tổn thất tài chính, sự vi phạm quyền riêng tư và dữ liệu cá nhân, cùng tác động tâm lý và sự mất niềm tin. Tuy nhiên, bằng cách thực hiện các biện pháp có mục tiêu như tăng cường các biện pháp an ninh và hệ thống an ninh mạng, nâng cao nhận thức của người dùng về an toàn trực tuyến, và thực thi các quy định khắt khe hơn cùng tăng cường thực thi pháp luật, vấn đề này có thể được giải quyết một cách hiệu quả. Cuối cùng, những nỗ lực phối hợp này sẽ giúp cải thiện tình hình trong dài hạn.
                    </div>
                </div>

                <h3 style="margin-top: 40px;">ĐỀ BÀI 4: CHỈ NGUYÊN NHÂN (TASK 02)</h3>
                <div class="prompt-box">
                    <p>In recent years, a growing number of young people have chosen to leave traditional jobs in companies to start their own businesses. This trend has attracted attention from the public and sparked discussion about what is driving this change.<br><br><strong>Write an essay to discuss the causes of this trend.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>a growing number of young people have chosen to leave traditional jobs in companies to start their own businesses</strong>. This trend has attracted attention from the public and sparked discussion about what is driving this change. This essay will examine the main causes of this trend.<br><br>
                    One major cause is that <strong>many young people want to have more freedom and control over their work</strong>. They do not want to work in highly restrictive environments with fixed schedules and strict regulations. Starting their own businesses allows them to make their own decisions and manage their work in their preferred way. For example, many young individuals nowadays choose to run online businesses or manage small personal brands. This helps them feel more creative and motivated to develop their careers in the long term.<br><br>
                    Another contributing factor is that <strong>many young people believe that starting a business can provide better income and financial opportunities</strong>. Salaries in many traditional jobs are often limited and increase slowly over time. In contrast, running a personal business can generate significant profits if the business is successful. For instance, many young entrepreneurs have earned high incomes through online selling or providing digital services. This makes entrepreneurship an attractive career choice for many young people.<br><br>
                    A further reason is that <strong>the development of technology and social media has made it easier for young people to start businesses</strong>. Online platforms allow young people to advertise products and reach customers at a relatively low cost. As a result, they can start businesses without requiring too much capital or experience. For example, many young people now use TikTok, Facebook, or Instagram to sell products and build their brands. In the long term, this has contributed to the growing trend of entrepreneurship among modern youth.<br><br>
                    In conclusion, <strong>this trend</strong> is mainly caused by the desire for freedom and independence at work, opportunities to earn higher incomes, and the development of technology and social media. These factors have a considerable impact on the career choices of young people today. Therefore, understanding these causes is essential to gain a clearer view of this growing trend in the long term.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>ngày càng có nhiều người trẻ lựa chọn rời bỏ các công việc truyền thống ở các công ty để bắt đầu công việc kinh doanh của riêng mình</strong>. Xu hướng này đã thu hút sự chú ý của dư luận và làm dấy lên những cuộc thảo luận về điều gì đang thúc đẩy sự thay đổi này. Bài tiểu luận này sẽ xem xét các nguyên nhân chính của xu hướng này.<br><br>
                    Một nguyên nhân chính là <strong>nhiều người trẻ muốn có nhiều tự do và kiểm soát hơn đối với công việc của họ</strong>. Họ không muốn làm việc trong những môi trường bị hạn chế với lịch trình cố định và các quy định nghiêm ngặt. Việc bắt đầu hoạt động kinh doanh riêng cho phép họ tự đưa ra quyết định và quản lý công việc theo cách ưa thích của họ. Ví dụ, nhiều cá nhân trẻ ngày nay lựa chọn kinh doanh trực tuyến hoặc quản lý các thương hiệu cá nhân nhỏ. Điều này giúp họ cảm thấy sáng tạo hơn và có động lực hơn để phát triển sự nghiệp trong dài hạn.<br><br>
                    Một yếu tố đóng góp khác là <strong>nhiều người trẻ tin rằng khởi nghiệp có thể mang lại cơ hội tài chính và thu nhập tốt hơn</strong>. Mức lương ở nhiều công việc truyền thống thường bị giới hạn và tăng chậm theo thời gian. Ngược lại, điều hành một doanh nghiệp cá nhân có thể tạo ra lợi nhuận đáng kể nếu doanh nghiệp thành công. Ví dụ, nhiều doanh nhân trẻ đã kiếm được thu nhập cao thông qua việc bán hàng trực tuyến hoặc cung cấp các dịch vụ kỹ thuật số. Điều này khiến khởi nghiệp trở thành một lựa chọn nghề nghiệp hấp dẫn đối với nhiều người trẻ.<br><br>
                    Một lý do nữa là <strong>sự phát triển của công nghệ và mạng xã hội đã giúp những người trẻ tuổi khởi nghiệp dễ dàng hơn</strong>. Các nền tảng trực tuyến cho phép giới trẻ quảng cáo sản phẩm và tiếp cận khách hàng với chi phí tương đối thấp. Kết quả là, họ có thể bắt đầu kinh doanh mà không cần quá nhiều vốn hoặc kinh nghiệm. Ví dụ, nhiều người trẻ hiện nay sử dụng TikTok, Facebook hoặc Instagram để bán sản phẩm và xây dựng thương hiệu của họ. Về lâu dài, điều này đã góp phần làm tăng xu hướng khởi nghiệp trong giới trẻ hiện đại.<br><br>
                    Tóm lại, <strong>xu hướng này</strong> chủ yếu là do mong muốn tự do và độc lập trong công việc, cơ hội kiếm thu nhập cao hơn, và sự phát triển của công nghệ cùng với mạng xã hội. Những yếu tố này có tác động đáng kể đến sự lựa chọn nghề nghiệp của giới trẻ hiện nay. Do đó, việc hiểu những nguyên nhân này là điều cần thiết để có cái nhìn rõ ràng hơn về xu hướng đang gia tăng này trong tương lai dài hạn.
                    </div>
                </div>

                <h3 style="margin-top: 40px;">ĐỀ BÀI 5: CHỈ ẢNH HƯỞNG (TASK 02)</h3>
                <div class="prompt-box">
                    <p>Deforestation has become a serious environmental issue in many parts of the world. As large areas of forest are being cut down every year, this practice is causing significant damage to the environment and human life.<br><br><strong>Write an essay to discuss the effects of deforestation.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>deforestation</strong> has become a growing concern in many parts of the world. This issue has created several challenges for both individuals and society. This essay will examine the main effects of this problem.<br><br>
                    One major effect is that <strong>deforestation causes serious damage to the natural environment and biodiversity</strong>. Forests are the natural habitats of many animal and plant species, so cutting down forests destroys their living environments. This can cause many species to decline in population or face the risk of extinction. For example, many tropical forests are currently losing rare animal species because of large-scale deforestation. In the long term, this can cause ecological imbalance and disrupt natural food chains.<br><br>
                    Another serious impact is that <strong>deforestation contributes to more serious climate change and natural disasters</strong>. Trees absorb carbon dioxide, so the loss of forests increases the amount of greenhouse gases in the atmosphere. This leads to global warming, floods, and soil erosion. For example, many deforested areas often face more serious flash floods and landslides. If this situation continues, extreme weather events may occur more frequently in the future.<br><br>
                    A further consequence is that <strong>forest destruction can cause many negative effects on people’s lives and livelihoods</strong>. Many local communities depend on forests for natural resources, agricultural production, and sources of income. When forests are destroyed, natural resources and environmental conditions decline, negatively affecting people’s living conditions and economic activities. For example, people in areas affected by deforestation may face water shortages, less fertile land, or reduced agricultural productivity. In the long term, this can increase poverty, unemployment, and other social problems in affected communities.<br><br>
                    In conclusion, <strong>deforestation</strong> results in several significant effects, including environmental damage and biodiversity loss, climate change and natural disasters, and negative effects on people’s lives and livelihoods. These impacts have considerable implications for both individuals and society. Therefore, addressing these effects is essential to improve the situation in the long term.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>nạn phá rừng</strong> đã trở thành một mối lo ngại ngày càng gia tăng ở nhiều nơi trên thế giới. Vấn đề này đã tạo ra một số thách thức cho cả cá nhân và xã hội. Bài tiểu luận này sẽ xem xét những tác động chính của vấn đề này.<br><br>
                    Một tác động lớn là <strong>nạn phá rừng gây ra thiệt hại nghiêm trọng cho môi trường tự nhiên và đa dạng sinh học</strong>. Rừng là môi trường sống tự nhiên của nhiều loài động thực vật, vì vậy việc chặt phá rừng sẽ phá hủy môi trường sống của chúng. Điều này có thể khiến nhiều loài bị suy giảm dân số hoặc đối mặt với nguy cơ tuyệt chủng. Ví dụ, nhiều khu rừng nhiệt đới hiện đang mất đi các loài động vật quý hiếm vì nạn phá rừng trên quy mô lớn. Về lâu dài, điều này có thể gây mất cân bằng sinh thái và phá vỡ chuỗi thức ăn tự nhiên.<br><br>
                    Một tác động nghiêm trọng khác là <strong>nạn phá rừng góp phần làm trầm trọng thêm biến đổi khí hậu và thiên tai</strong>. Cây cối hấp thụ lượng khí thải carbon dioxide, vì vậy sự mất đi của các khu rừng làm tăng lượng khí nhà kính trong bầu khí quyển. Điều này dẫn đến sự nóng lên toàn cầu, lũ lụt và xói mòn đất. Ví dụ, nhiều khu vực bị phá rừng thường phải đối mặt với lũ quét và lở đất nghiêm trọng hơn. Nếu tình trạng này tiếp tục, các hiện tượng thời tiết khắc nghiệt có thể xảy ra thường xuyên hơn trong tương lai.<br><br>
                    Một hệ quả nữa là <strong>sự tàn phá rừng có thể gây ra nhiều tác động tiêu cực đến đời sống và sinh kế của con người</strong>. Nhiều cộng đồng địa phương phụ thuộc vào rừng cho các nguồn tài nguyên tự nhiên, sản xuất nông nghiệp và nguồn thu nhập. Khi rừng bị phá hủy, tài nguyên thiên nhiên và điều kiện môi trường suy giảm, ảnh hưởng tiêu cực đến điều kiện sống và các hoạt động kinh tế của con người. Ví dụ, người dân ở các khu vực bị ảnh hưởng bởi nạn phá rừng có thể đối mặt với tình trạng thiếu nước, đất đai kém màu mỡ hơn, hoặc năng suất nông nghiệp giảm sút. Về lâu dài, điều này có thể làm tăng sự nghèo đói, thất nghiệp và các vấn đề xã hội khác trong các cộng đồng bị ảnh hưởng.<br><br>
                    Tóm lại, <strong>nạn phá rừng</strong> dẫn đến một số tác động đáng kể, bao gồm thiệt hại về môi trường và mất đa dạng sinh học, biến đổi khí hậu và thiên tai, cùng với những tác động tiêu cực đến cuộc sống và sinh kế của con người. Những tác động này có ý nghĩa to lớn đối với cả cá nhân và xã hội. Do đó, việc giải quyết những tác động này là điều thiết yếu để cải thiện tình hình trong dài hạn.
                    </div>
                </div>

                <h3 style="margin-top: 40px;">ĐỀ BÀI 6: CHỈ GIẢI PHÁP (TASK 02)</h3>
                <div class="prompt-box">
                    <p>In today’s globalized world, language education plays a key role in helping people communicate, work, and study across borders. However, in many countries, language learning is still limited or ineffective.<br><br><strong>Write an essay to suggest measures that can be taken to promote language education.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>foreign language education</strong> has become increasingly important in many parts of the world. It has had a profound impact on both individuals and society. This essay will suggest several practical measures to effectively support such efforts.<br><br>
                    One effective step is to <strong>improve foreign language teaching methods</strong>. Schools should apply more modern and interactive teaching methods instead of focusing only on grammar and theory. This helps learners develop practical communication skills and become more interested in learning foreign languages. For example, teachers can organize group discussions, role-play activities, or language games in the classroom. In the long term, these methods can improve the quality of language education and students’ ability to use foreign languages.<br><br>
                    Another possible measure is to <strong>increase access to high-quality language learning resources</strong>. Governments and educational institutions should invest in online learning platforms, digital libraries, and language learning applications. This allows learners to access learning materials more easily anytime and anywhere at an affordable cost. For instance, students can use language learning apps or participate in free online courses. As a result, more people can improve their language skills even if they live in areas with limited educational opportunities.<br><br>
                    A further approach is to <strong>create more opportunities for learners to practice foreign languages regularly</strong>. Schools and educational organizations should establish language clubs and international exchange programs. This helps learners become more confident and improve their real-life communication skills. For example, students can take part in language exchange sessions with foreigners or communication activities in English. In the long term, this can create a positive learning environment and encourage the use of foreign languages in the community.<br><br>
                    In conclusion, <strong>this objective can be effectively achieved</strong> by implementing measures such as improving foreign language teaching methods, increasing access to high-quality language learning resources, and creating more opportunities for learners to practice foreign languages regularly. These approaches can bring significant benefits to both individuals and society. Therefore, taking such actions is essential to secure long-term improvement.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>giáo dục ngoại ngữ</strong> ngày càng trở nên quan trọng ở nhiều nơi trên thế giới. Nó đã có tác động sâu sắc đến cả cá nhân và xã hội. Bài luận này sẽ đề xuất một số biện pháp thiết thực để hỗ trợ hiệu quả những nỗ lực như vậy.<br><br>
                    Một bước hiệu quả là <strong>cải thiện các phương pháp giảng dạy ngoại ngữ</strong>. Các trường học nên áp dụng các phương pháp giảng dạy hiện đại và mang tính tương tác cao hơn thay vì chỉ tập trung vào ngữ pháp và lý thuyết. Điều này giúp người học phát triển các kỹ năng giao tiếp thực tế và trở nên hứng thú hơn với việc học ngoại ngữ. Ví dụ, giáo viên có thể tổ chức các buổi thảo luận nhóm, các hoạt động đóng vai, hoặc các trò chơi ngôn ngữ trong lớp học. Về lâu dài, những phương pháp này có thể cải thiện chất lượng giáo dục ngôn ngữ và khả năng sử dụng ngoại ngữ của học sinh.<br><br>
                    Một biện pháp khả thi khác là <strong>tăng cường khả năng tiếp cận các nguồn tài nguyên học ngôn ngữ chất lượng cao</strong>. Các chính phủ và cơ sở giáo dục nên đầu tư vào các nền tảng học tập trực tuyến, thư viện kỹ thuật số và các ứng dụng học ngôn ngữ. Điều này cho phép người học tiếp cận các tài liệu học tập một cách dễ dàng hơn ở mọi lúc, mọi nơi với mức chi phí hợp lý. Ví dụ, sinh viên có thể sử dụng các ứng dụng học ngoại ngữ hoặc tham gia các khóa học trực tuyến miễn phí. Kết quả là, nhiều người hơn có thể cải thiện các kỹ năng ngôn ngữ của họ ngay cả khi họ sống ở các khu vực có cơ hội giáo dục hạn chế.<br><br>
                    Một hướng tiếp cận nữa là <strong>tạo ra nhiều cơ hội hơn cho người học để thực hành ngoại ngữ thường xuyên</strong>. Các trường học và tổ chức giáo dục nên thành lập các câu lạc bộ ngôn ngữ và các chương trình giao lưu quốc tế. Điều này giúp người học trở nên tự tin hơn và cải thiện các kỹ năng giao tiếp ngoài đời thực của họ. Ví dụ, học sinh có thể tham gia vào các buổi trao đổi ngôn ngữ với người nước ngoài hoặc các hoạt động giao tiếp bằng tiếng Anh. Về lâu dài, điều này có thể tạo ra một môi trường học tập tích cực và khuyến khích việc sử dụng ngoại ngữ trong cộng đồng.<br><br>
                    Tóm lại, <strong>mục tiêu này có thể đạt được một cách hiệu quả</strong> bằng cách thực hiện các biện pháp như cải thiện phương pháp giảng dạy ngoại ngữ, tăng cường tiếp cận các nguồn tài nguyên học ngôn ngữ chất lượng cao, và tạo ra nhiều cơ hội hơn cho người học để thực hành ngoại ngữ thường xuyên. Những cách tiếp cận này có thể mang lại những lợi ích to lớn cho cả cá nhân và xã hội. Vì vậy, việc thực hiện những hành động như vậy là điều cần thiết để đảm bảo sự cải thiện trong dài hạn.
                    </div>
                </div>
            </div>
        """
    },
    {
        "id": "opinion",
        "icon": "fa-comment-dots",
        "titleEn": "OPINION",
        "titleVi": "Trình Bày Quan Điểm",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích</h3>
                <p><strong>Trình bày quan điểm cá nhân</strong> về một vấn đề xã hội và <strong>bảo vệ quan điểm đó bằng các lập luận thuyết phục</strong>.</p>
            </div>
            <div class="content-block">
                <h3>Đặc điểm của dạng bài</h3>
                <p>Thí sinh cần lựa chọn một lập trường rõ ràng như <strong>hoàn toàn đồng ý</strong> hoặc <strong>hoàn toàn không đồng ý</strong>. OPINION ESSAY không yêu cầu người viết giữ quan điểm trung lập. Bài viết cần có <strong>hệ thống lập luận mạch lạc, logic và nhất quán xuyên suốt</strong>.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Một số dạng câu hỏi phổ biến:</h3>
                <ul>
                    <li>Do you agree or disagree with this opinion?</li>
                    <li>To what extent do you agree or disagree?</li>
                    <li>Do you agree that...?</li>
                    <li>What is your opinion about this?</li>
                    <li>What do you think about this?</li>
                    <li>Do you support or oppose this view? Why?</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-step">
                <h4>1. MỞ BÀI</h4>
                <p>↳ <span class="outline-phrase">In recent years, the idea that [quan điểm trong đề bài – mệnh đề] has attracted considerable public attention and discussion. From my perspective, I completely agree / disagree with this opinion for several important reasons. This essay will present the main arguments supporting my viewpoint.</span></p>
            </div>
            <div class="outline-step">
                <h4>2. THÂN BÀI</h4>
                <p><strong>THÂN BÀI 1</strong></p>
                <p>↳ <span class="outline-phrase">The first reason why I agree / disagree with this opinion is that [lý do 1 – mệnh đề].</span> → Giải thích và phát triển lý do bằng các lập luận, ví dụ hoặc dẫn chứng phù hợp (khoảng 4–6 câu).</p>
                <p><strong>THÂN BÀI 2</strong></p>
                <p>↳ <span class="outline-phrase">Another important reason is that [lý do 2 – mệnh đề].</span> → Tiếp tục phân tích và mở rộng ý bằng giải thích hoặc ví dụ cụ thể (khoảng 4–6 câu).</p>
                <p><strong>THÂN BÀI 3</strong></p>
                <p>↳ <span class="outline-phrase">A further reason supporting my viewpoint is that [lý do 3 – mệnh đề].</span> → Phát triển lý do cuối cùng và nhấn mạnh tác động hoặc ý nghĩa của vấn đề (khoảng 4–6 câu).</p>
            </div>
            <div class="outline-step">
                <h4>3. KẾT BÀI</h4>
                <p>↳ <span class="outline-phrase">In conclusion, I strongly agree / disagree with the idea that [quan điểm trong đề bài – mệnh đề]. The arguments presented above clearly explain why I support / oppose this viewpoint. Therefore, I believe that this perspective should be carefully considered in modern society.</span></p>
            </div>
        """,
        "sampleWriting": """
            <div class="content-block">
                <h3>ĐỀ BÀI (TASK 02)</h3>
                <div class="prompt-box">
                    <p>In today’s modern society, many families can afford to hire domestic helpers or rely on convenient services for meals and housework. As a result, some people believe that children, especially girls, no longer need to learn how to cook or do household chores.<br><br><strong>To what extent do you agree or disagree with this opinion?</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, the idea that <strong>children, especially girls, no longer need to learn how to cook or do household chores</strong> has attracted considerable public attention and discussion. From my perspective, I completely <strong>disagree</strong> with this opinion for several important reasons. This essay will present the main arguments supporting my viewpoint.<br><br>
                    The first reason why I <strong>disagree</strong> with this opinion is that <strong>learning household chores helps children develop important life skills</strong>. Cooking, cleaning, and organizing personal belongings are essential abilities that people need in daily life. If children are not taught these skills from an early age, they may become too dependent on others in the future. In addition, doing household tasks can allow young people to become more independent and better prepared for adult life. In fact, many young adults who live away from their families often struggle with daily activities because they lack basic household skills.<br><br>
                    Another important reason is that <strong>household chores can strengthen family relationships and encourage children to become more responsible</strong>. When children help their parents with cooking or cleaning, they learn to share responsibilities within the family. This can create a stronger sense of cooperation and mutual understanding among family members. Moreover, participating in household tasks allows children to appreciate their parents’ hard work more deeply. For instance, teenagers who regularly contribute to housework often develop closer bonds with their parents and communicate more effectively at home.<br><br>
                    A further reason supporting my viewpoint is that <strong>both boys and girls should learn household chores to promote gender equality</strong>. In modern society, household responsibilities should not be considered the duty of women alone. Teaching both genders to cook and clean helps eliminate traditional stereotypes about the roles of men and women in the family. Furthermore, these skills are useful for everyone regardless of their future career or lifestyle. In the long term, this can contribute to building more equal and balanced relationships within families and society.<br><br>
                    In conclusion, I strongly <strong>disagree</strong> with the idea that <strong>household chores are no longer necessary for children in modern society</strong>. The arguments presented above clearly explain why I oppose this viewpoint. Therefore, I believe that this perspective should be carefully considered in modern society.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, ý kiến cho rằng <strong>trẻ em, đặc biệt là bé gái, không cần phải học cách nấu ăn hay làm việc nhà nữa</strong> đã thu hút sự chú ý và thảo luận đáng kể từ công chúng. Từ góc độ của tôi, tôi hoàn toàn <strong>không đồng tình</strong> với quan điểm này vì một số lý do quan trọng. Bài luận này sẽ trình bày những lập luận chính ủng hộ quan điểm của tôi.<br><br>
                    Đầu tiên, <strong>làm việc nhà là một kỹ năng sống thiết yếu giúp trẻ em trở nên tự lập</strong>. Khi trẻ học cách nấu ăn, dọn dẹp và quản lý nhà cửa, chúng phát triển khả năng tự chăm sóc bản thân trong tương lai. Thiếu đi những kỹ năng cơ bản này, chúng có thể gặp khó khăn khi sống một mình hoặc khi đi học xa nhà. Ví dụ, một sinh viên biết cách chuẩn bị bữa ăn sẽ không phải phụ thuộc vào đồ ăn nhanh đắt đỏ, điều này có lợi cho sức khỏe và ngân sách của họ. Do đó, việc dạy trẻ những kỹ năng này là cần thiết cho sự phát triển cá nhân của chúng.<br><br>
                    Hơn nữa, <strong>việc chia sẻ việc nhà dạy cho trẻ em tinh thần trách nhiệm và làm việc nhóm</strong>. Khi cả bé trai và bé gái tham gia vào việc dọn dẹp hoặc nấu nướng, chúng hiểu được giá trị của sự chăm chỉ và học cách trân trọng những nỗ lực của cha mẹ mình. Điều này cũng thúc đẩy bình đẳng giới, vì nó cho thấy các nghĩa vụ trong gia đình không phải là trách nhiệm duy nhất của phụ nữ. Ví dụ, trong những gia đình nơi con trai và con gái chia sẻ việc nhà một cách bình đẳng, trẻ em có xu hướng lớn lên với ý thức cao hơn về sự công bằng và sự tôn trọng đối với người khác. Do đó, làm việc nhà là một cách có giá trị để xây dựng tính cách mạnh mẽ và sự gắn kết gia đình.<br><br>
                    Tóm lại, tôi hoàn toàn <strong>không đồng ý</strong> với ý kiến cho rằng trẻ em không còn cần phải học cách nấu ăn hay làm việc nhà nữa. <strong>Những kỹ năng này rất quan trọng để nuôi dưỡng tính tự lập, dạy tinh thần trách nhiệm và thúc đẩy bình đẳng giới</strong>. Vì vậy, cha mẹ nên tiếp tục khuyến khích con cái của họ, bất kể giới tính nào, tham gia vào các nghĩa vụ gia đình vì lợi ích dài hạn của chúng.
                    </div>
                </div>
            </div>
        """
    },
    {
        "id": "discussion",
        "icon": "fa-users-viewfinder",
        "titleEn": "DISCUSSION",
        "titleVi": "Thảo Luận 2 Chiều",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích</h3>
                <p>Phân tích một vấn đề dưới <strong>góc nhìn của hai quan điểm hoặc hai lập trường trái chiều</strong>, sau đó nêu rõ quan điểm cá nhân nếu đề bài có yêu cầu, hoặc tổng hợp và đánh giá hai phía một cách khách quan nếu đề không yêu cầu ý kiến riêng.</p>
            </div>
            <div class="content-block">
                <h3>Đặc điểm của dạng bài</h3>
                <p>Người viết cần <strong>trình bày lập luận cho cả hai phía một cách tương đối cân bằng và hợp lý</strong>. Khi phân tích hai quan điểm đối lập, người viết nên giữ văn phong khách quan và <strong>hạn chế thiên vị quá mức cho một phía</strong>. Ý kiến cá nhân (nếu có) nên được thể hiện rõ ràng và hợp lý.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các cấu trúc thể hiện hai quan điểm hoặc hai lập trường trái chiều:</h3>
                <ul>
                    <li>Discuss both views and give your opinion.</li>
                    <li>Discuss both sides and state your own view.</li>
                    <li>Some people believe that... while others think that...</li>
                    <li>There are different views about…</li>
                    <li>While some think that…, others feel that…</li>
                    <li>Some people argue that… while others believe that…</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-step">
                <h4>1. MỞ BÀI</h4>
                <p>↳ <span class="outline-phrase">In recent years, [chủ đề] has become a subject of considerable debate. Some people believe that [ý kiến 1 – mệnh đề], while others argue that [ý kiến 2 – mệnh đề]. This essay will discuss both perspectives and present my personal viewpoint.</span></p>
            </div>
            <div class="outline-step">
                <h4>2. THÂN BÀI</h4>
                <p><strong>THÂN BÀI 1: Phân tích ý kiến 1</strong></p>
                <p>↳ <span class="outline-phrase">On the one hand, it is argued that [ý kiến 1 – mệnh đề].</span></p>
                <p>→ Phân tích và phát triển quan điểm bằng giải thích, ví dụ hoặc dẫn chứng phù hợp (khoảng 6–8 câu).</p>
                <p><strong>THÂN BÀI 2: Phân tích ý kiến 2</strong></p>
                <p>↳ <span class="outline-phrase">On the other hand, it is believed that [ý kiến 2 – mệnh đề].</span></p>
                <p>→ Phân tích quan điểm đối lập bằng các lập luận và ví dụ phù hợp (khoảng 6–8 câu).</p>
            </div>
            <div class="outline-step">
                <h4>3. KẾT BÀI</h4>
                <p>↳ <span class="outline-phrase">In conclusion, both sides of the argument present valid points. However, I personally believe that [quan điểm cá nhân – mệnh đề] because [lý do ngắn gọn – mệnh đề]. Therefore, people should carefully consider both perspectives before forming a final opinion.</span></p>
            </div>
        """,
        "sampleWriting": """
            <div class="content-block">
                <h3>ĐỀ BÀI (TASK 02)</h3>
                <div class="prompt-box">
                    <p>Some people believe that children should read picture books because they are easier to understand and more enjoyable. However, others argue that picture books may negatively affect children's imagination, just like watching television.<br><br><strong>Discuss both views and give your own opinion.</strong> Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar.</p>
                </div>
                <h3 style="margin-top: 25px;">BÀI VIẾT MẪU (SAMPLE ESSAY - B2 LEVEL)</h3>
                <div class="sample-letter-box">
                    In recent years, <strong>the use of picture books for children</strong> has become a subject of considerable debate. Some people believe that <strong>children should read picture books because they are easier to understand and more enjoyable</strong>, while others argue that <strong>these books may negatively affect children’s imagination in a similar way to television</strong>. <strong>This essay will discuss both perspectives and present my personal viewpoint.</strong><br><br>
                    On the one hand, it is argued that <strong>picture books bring many benefits to children’s learning and reading habits</strong>. First of all, colorful illustrations can help young readers understand stories more easily, especially when their vocabulary is still limited. This visual support allows children to follow the plot, recognize characters, and connect new words with specific situations. As a result, reading becomes less difficult and more enjoyable for young learners. In addition, picture books can encourage children to develop a regular reading habit from an early age. For example, many primary school teachers use picture books in class to make reading lessons more engaging and interactive. Therefore, many people believe that picture books are useful tools for supporting children’s early language development.<br><br>
                    On the other hand, many people believe that <strong>picture books may have negative effects on children’s imagination and thinking ability</strong>. Since the images are already provided, children may not need to imagine the characters, settings, or events by themselves. This can reduce their ability to visualize ideas and create mental images while reading. As a result, they may become too dependent on visual support instead of developing their own imagination. Moreover, if children are exposed to illustrated materials too often, they may find text-based books more difficult and less attractive. For instance, some children may lose interest in longer stories without pictures because these books require more concentration and imagination. Therefore, many people are concerned that excessive use of picture books may limit children’s creativity and independent thinking.<br><br>
                    In conclusion, both sides of the argument present valid points. However, I personally believe that <strong>picture books are beneficial for children</strong> because <strong>they help young readers develop reading habits and improve language skills</strong>. Therefore, people should carefully consider both perspectives before forming a final opinion.
                </div>
                <button class="translation-toggle-btn" onclick="toggleTranslation(this)">
                    <i class="fa-solid fa-language"></i> Xem bản dịch tiếng Việt
                </button>
                <div class="translation-content" style="display: none;">
                    <div class="sample-letter-box">
                        Trong những năm gần đây, <strong>việc sử dụng sách tranh cho trẻ em</strong> đã trở thành một chủ đề gây nhiều tranh luận. Một số người tin rằng <strong>trẻ em nên đọc sách tranh vì chúng dễ hiểu và thú vị hơn</strong>, trong khi những người khác cho rằng <strong>những cuốn sách này có thể ảnh hưởng tiêu cực đến trí tưởng tượng của trẻ giống như việc xem tivi</strong>. <strong>Bài luận này sẽ thảo luận về cả hai quan điểm và trình bày góc nhìn cá nhân của tôi.</strong><br><br>
                    Một mặt, có những lập luận xác đáng để ủng hộ ý kiến cho rằng <strong>sách tranh có lợi cho trẻ em</strong>. Lý do chính là <strong>các hình minh họa làm cho việc đọc trở nên dễ tiếp cận và hấp dẫn hơn đối với những người học nhỏ tuổi</strong>. Trẻ em, đặc biệt là những trẻ chưa đọc trôi chảy, dựa vào hình ảnh để theo dõi câu chuyện và hiểu các ý tưởng phức tạp. Các công cụ hỗ trợ hình ảnh giúp trẻ nắm bắt bối cảnh và duy trì sự tập trung trong thời gian dài hơn. Ví dụ, một đứa trẻ đọc một cuốn sách về động vật có thể dễ dàng nhận biết các loài khác nhau thông qua các bức tranh đầy màu sắc, điều này làm cho quá trình học tập vừa thú vị vừa hiệu quả.<br><br>
                    Mặt khác, một số người cho rằng <strong>sách tranh có thể hạn chế các kỹ năng tưởng tượng của một đứa trẻ</strong>. Họ tin rằng <strong>khi tất cả các chi tiết hình ảnh được cung cấp, trẻ em không cần phải sử dụng sự sáng tạo của mình để hình dung ra các nhân vật hoặc bối cảnh</strong>. Điều này thường được so sánh với việc xem tivi, nơi người xem là những người tiếp nhận thông tin thụ động. Không cần phải hình dung câu chuyện trong tâm trí, trẻ em có thể bỏ lỡ cơ hội phát triển tư duy sáng tạo của mình, điều vốn rất quan trọng đối với sự phát triển nhận thức.<br><br>
                    Theo quan điểm của tôi, <strong>mặc dù sách tranh có thể hạn chế một số khía cạnh của trí tưởng tượng, nhưng những lợi ích của chúng vượt xa nhược điểm này</strong>. <strong>Hình ảnh là những công cụ cần thiết để giới thiệu trẻ em đến với thế giới của việc đọc trước khi chúng có thể xử lý các cuốn sách nhiều chữ.</strong> Khi chúng lớn lên và kỹ năng đọc của chúng được cải thiện, chúng có thể chuyển tự nhiên sang những cuốn sách không có tranh ảnh, điều này sau đó sẽ phát triển hơn nữa trí tưởng tượng của chúng.<br><br>
                    Tóm lại, mặc dù một số người lo lắng rằng sách tranh có thể ảnh hưởng tiêu cực đến sự sáng tạo giống như tivi, tôi tin rằng <strong>chúng đóng một vai trò tích cực và thiết yếu trong nền giáo dục sớm của trẻ</strong>. Cha mẹ nên sử dụng chúng như một bước đệm để giúp trẻ hình thành thói quen đọc sách suốt đời.
                    </div>
                </div>
            </div>
        """
    }
]

recitationQuestions = {
    "adv-disadv": [
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>1. MỞ BÀI<br>Viết câu giới thiệu chủ đề:", "target": "In recent years, [chủ đề] has become increasingly prevalent in modern society."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>1. MỞ BÀI<br>Viết câu khẳng định vấn đề có hai mặt (lợi và hại):", "target": "Although it brings certain benefits, there are also some negative aspects."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>1. MỞ BÀI<br>Viết câu giới thiệu mục đích bài viết:", "target": "This essay will examine both the advantages and disadvantages."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu chủ đoạn cho thân bài miêu tả thuận lợi:", "target": "On the one hand, [chủ đề] offers several advantages."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu dẫn lợi ích 1:", "target": "One major benefit is that [lợi ích 1]."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu dẫn lợi ích 2:", "target": "Another positive effect is that [lợi ích 2]."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu dẫn lợi ích 3:", "target": "A further aspect to consider is that [lợi ích 3]."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu chủ đoạn cho thân bài miêu tả bất lợi:", "target": "On the other hand, there are some disadvantages that should be considered."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu dẫn bất lợi 1:", "target": "One possible drawback is that [bất lợi 1]."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu dẫn bất lợi 2:", "target": "Another negative aspect is that [bất lợi 2]."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>2. THÂN BÀI<br>Viết câu dẫn bất lợi 3:", "target": "A further concern is that [bất lợi 3]."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>3. KẾT BÀI<br>Viết câu Kết bài khẳng định chủ đề có cả hai mặt:", "target": "In conclusion, [chủ đề] presents both advantages and disadvantages."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>3. KẾT BÀI<br>Viết câu nhận xét chung:", "target": "The points discussed above highlight its key aspects."},
        {"cue": "[DÀN Ý 01 - THUẬN LỢI & BẤT LỢI]<br>3. KẾT BÀI<br>Viết câu chốt lại lời khuyên :", "target": "Overall, understanding these factors helps provide a more balanced view of this topic."}
    ],
    "cause-effect": [
        {"cue": "[NGUYÊN NHÂN & GIẢI PHÁP]<br>1. MỞ BÀI<br>Viết câu dẫn dắt chủ đề:", "target": "In recent years, [chủ đề] has become a growing concern in many parts of the world."},
        {"cue": "[NGUYÊN NHÂN & GIẢI PHÁP]<br>1. MỞ BÀI<br>Viết câu nêu mức độ nghiêm trọng:", "target": "This issue has created several challenges for both individuals and society."},
        {"cue": "[NGUYÊN NHÂN & GIẢI PHÁP]<br>1. MỞ BÀI<br>Viết câu giới thiệu mục đích bài viết:", "target": "This essay will examine the main causes of this problem and suggest possible solutions."},
        {"cue": "[NGUYÊN NHÂN & GIẢI PHÁP]<br>2. THÂN BÀI<br>Viết câu chủ đoạn Nguyên Nhân:", "target": "This issue can be attributed to several key factors."},
        {"cue": "[NGUYÊN NHÂN & GIẢI PHÁP]<br>2. THÂN BÀI<br>Viết câu chủ đoạn Ảnh Hưởng:", "target": "This problem can lead to several significant consequences."},
        {"cue": "[NGUYÊN NHÂN & GIẢI PHÁP]<br>2. THÂN BÀI<br>Viết câu chủ đoạn Giải Pháp:", "target": "To address this problem, several practical solutions can be implemented."},
        {"cue": "[NGUYÊN NHÂN & GIẢI PHÁP]<br>3. KẾT BÀI<br>Viết câu tóm tắt:", "target": "In conclusion, [chủ đề] is caused by several factors and requires practical solutions to address it effectively."}
    ],
    "opinion": [
        {"cue": "[OPINION ESSAY]<br>1. MỞ BÀI<br>Viết câu giới thiệu chủ đề:", "target": "In recent years, the idea that [quan điểm] has attracted considerable public attention and discussion."},
        {"cue": "[OPINION ESSAY]<br>1. MỞ BÀI<br>Viết câu nêu lập trường cá nhân:", "target": "From my perspective, I completely agree / disagree with this opinion for several important reasons."},
        {"cue": "[OPINION ESSAY]<br>1. MỞ BÀI<br>Viết câu giới thiệu nội dung bài viết:", "target": "This essay will present the main arguments supporting my viewpoint."},
        {"cue": "[OPINION ESSAY]<br>2. THÂN BÀI<br>Viết câu luận điểm 1:", "target": "The first reason why I agree / disagree with this opinion is that [lý do 1]."},
        {"cue": "[OPINION ESSAY]<br>2. THÂN BÀI<br>Viết câu luận điểm 2:", "target": "Another important reason is that [lý do 2]."},
        {"cue": "[OPINION ESSAY]<br>2. THÂN BÀI<br>Viết câu luận điểm 3:", "target": "A further reason supporting my viewpoint is that [lý do 3]."},
        {"cue": "[OPINION ESSAY]<br>3. KẾT BÀI<br>Viết câu khẳng định lại lập trường:", "target": "In conclusion, I strongly agree / disagree with the idea that [quan điểm]."}
    ],
    "discussion": [
        {"cue": "[DISCUSSION ESSAY]<br>1. MỞ BÀI<br>Viết câu giới thiệu chủ đề:", "target": "In recent years, [chủ đề] has become a subject of considerable debate."},
        {"cue": "[DISCUSSION ESSAY]<br>1. MỞ BÀI<br>Viết câu nêu 2 quan điểm:", "target": "Some people believe that [ý kiến 1], while others argue that [ý kiến 2]."},
        {"cue": "[DISCUSSION ESSAY]<br>1. MỞ BÀI<br>Viết câu giới thiệu nội dung bài:", "target": "This essay will discuss both perspectives and present my personal viewpoint."},
        {"cue": "[DISCUSSION ESSAY]<br>2. THÂN BÀI<br>Viết câu chủ đoạn phân tích ý kiến 1:", "target": "On the one hand, it is argued that [ý kiến 1]."},
        {"cue": "[DISCUSSION ESSAY]<br>2. THÂN BÀI<br>Viết câu chủ đoạn phân tích ý kiến 2:", "target": "On the other hand, it is believed that [ý kiến 2]."},
        {"cue": "[DISCUSSION ESSAY]<br>3. KẾT BÀI<br>Viết câu kết luận khách quan:", "target": "In conclusion, both sides of the argument present valid points."},
        {"cue": "[DISCUSSION ESSAY]<br>3. KẾT BÀI<br>Viết câu chốt lại quan điểm cá nhân:", "target": "However, I personally believe that [quan điểm cá nhân] because [lý do ngắn gọn]."}
    ]
}

js_content = "const essayTypes = " + json.dumps(essayTypes, ensure_ascii=False, indent=4) + ";\n\n"
js_content += "const recitationQuestions = " + json.dumps(recitationQuestions, ensure_ascii=False, indent=4) + ";\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Generated data.js successfully.")
