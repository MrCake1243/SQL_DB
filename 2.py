import sqlite3
print("Действия для программы:\n1 - Вывести все товары\n2 - Вывести список категорий\n3 - Добавить товар\n4 - Добавить категории\n5 - Удалить товар\n0 - ВЫХОД")
def all_table():
    with sqlite3.connect("t1.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT name, price, category_name 
                       FROM products 
                       LEFT JOIN categories 
                       ON products.category_id = categories.id;''')
        result = cursor.fetchall()
        for row in result:
            print(f"Товар: {row[0]} | Цена: {row[1]} | Категория: {row[2]} ")
    conn.close()

def all_categories():
    with sqlite3.connect("t1.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM categories;''')
        result = cursor.fetchall()
        print("Категории:")
        for row in result:
            print(f"{row[0]} - {row[1]}")
    conn.close()

def add_product():
    count_cat = int(count_categories())
    with sqlite3.connect("t1.db") as conn:
        cursor = conn.cursor()
        name = input("Введите название: ")
        price = float(input("Введите стоимость: "))
        
        category_id = int(input("Ведите ID категории: "))
        if category_id <= count_cat:
            cursor.execute(f"INSERT INTO products(name, price, category_id) VALUES(:name,:price,:category_id)", {"name": name, "price": price, "category_id": category_id})
            print("Товар добавлен!")
        else: 
            print(f"Такой категории нет, всего категорий {count_cat}")
    conn.close()

def add_category():
    with sqlite3.connect("t1.db") as conn:
        cursor = conn.cursor()
        category_name = input("Введите название категории: ")
        cursor.execute(f"INSERT INTO categories(category_name) VALUES(:category_name)", {"category_name": category_name})
        print(f"Категория добавлена! Теперь категорий {count_categories() + 1}!")
    conn.close()

def delete_product():
    with sqlite3.connect("t1.db") as conn:
        cursor = conn.cursor()
        delete_id = input("Введите индекс товара для удаления:")
        cursor.execute(f"DELETE FROM products WHERE id =?", (delete_id,))
        print(f"Товар удалён")
    conn.close()

def count_categories():
    with sqlite3.connect("t1.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT category_name FROM categories;''')
        result = cursor.fetchall()
        count = 0
        for row in result:
            count += 1
        return count
    conn.close()
choice = int(input("Введите № действия: "))
while choice != 0:
    match choice:
        case 1: 
            all_table()
        case 2:
            all_categories()
        case 3:
            add_product()
        case 4:
            add_category()
        case 5:
            delete_product()
    choice = int(input("Введите № действия: "))