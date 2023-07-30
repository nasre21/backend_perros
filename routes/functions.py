import src.database as db
from flask import request, jsonify



database_path = ""

def init_db(database):
    global database_path
    database_path = database


def add_user():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"
        
        cursor = con.cursor()
        data = request.get_json()

        name = data["name"]
        adress = data["adress"]
        phone = data["phone"] 
        password = data["password"]
        message = data["message"]
        cursor.execute('INSERT INTO clientes ( name, address, phone, password, message) VALUES (%s, %s, %s, %s, %s)', (name, adress, phone, password, message))
        
        con.commit()
        con.close()

        print('User agregado exitosamente')

        return "User creado exitosamente"
    except Exception as e:  # Captura excepciones específicas y muestra el error
        print("Error:", e)
        return "Error al agregar el user"



    
def get_user(id):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM clientes WHERE id_cliente = %s', (id,))
    data_user = cursor.fetchone()
    
    if data_user:
        data = {'id_cliente': data_user[0], 'name': data_user[1], 'adress': data_user[2], 'phone': data_user[3]}
        con.close()
        print(data)
        return jsonify(data)
    else:
        return 'The user was not found' 


def users_get():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"

        cursor = con.cursor()
        cursor.execute('SELECT * FROM clientes')
        users = cursor.fetchall()
        con.close()

        return users
    except Exception as e:
        print("Error:", e)
        return "Error al obtener los usuarios"


def user_delete(id_delete):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('DELETE FROM clientes WHERE id_cliente = %s', (id_delete,))
    con.commit()
    con.close()
    return 'Product deleted'

def user_edit(id_edit,data):
    con = db.conectdb()
    cursor = con.cursor()
    
    
    if "name" in data:
        name = data["name"]
        cursor.execute('UPDATE clientes SET name = %s WHERE id_cliente = %s', (name, id_edit))

    if "adress" in data:
        adress = data["adress"]
        cursor.execute('UPDATE clientes SET adress = %s WHERE id_cliente = %s', (adress, id_edit))

    if "phone" in data:
        phone = data["phone"]
        cursor.execute('UPDATE clientes SET phone = %s WHERE id_cliente = %s', (phone, id_edit))
              
    con.commit()
    con.close()

    return 'Dates modified'


# Dogs function
def dogs_add():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"
        
        cursor = con.cursor()
        data = request.get_json()
        id_product = data["id_product"]
        photo = data["photo"]
        description = data["description"] 
        precio = data["precio"]
        cliente_id = data["cliente_id"]
        cursor.execute('INSERT INTO product_perros (id_product ,photo, description, precio, cliente_id) VALUES (%s,%s, %s, %s, %s)', (id_product, photo, description, precio, cliente_id))
        con.commit()
        con.close()

        print('Perro agregado exitosamente')

        return "Perro creado exitosamente"
    except Exception as e:  # Captura excepciones específicas y muestra el error
        print("Error:", e)
        return "Error al agregar el perro"


def dogs_get():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"
        
        cursor = con.cursor()
        cursor.execute('SELECT * FROM product_perros')
        products = cursor.fetchall()
        con.close()

        data_products = [{'id_product': product[0], 'photo': product[1], 'description': product[2], 'precio': product[3],'cliente_id':product[4]} for product in products]

        return jsonify(data_products)
    except Exception as e:

        return f"Error al obtener los usuarios: {str(e)}"
    

def get_product(id):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM product_perros WHERE id_product = %s', (id,))
    data_product = cursor.fetchone()
    
    if data_product:
        data = {'id_product': data_product[0], 'photo': data_product[1], 'description': data_product[2], 'precio': data_product[3], 'cliente_id': data_product[4]}
        con.close()
        print(data)
        return jsonify(data)
    else:
        return 'The product was not found' 


def dogs_edit(id, data):
    con = db.conectdb()
    cursor = con.cursor()

    if "photo" in data:
        photo = data["photo"]
        cursor.execute('UPDATE product_perros SET photo = %s WHERE id_product = %s', (photo, id))

    if "description" in data:
        description = data["description"]
        cursor.execute('UPDATE product_perros SET description = %s WHERE id_product = %s', (description, id))

    if "precio" in data:
        precio = data["precio"]
        cursor.execute('UPDATE product_perros SET precio = %s WHERE id_product = %s', (precio, id))

    if "cliente_id" in data:
        cliente_id = data["cliente_id"]
        cursor.execute('UPDATE product_perros SET cliente_id = %s WHERE id_product = %s', (cliente_id, id))

    con.commit()
    con.close()

    return 'Product modified'


def dogs_delete(id_delete):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('DELETE FROM product_perros WHERE id_product = %s', (id_delete,))
    con.commit()
    con.close()
    return 'Product deleted'


def add_compra():
    try:
        con = db.conectdb()
        if con is None:
            return jsonify({"error": "Error: No se pudo establecer la conexión a la base de datos"})
        
        cursor = con.cursor()
        data = request.get_json()
        cantidad = data["cantidad"]
        producto_id = data["producto_id"]
        id_cliente = data["id_cliente"]
        print("@#@#@#data en add_compra-", data)

        cursor.execute('INSERT INTO compras (cantidad, producto_id, id_cliente) VALUES (%s, %s, %s)',
                       (cantidad, producto_id, id_cliente))
        con.commit()
        con.close()

        print('Compra agregada exitosamente')

        return jsonify({"message": "Compra creada exitosamente"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Error al agregar la compra", "details": str(e)})

    


def get_compra(id_compra):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM compras WHERE id_compras = %s', (id_compra,))
    data_compra = cursor.fetchone()
    
    if data_compra:
        data = {'id_compras': data_compra[0], 'cantidad': data_compra[1], 'producto_id': data_compra[2], 'id_cliente': data_compra[3]}
        con.close()
        print(data)
        return jsonify(data)
    else:
        return 'La compra no fue encontrada'

def get_compras():
    try:
        con = db.conectdb()
        if con is None:
            return jsonify({"error": "Error: No se pudo establecer la conexión a la base de datos"})

        cursor = con.cursor()
        cursor.execute('SELECT * FROM compras')

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

        compras = cursor.fetchall()
        con.close()

        # Convertir la lista de listas en una lista de diccionarios
        compras_dict = []
        for compra in compras:
            compra_dict = dict(zip(column_names, compra))
            compras_dict.append(compra_dict)

        return jsonify(compras_dict)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Error al obtener las compras", "details": str(e)})


def delete_compra(id_compra):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('DELETE FROM compras WHERE id_compras = %s', (id_compra,))
    con.commit()
    con.close()
    return 'Compra eliminada'

def edit_compra(id_compra, data):
    con = db.conectdb()
    cursor = con.cursor()
    
    if "cantidad" in data:
        cantidad = data["cantidad"]
        cursor.execute('UPDATE compras SET cantidad = %s WHERE id_compras = %s', (cantidad, id_compra))

    if "producto_id" in data:
        producto_id = data["producto_id"]
        cursor.execute('UPDATE compras SET producto_id = %s WHERE id_compras = %s', (producto_id, id_compra))

    if "id_cliente" in data:
        id_cliente = data["id_cliente"]
        cursor.execute('UPDATE compras SET id_cliente = %s WHERE id_compras = %s', (id_cliente, id_compra))
              
    con.commit()
    con.close()

    return 'Datos de la compra modificados'
