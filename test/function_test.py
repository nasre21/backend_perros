
import pytest
from routes.functions import * 
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