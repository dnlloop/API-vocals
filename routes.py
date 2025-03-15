from flask import Blueprint, request, jsonify
from models import db, EducationalText

bp = Blueprint("api", __name__)

@bp.route("/texts", methods=["GET"])
def get_texts():
    texts = EducationalText.query.all()
    return jsonify([{
        "id": text.id,
        "title": text.title,
        "summary": text.summary,
        "chapter": text.chapter,
        "content": text.content,
        "image": text.image,
        "audio": text.audio,
        "author": text.author,
        "author_image": text.author_image,
        "category": text.category
    } for text in texts])

@bp.route("/texts", methods=["POST"])
def add_text():
    data = request.json
    new_text = EducationalText(
        title=data["title"],
        summary=data["summary"],
        chapter=data["chapter"],
        content=data["content"],
        image=data.get("image"),
        audio=data.get("audio"),
        author=data["author"],
        author_image=data.get("author_image"),
        category=data["category"]
    )
    db.session.add(new_text)
    db.session.commit()
    return jsonify({"message": "متن آموزشی اضافه شد!"}), 201
