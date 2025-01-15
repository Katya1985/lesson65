import sqlite3


def initiate_db():
    connection = sqlite3.connect("Prod.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title  TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.executescript('''
    INSERT INTO Products (title, description, price) 
    VALUES('Витамин Fe', 'Витамин железо', '100');
    INSERT INTO Products(title, description, price)
    VALUES('Мультивитамины', 'Витаминный комплекс', '200');
    INSERT INTO Products(title, description, price)
    VALUES('Витамин B9', 'Фолиевая кислота', '300');
    INSERT INTO Products(title, description, price)
    VALUES('Витамин D', 'Рыбный жир', '400');   
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("Prod.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users


if __name__ == '__main__':
    initiate_db()
    get_all_products()
