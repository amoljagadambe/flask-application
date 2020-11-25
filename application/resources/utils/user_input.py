from flask_restx import fields
from application import api
from werkzeug.datastructures import FileStorage

user_fields = api.model('Recommendation', {
    'word': fields.String,
    'category': fields.String(required=False),
    'word_s1': fields.String(required=False),
    'word_s2': fields.String(required=False),
    'word_s3': fields.String(required=False),
    'word_s4': fields.String(required=False),
    'phase': fields.String(required=False),
    'primary_syllable_stress': fields.String(required=False)
})


upload_parser = api.parser()
upload_parser.add_argument('file', location='files',type=FileStorage)