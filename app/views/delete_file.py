from flask import Blueprint, jsonify, Flask, flash, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from app import config

UPLOAD_FOLDER = './'
MOD_DELETE_FILE = Blueprint(
    'delete', __name__, url_prefix='/delete'
)

@MOD_DELETE_FILE.route("/", methods=['POST', 'GET'])
def fileUpload():
    filename = request.args.get('filename')
    target=os.path.join(UPLOAD_FOLDER, config.PROFILE_DIR)
    destination="/".join([target, filename])
    os.remove(destination)
    return jsonify(True)
