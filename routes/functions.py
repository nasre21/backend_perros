import src.database as db
from flask import request, jsonify



database_path = ""

def init_db(database):
    global database_path
    database_path = database


def dogs_add_user():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"
        
        cursor = con.cursor()
        data = request.get_json()
        id = data["id"]

        name = data["name"]
        address = data["adress"] 
        phone = data["phone"]
        cursor.execute('INSERT INTO clientes (id, name, adress, phone) VALUES (%s,%s, %s, %s)', (id, name, address, phone,))
        con.commit()
        con.close()

        print('Usuario agregado exitosamente')

        return "Usuario creado exitosamente"
    except Exception as e:

        return f"Error al agregar el usuario: {str(e)}"
    


def dogs_get_user():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"
        
        cursor = con.cursor()
        cursor.execute('SELECT * FROM clientes')
        users = cursor.fetchall()
        con.close()

        data_users = [{'id': user[0], 'name': user[1], 'address': user[2], 'phone': user[3]} for user in users]

        return jsonify(data_users)
    except Exception as e:

        return f"Error al obtener los usuarios: {str(e)}"


