
import pytest
from routes.functions import * 
from flask import Flask
import os
from src.webserver import create_app
import mysql.connector 





@pytest.fixture
def app():
        
    app = create_app("Dogs_product")
    
    app.config['TESTING'] = True
    return app


def test_get_user(app):
        with app.test_client() as client:
            response = client.get('/user')
            assert response.status_code == 200


            
def test_exist_database():
    try:
        con = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="NASSERDINE",
            database="Dogs_product",
            port=3306
        )
        # If the connection is successful, the test passes
        assert con.is_connected()
        con.close()  # Close the connection to avoid leaving connections open
    except Exception as e:
        # If an exception occurs, fail the test with the error message
        pytest.fail(f"Caught exception: {type(e).__name__}")


# test/function_test.py

def test_add_user(app):
    with app.test_client() as client:
        # Datos de prueba para el usuario
        user_data = {
            "id": 2,  # Use a unique id for the test data
            "name": "bilbaino",
            "adress": "aitorcarisma@gmail.com",
            "phone": "632123454"
        }

        # Llamamos a la función que queremos probar y pasamos los datos de prueba en formato JSON
        response = client.post('/user/add', json=user_data)

        # Comprobamos que la respuesta tiene el código de estado 200 (OK)
        assert response.status_code == 200

        # Comprobamos que la respuesta contiene el mensaje de éxito "Error al agregar el usuario"
        assert response.data.decode("utf-8") == "Error al agregar el usuario"
