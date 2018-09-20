with open('referat.txt', 'r', encoding='utf-8') as f:
    content=str(f.read())
    l=len(content)
    print(l)
    content_list=content.split(' ')
    wordcount=len(content_list)
    print(wordcount)
    content_new=content.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(content_new)

