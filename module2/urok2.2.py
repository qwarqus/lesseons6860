qwe = {    "привіт": "hello",
    "друг": "friend",
    "сонце": "sun",
    "місяць": "moon"}
word = input('введіть слово українською ')
qwe = qwe.get(word)
print(f'''
переклад знайдено

{qwe}''')