import sqlite3
import hashlib

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Crea las tablas de usuarios y productos si no existen."""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )""")
        
        self.conn.commit()

    def hash_password(self, password):
        """Encripta la contraseña."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """Registra un nuevo usuario."""
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                                (username, self.hash_password(password)))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def validate_user(self, username, password):
        """Valida credenciales de usuario."""
        print(f"Database: Validando usuario {username}")
        self.cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        if user:
            stored_hash = self.hash_password(user[0])
            provided_hash = self.hash_password(password)
            print(f"Database: Stored hash: {stored_hash}")
            print(f"Database: Provided hash: {provided_hash}")
            return stored_hash == provided_hash
        print("Database: Usuario no encontrado o contraseña incorrecta")
        return False

    def get_products(self):
        """Obtiene todos los productos."""
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()
