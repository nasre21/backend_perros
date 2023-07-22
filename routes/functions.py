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
    except:

        return "Error al agregar el usuario"
    


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


def user_delete(id_delete):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('DELETE FROM clientes WHERE id = %s', (id_delete,))
    con.commit()
    con.close()
    return 'Product deleted'

def user_edit(id_edit,data):
    con = db.conectdb()
    cursor = con.cursor()
    
    
    if "name" in data:
        name = data["name"]
        cursor.execute('UPDATE clientes SET name = %s WHERE id = %s', (name, id_edit))

    if "adress" in data:
        adress = data["adress"]
        cursor.execute('UPDATE clientes SET adress = %s WHERE id = %s', (adress, id_edit))

    if "phone" in data:
        phone = data["phone"]
        cursor.execute('UPDATE clientes SET phone = %s WHERE id = %s', (phone, id_edit))
              
    con.commit()
    con.close()

    return 'Dates modified'