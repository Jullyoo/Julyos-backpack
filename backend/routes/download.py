import os
from flask import (Blueprint, send_file)

download_bp = Blueprint("download", __name__)

@download_bp.route("/download/<filename>")
def download(filename):
    filepath = os.path.join("outputs", filename)
    return send_file(filepath, as_attachment=True)