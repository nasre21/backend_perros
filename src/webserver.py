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
    def add_dogs():
            return dogs_add_user()
    




    # ROUTES GET USERS
    @app.route('/user', methods=['GET'])
    def get_dogs():
            return dogs_get_user()
    
    # TO EXECUTE THE APPLICATION
    if __name__ == '__main__':
        app.run(debug=True)
    # with app.run we're going to indicate that the app is going to be in development
    return app