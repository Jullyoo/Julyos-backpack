from flask import (Blueprint, request, jsonify)
from services.file_service import read_file

preview_bp = Blueprint("preview",__name__)

@preview_bp.route("/preview", methods=["POST"])
def preview():
    file = request.files["file"]
    df = read_file(file)
    return jsonify({

        "columns": df.columns.tolist(),

        "rows": df.head(20).fillna("").to_dict(orient="records"),

        "total_rows": len(df),

        "total_columns": len(df.columns) 
    })