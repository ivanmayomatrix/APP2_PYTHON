# APP2_PYTHON
Ejercicio Python login

## Instrucciones para ejecutar el proyecto

1. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar la base de datos SQLite:
   ```bash
   python backend/init_db.py
   ```

4. Ejecutar el código:
   ```bash
   python backend/app.py
   ```

## Notas adicionales

- Asegúrate de tener Python 3 instalado en tu sistema.
- Puedes modificar el archivo `backend/app.py` según tus necesidades.
- La base de datos `database.db` se creará en el directorio del proyecto.