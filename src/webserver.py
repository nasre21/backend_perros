from flask import Flask, request

from flask_cors import CORS

from routes.functions import *



def create_app(database):
    
    app = Flask(__name__)
    CORS(app)
    
    # initialising the database
    init_db(database)


        # ROUTES ADD USERS
    @app.route('/user', methods=['POST'])
    def add_user_route():
            return add_user()
    
    # ROUTES GET USERS
    # routes a_get
    @app.route('/user', methods=['GET'])
    def get_users():
            return users_get()
    
    @app.route("/user/<int:id>", methods=['GET'])
    def get_a_user(id):
        return get_user(id)
    
    # ROUTES DELETE USERS  
    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
          return user_delete(id)
    
   #  ROUTES UPDATE USERS  
    @app.route('/user/int:id>', methods=['PATCH'])
    def edit_user(id):
          data = request.get_json()
          return user_edit(id, data)
    

 #Routes add Dogs

    @app.route('/dogs', methods=['GET'])
    def get_dogs():
            return dogs_get()

# routes a_get
    @app.route("/dogs/<int:id_product>", methods=['GET'])
    def get_a_product(id_product):
        return get_product(id_product)
    
    @app.route('/dogs', methods=['POST'])
    def add_dogs():
            return dogs_add()    

#routes delete
    @app.route('/dogs/<int:id_delete>', methods=['DELETE'])
    def delete_dogs(id_delete):
            return dogs_delete(id_delete)
    
    #  ROUTES UPDATE USERS  
    @app.route("/dogs/<int:id>", methods=['PATCH'])
    def edit_dogs(id):
          data = request.get_json()
          return dogs_edit(id, data)
    


    # ROUTES ADD COMPRAS
    @app.route('/compras', methods=['POST'])
    def create_compra():
        return add_compra()

    # ROUTES GET COMPRAS
    # routes a_get
    @app.route('/compras', methods=['GET'])
    def get_all_compras():
        return get_compras()

    @app.route("/compras/<int:id>", methods=['GET'])
    def get_a_compra(id):
        return get_compra(id)

    # ROUTES DELETE COMPRAS
    @app.route('/compras/<int:id>', methods=['DELETE'])
    def delete_a_compra(id):
        return delete_compra(id)

    # ROUTES UPDATE COMPRAS
    @app.route('/compras/<int:id>', methods=['PATCH'])
    def edit_a_compra(id):
        data = request.json 
        return edit_compra(id,data)

    

    # TO EXECUTE THE APPLICATION
    if __name__ == '__main__':
        app.run(debug=True)
    # with app.run we're going to indicate that the app is going to be in development
    return app





