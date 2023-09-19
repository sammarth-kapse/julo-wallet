from flask import Blueprint, Flask
from flask_restx import Api
import routing

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp, version='1.0', title='Wallet Api', description='Wallet Api')

routing.add_routes(api)
app.register_blueprint(api_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
