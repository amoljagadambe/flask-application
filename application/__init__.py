from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'List'

api = Api(app, title='Basic App', description='Created by Amol Jagadambe', default='Flask', default_label='Controllers',
          validate=True)

from application.resources import home
