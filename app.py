from flask import Flask
from api.api_pokemon import api_pk


app = Flask(__name__)
app.register_blueprint(api_pk,url_prefix='/api')

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000, debug=True)