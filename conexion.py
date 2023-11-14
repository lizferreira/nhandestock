#---LIBRERIAS---
from flask import Flask
from models import db


#Instanciamos la clase flask
app = Flask(__name__)

#---CONFIGURACION---#
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos_registrados.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#---INICIALIZAR SQLAlchemy---#
db.init_app(app)


with app.app_context():
    db.create_all()