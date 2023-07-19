from flask import Flask, request

from flask_cors import CORS

from routes.functions import *



def create_app(database):
    
    app = Flask(__name__)
    CORS(app)
    
    # initialising the database
    init_db(database)


     # ROUTES ADD USERS
    @app.route('/user/add', methods=['POST'])
    def add_user():
            return dogs_add_user()
    




    # ROUTES GET USERS
    @app.route('/user', methods=['GET'])
    def get_user():
            return dogs_get_user()
    # ROUTES DELETE USERS  
    @app.route('/user/delete/<int:id_delete>', methods=['DELETE'])
    def delete_user(id_delete):
          return user_delete(id_delete)
    
   #  ROUTES UPDATE USERS  
    @app.route('/user/edit/<int:id_edit>', methods=['PATCH'])
    def edit_user(id_edit):
          data = request.get_json()
          return user_edit(id_edit, data)
    

    # TO EXECUTE THE APPLICATION
    if __name__ == '__main__':
        app.run(debug=True)
    # with app.run we're going to indicate that the app is going to be in development
    return app


