
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS

from simple_app.endpoints import project_api_routes



def create_app():
    web_app = Flask(__name__)  # Initialize Flask App   # "Flask" is a constructor
    CORS(web_app) # Enabling CORS, which means giving security extension to our application

    api_blueprint = Blueprint('api_blueprint', __name__) # Blueprint means creating a copy, here we're creating a copy and assigning to the "API Route"
    api_blueprint = project_api_routes(api_blueprint) # Here, We're sending the API blueprint to "Project API Route" which is a module created in this "CRUD_APP"

    '''
    The above two lines are "Standard Syntax"
    '''
    
    web_app.register_blueprint(api_blueprint, url_prefix='/api')    

    return web_app


app = create_app()

if __name__ == "__main__":  # __name__ is a constructor
    app.run(host="0.0.0.0",debug= True)
