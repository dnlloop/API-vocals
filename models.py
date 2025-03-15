from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EducationalText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    chapter = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=True)  # لینک عکس
    audio = db.Column(db.String(255), nullable=True)  # لینک فایل صوتی
    author = db.Column(db.String(100), nullable=False)
    author_image = db.Column(db.String(255), nullable=True)  # عکس پروفایل نویسنده
    category = db.Column(db.String(50), nullable=False)  # (مقدماتی، متوسطه، پیشرفته)
