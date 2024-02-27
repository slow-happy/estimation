from datetime import datetime
from apps.app import db


class UserImage(db.Model):
    __tablename__ = "user_images"
    id = db.Column(db.Integer, primary_key=True)
    # user_id는 users 테이블의 id컬럼을 외부 키로 설정한다.
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    image_path = db.Column(db.String(500))
    is_deteced = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )