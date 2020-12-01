from application.resources.fileuploader.file_handler import FileHandler
from application.resources.utils.user_input import upload_parser
from flask_restx import Resource
from application import api
from flask import request

file = api.namespace('fileUploader', description='Operations related to File Uploader')


@file.route('/', endpoint='/fileUploader')
class FileUploaderController(Resource):

    @api.expect(upload_parser, validate=False)
    def post(self):
        FileHandler().save_file(request)
        return "file successfully saved"
