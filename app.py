from flask import Flask, request, jsonify
from config import Config
from models import db
from routes import bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


app.register_blueprint(bp, url_prefix="/api")


texts = []
@app.route("/api/texts", methods=["POST"])
def add_texts():
    global texts
    data = request.get_json()
    if isinstance(data, list):
        texts.extend(data)  # اضافه کردن کل لیست به آرایه
    else:
        texts.append(data)  # اگر یه دونه ارسال شد
    return jsonify({"message": "Data added successfully!", "total": len(texts)}), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=10000)
