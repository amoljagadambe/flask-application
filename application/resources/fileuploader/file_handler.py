from werkzeug.utils import secure_filename
from application import app
import os

ALLOWED_EXTENSIONS = set(['wav', 'mp3'])
BASE_FOLDER = os.path.abspath(os.path.dirname(__name__))
UPLOAD_PATH = "/application/resources/fileuploader/audio-files/"

app.config['UPLOAD_FOLDER'] = BASE_FOLDER + UPLOAD_PATH


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


class FileHandler:
    def __init__(self):
        print("File handler init")

    @staticmethod
    def save_file(request):
        if 'file' not in request.files:
            return "No file found"

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(file_path)

        return file_path
