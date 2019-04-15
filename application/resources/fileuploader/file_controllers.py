from application.resources.fileuploader.file_handler import FileHandler
from application.resources.recommender.user_input import upload_parser
from flask_restplus import Resource
from application import api
from flask import request

file = api.namespace('fileUploader', description='Operations related to fileUploader')


@file.route('/', endpoint='/fileUploader')
class fileUploaderController(Resource):

    @api.expect(upload_parser, validate=False)
    def post(self):
        FileHandler().saveFile(request)
        return "file successfully saved"
