def acronym(words):
    word = words.split()         #以空白作為分隔建立list
    result = ""
    for i in word:
        result += i[0].upper()   #把每個單字字首大寫
    print(result)

words = input('請輸入一段話')
acronym(words)