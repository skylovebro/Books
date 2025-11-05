try:
    myfile = open('books.txt', 'r', encoding='utf-8')
    myfile.close()
except FileNotFoundError:
    myfile = open('books.txt', 'w', encoding='utf-8')
    myfile.close()

myfile = open('books.txt', 'r', encoding='utf-8')
books = myfile.readlines()
myfile.close()

def add_book():
    tittle_book = input('Введите название книги и год:')
    myfile = open('books.txt', 'a', encoding='utf-8')
    myfile.write(tittle_book + '\n')
    myfile.close()

def look_book():
    myfile = open('books.txt', 'r', encoding='utf-8')
    content = myfile.read()
    myfile.close()
    print(content)

def delete_book():
    title = input('Введите название книги которую хотите удалить')
    myfile = open('books.txt', 'r', encoding='utf-8')
    books = myfile.readlines()
    myfile.close()

    new_books = []
    found = False
    for book in books:
        if title not in book:
            new_books.append(book)
        else:
            found = True

    myfile = open('books.txt', 'w', encoding='utf-8')
    myfile.writelines(new_books)
    myfile.close()

def search_book():
    search = input('Введите название книги которую вы хотите найти:')
    myfile = open('books.txt', 'r', encoding='utf-8')
    books = myfile.readlines()
    myfile.close()

    for i, book in enumerate(books, 1):
        if search in book or search == str(i):
            print(book.strip())

def replace():
    offer = input('Введите книгу которую надо заменить')
    poffer = input('Введите книгу на которую надо заменить')
    for i, book in enumerate(books, 1):
        if offer in book or offer == str(i):
            ntu = books.index(book)
            books[ntu] = poffer
    myfile = open('books.txt', 'w', encoding='utf-8')
    myfile.writelines(books)
    myfile.close()

while True:
    print('1.Добавить книгу\n2.Просмотреть книги\n3.Удалить книгу по названию\n4.Найти книгу\n5.Перезапись')
    chhose = int(input())
    if chhose == 1:
        add_book()
    elif chhose == 2:
        look_book()
    elif chhose == 3:
        delete_book()
    elif chhose == 4:
        search_book()
    elif chhose == 5:
        replace()
