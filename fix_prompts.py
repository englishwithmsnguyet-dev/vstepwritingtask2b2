with open("generate_b2_data.py", "r", encoding="utf-8") as f:
    content = f.read()

req_text = " Include reasons and any relevant examples to support your answer. You should write at least 250 words. Your response will be evaluated in terms of Task fulfillment, Organization, Vocabulary, and Grammar."

replacements = [
    (
        "Some people believe that e-learning will replace traditional classes in the future.<br><br><strong>Write an essay to discuss the advantages and disadvantages of online learning.</strong></p>",
        f"Some people believe that e-learning will replace traditional classes in the future.<br><br><strong>Write an essay to discuss the advantages and disadvantages of online learning.</strong>{req_text}</p>"
    ),
    (
        "Participating in volunteer activities is believed to bring various benefits to individuals and the community.<br><br><strong>Write an essay to discuss the benefits of doing volunteer work.</strong></p>",
        f"Participating in volunteer activities is believed to bring various benefits to individuals and the community.<br><br><strong>Write an essay to discuss the benefits of doing volunteer work.</strong>{req_text}</p>"
    ),
    (
        "Obesity is a serious global problem in today's society, especially among young people...<br><br><strong>Write an essay to discuss the causes of obesity among young people and suggest possible solutions.</strong></p>",
        f"Obesity is a serious global problem in today's society, especially among young people. More than one-third of adults and 17% of youth in the United States are obese, although the prevalence remained stable between 2003-2004 and 2009-2010. Obesity causes a lot of conditions, including heart disease, stroke, type 2 diabetes, and certain types of cancer, some of the leading causes of preventable death.<br><br><strong>Write an essay to discuss the causes of obesity among young people and suggest possible solutions.</strong>{req_text}</p>"
    ),
    (
        "This trend has raised concerns about its possible causes and effects on individuals and society.<br><br><strong>Write an essay to discuss the causes of this trend and its effects.</strong></p>",
        f"This trend has raised concerns about its possible causes and effects on individuals and society.<br><br><strong>Write an essay to discuss the causes of this trend and its effects.</strong>{req_text}</p>"
    ),
    (
        "This trend is causing growing concern globally about its impacts on both individuals and organizations.<br><br><strong>Write an essay to discuss the effects of cybercrime and suggest possible solutions.</strong></p>",
        f"This trend is causing growing concern globally about its impacts on both individuals and organizations.<br><br><strong>Write an essay to discuss the effects of cybercrime and suggest possible solutions.</strong>{req_text}</p>"
    ),
    (
        "As a result, some people believe that children, especially girls, no longer need to learn how to cook or do household chores.<br><br><strong>To what extent do you agree or disagree with this opinion?</strong></p>",
        f"As a result, some people believe that children, especially girls, no longer need to learn how to cook or do household chores.<br><br><strong>To what extent do you agree or disagree with this opinion?</strong>{req_text}</p>"
    ),
    (
        "However, others argue that picture books may negatively affect children's imagination, just like watching television.<br><br><strong>Discuss both views and give your own opinion.</strong></p>",
        f"However, others argue that picture books may negatively affect children's imagination, just like watching television.<br><br><strong>Discuss both views and give your own opinion.</strong>{req_text}</p>"
    )
]

for old_str, new_str in replacements:
    content = content.replace(old_str, new_str)

with open("generate_b2_data.py", "w", encoding="utf-8") as f:
    f.write(content)
