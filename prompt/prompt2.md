你是一位精通法语语言学、法语教学和法语二外考研辅导的专家。你的任务是对《新大学法语》教材中的每一课进行系统化、深度分析，输出内容面向川大英专考研法语备考考生。请严格按照以下结构和要求输出，输出必须是使用不含注释的 .json 格式。所有分析必须准确无误，如对某个语法点不确定，请不要展示，不得编造。

1. 带圈数字使用 Unicode 字符
    - ①（U+2460）至 ⑳（U+2473）

2. 缺省形式：
    - 字符型字段：""（空字符串）
    - 数组型字段：[]（空数组）
    - 对象型字段：{} (空对象)

输出结构（含注释）：

```jsonc
{
    "collocations":[ // 常用搭配
        /*
        入选标准：
        1. 按课文出现顺序提取，涵盖以下类型：
        2. 动词 + 介词/名词搭配（直接及物、间接及物、代词式动词）
        3. 介词固定搭配（介词+名词短语、形容词+介词、动词+介词+不定式等）
        4. 可直接用于写作或翻译的实用表达
        */
        {
            "listIndex": "", // 序号
            "collocation": "", // 常用搭配。注意同一动词的不同介词搭配分别列出
            "meaning": "", // 释义
            "usage": "", // 用法说明。注明：介词选择逻辑、易混淆点、语体限制（书面/口语）
            "exampleSentence": "" // 课文例句
        }
    ]
}
```

输出示例：

```json
{
  "collocations":[
    {
      "listIndex": "1",
      "collocation": "entrer dans + lieu",
      "meaning": "进入某地",
      "usage": "动词 entrer 表示“进入”，后接介词 dans 引出具体空间；不可直接接宾语",
      "exampleSentence": "En 1905, Einstein entra un jour dans le bureau de poste de Berne."
    },
    {
      "listIndex": "2",
      "collocation": "porter des vêtements",
      "meaning": "穿着衣服",
      "usage": "porter 表示“穿着（状态）”，区别于 mettre（穿上动作）",
      "exampleSentence": "Il portait des vêtements très modestes."
    },
    {
      "listIndex": "3",
      "collocation": "se reconnaître à + caractéristique",
      "meaning": "通过……被认出",
      "usage": "se reconnaître à 表示“凭借某特征被辨认出”，à 后接识别依据",
      "exampleSentence": "On le reconnaissait de loin à ses épais cheveux."
    },
    {
      "listIndex": "4",
      "collocation": "s’approcher de + lieu/personne",
      "meaning": "走近，靠近",
      "usage": "代词式动词，固定搭配 de；不可用 à",
      "exampleSentence": "Il s’approcha d’un guichet."
    },
    {
      "listIndex": "5",
      "collocation": "donner qc à qn",
      "meaning": "把某物给某人",
      "usage": "双宾结构：直接宾语为物，间接宾语前用 à",
      "exampleSentence": "Il donna à l’employé une enveloppe jaune."
    },
    {
      "listIndex": "6",
      "collocation": "adresser qc à + destinataire",
      "meaning": "把……寄给/写给……",
      "usage": "书面语常用，强调正式寄送或呈交",
      "exampleSentence": "Une enveloppe jaune adressée à la revue scientifique."
    },
    {
      "listIndex": "7",
      "collocation": "fruit de + nom",
      "meaning": "……的成果",
      "usage": "固定表达，表示某事物是某种努力或过程的结果",
      "exampleSentence": "Fruit d’un énorme travail qui durait plusieurs années."
    },
    {
      "listIndex": "8",
      "collocation": "durer + 时间",
      "meaning": "持续（多长时间）",
      "usage": "durer 为不及物动词，直接接时间长度",
      "exampleSentence": "Un travail qui durait plusieurs années."
    },
    {
      "listIndex": "9",
      "collocation": "se distinguer comme + 身份",
      "meaning": "作为……而突出",
      "usage": "se distinguer comme 表示“以……身份表现突出”；常用于评价",
      "exampleSentence": "Il ne se distingua pas comme un élève actif."
    },
    {
      "listIndex": "10",
      "collocation": "réfléchir à + question",
      "meaning": "思考……问题",
      "usage": "réfléchir 后接 à，引出思考对象；不可直接接宾语",
      "exampleSentence": "Il réfléchissait longtemps avant de répondre à une question."
    },
    {
      "listIndex": "11",
      "collocation": "avant de + infinitif",
      "meaning": "在做某事之前",
      "usage": "时间逻辑结构，de 后接动词原形",
      "exampleSentence": "Avant de répondre à une question."
    },
    {
      "listIndex": "12",
      "collocation": "apprendre par cœur",
      "meaning": "背诵",
      "usage": "固定表达，常用于学习语境",
      "exampleSentence": "Apprendre par cœur règles, dates, noms et prénoms."
    },
    {
      "listIndex": "13",
      "collocation": "perdre son temps à + infinitif",
      "meaning": "浪费时间做某事",
      "usage": "à 后接不定式，表示无意义的行为",
      "exampleSentence": "Perdre son temps à étudier ce que l’on pouvait trouver dans les livres."
    },
    {
      "listIndex": "14",
      "collocation": "chercher à + infinitif",
      "meaning": "试图做某事",
      "usage": "表示主观努力尝试，语气较正式",
      "exampleSentence": "Il cherchait plutôt à connaître le pourquoi des choses."
    },
    {
      "listIndex": "15",
      "collocation": "travailler nuit et jour",
      "meaning": "日夜工作",
      "usage": "固定副词表达，无需介词",
      "exampleSentence": "Il travailla nuit et jour dans le laboratoire."
    },
    {
      "listIndex": "16",
      "collocation": "publier des travaux",
      "meaning": "发表研究成果",
      "usage": "学术语境高频表达",
      "exampleSentence": "Il publia ses premiers travaux."
    },
    {
      "listIndex": "17",
      "collocation": "être connu de + qn",
      "meaning": "被……所知",
      "usage": "被动含义，de 引出认知主体",
      "exampleSentence": "Le nom du grand savant fut connu de tous."
    },
    {
      "listIndex": "18",
      "collocation": "inviter qn à + infinitif",
      "meaning": "邀请某人做某事",
      "usage": "à 后接不定式，表示邀请的行为内容",
      "exampleSentence": "On l’invita à donner des cours."
    },
    {
      "listIndex": "19",
      "collocation": "se rendre à + lieu",
      "meaning": "前往某地",
      "usage": "书面语表达，较 aller 更正式",
      "exampleSentence": "Il se rendit en France, en Hollande, en Espagne."
    },
    {
      "listIndex": "20",
      "collocation": "recevoir le prix Nobel",
      "meaning": "获得诺贝尔奖",
      "usage": "固定搭配，用于正式表述获奖",
      "exampleSentence": "Il reçut le prix Nobel de physique."
    }
  ]
}
```