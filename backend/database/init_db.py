import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Crear la tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Crear la tabla de productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# Insertar productos iniciales solo si la tabla está vacía
cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", [
        ("Laptop HP", 750.00),
        ("iPhone 14", 999.00),
        ("Samsung Galaxy S24", 1200.00),
        ("Audífonos Sony", 150.00)
    ])
    print("✅ Productos insertados.")

# Insertar usuario por defecto si no existe
cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Base de datos `database.db` creada correctamente.")
