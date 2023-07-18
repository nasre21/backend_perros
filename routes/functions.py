import src.database as db
from flask import request



database_path = ""

def init_db(database):
    global database_path
    database_path = database


def dogs_add_user():
    try:
        con = db.conectdb()  # Asegúrate de llamar correctamente la función 'conectdb()'
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"
        
        cursor = con.cursor()
        data = request.get_json()
        id = data["id"]

        name = data["name"]
        address = data["adress"]  # Corregí el nombre de la variable 'adress' a 'address'
        phone = data["phone"]
        cursor.execute('INSERT INTO clientes (id, name, adress, phone) VALUES (%s,%s, %s, %s)', (id, name, address, phone,))
        con.commit()
        con.close()

        print('Usuario agregado exitosamente')

        return "Usuario creado exitosamente"
    except Exception as e:
        # Manejo de excepciones para capturar cualquier error durante la ejecución
        return f"Error al agregar el usuario: {str(e)}"


