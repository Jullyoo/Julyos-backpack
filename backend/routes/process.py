from flask import (Blueprint, request, jsonify)
from services.file_service import (read_file)
from services.export_service import (export_csv)
from core.engine import (ETLEngine)

process_bp = Blueprint("process", __name__)

@process_bp.route("/process", methods=["POST"])
def process():
    file = request.files["file"]
    operations = request.form.getlist("operations")
    df = read_file(file)
    result_df = ETLEngine.run(df, operations)
    export_csv(result_df, "Resultado.csv")
    return jsonify({ "status":"success", "filename": "Resultado.csv" })