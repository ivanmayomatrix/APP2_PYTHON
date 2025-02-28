from models.model import Database

class Controller:
    def __init__(self):
        self.db = Database()

    def register_user(self, username, password):
        return self.db.register_user(username, password)

    def login_user(self, username, password):
        print(f"Controller: Validando usuario {username} con contraseña {password}")
        result = self.db.validate_user(username, password)
        print(f"Controller: Resultado de validación {result}")
        return result

    def fetch_products(self):
        products = self.db.get_products()
        return [{"id": product[0], "name": product[1], "price": product[2]} for product in products]
