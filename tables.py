import csv
list1=[{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},]
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields=['name', 'age', 'job']
    writer=csv.DictWriter(f, fields, ';')
    writer.writeheader()
    for user in list1:
        writer.writerow(user)
