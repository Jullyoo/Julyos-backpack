from flask import Flask
from flask_cors import CORS

from routes.process import process_bp
from routes.preview import preview_bp
from routes.download import download_bp

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": [
                "https://julyos-backpack.vercel.app"
            ]
        }
    }
)

app.register_blueprint(process_bp)
app.register_blueprint(preview_bp)
app.register_blueprint(download_bp)

@app.route("/")
def home():
    return {
        "status": "online",
        "application": "DataForge"
    }

print(app.url_map)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)