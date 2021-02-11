from flask import Blueprint, jsonify, Flask, flash, request, redirect, url_for, session
import logging
import os
from werkzeug.utils import secure_filename
from app import config

UPLOAD_FOLDER = './'
MOD_UPLOAD_FILE = Blueprint(
    'upload', __name__, url_prefix='/upload'
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')

@MOD_UPLOAD_FILE.route("/", methods=['POST', 'GET'])
def fileUpload():
    logger.info("welcome to upload`")
    target=os.path.join(UPLOAD_FOLDER, config.PROFILE_DIR)
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    return jsonify(True)
