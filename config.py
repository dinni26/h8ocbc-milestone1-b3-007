import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Untuk Connexion Instance 
connex_app = connexion.App(__name__, specification_dir=basedir)

# Flask app di Connexion Instance nya
app = connex_app.app

# Config SQL Alchemy untuk database
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'final_proj.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://otelkuabivpfnj:297fd17d4f5d7412fdf865d27ef6e0c229d58956231b5bd7a3be444489e26f31@ec2-44-199-143-43.compute-1.amazonaws.com:5432/d7ltdv75447p4v'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Untuk SQLAlchemy Instance
db = SQLAlchemy(app)

# Untuk Marshmallow Instance
ma = Marshmallow(app)