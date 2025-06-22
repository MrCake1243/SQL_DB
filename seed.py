from models import *
TABLES = [Author, Book, Genre, BookGenre]
with db:
    db.drop_tables(TABLES)
    db.create_tables(TABLES)

     # Создаем авторов
    authors = [
        {'name': 'Анджей Сапковский'},
        {'name': 'Жюль Верн'},
        {'name': 'Олдос Хаксли'}
    ]
    Author.insert_many(authors).execute()

    # Создаем жанры
    genres = [
        {'name': 'Фэнтези'},
        {'name': 'Приключения'},
        {'name': 'Антиутопия'},
        {'name': 'Детектив'}
        
    ]
    Genre.insert_many(genres).execute()

    # Создаем книги и связи
    books = [
        {
            'title': 'Ведьмак',
            'author': 'Анджей Сапковский',
            'price': 699.99,
            'genres': ['Фэнтези', 'Приключения']
        },
        
        {
            'title': 'Таинственный остров',
            'author': 'Жюль Верн',
            'price': 499.99,
            'genres': ['Приключения']
        },

        {
            'title': 'О дивный новый мир',
            'author': 'Олдос Хаксли',
            'price': 650.50,
            'genres': ['Антиутопия']
        },
    ]

    for book_data in books:
        author = Author.get(Author.name == book_data['author'])
        book = Book.create(
            title=book_data['title'],
            author=author,
            price=book_data['price']
        )
        
        # Добавляем связи с жанрами
        for genre_name in book_data['genres']:
            genre = Genre.get(Genre.name == genre_name)
            BookGenre.create(book=book, genre=genre)


