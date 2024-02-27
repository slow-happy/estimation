from datetime import datetime
from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# db.Model을 상속한 User 클래스를 작성한다.usermixin을 추가한다.
class User(db.Model, UserMixin):
    # 테이블명을 지정한다.
    __tablename__ = "users"
    # 컬럼을 정의한다. 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    auth = db.Column(db.String(20), default = "normal")
    password_hash = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # 비밀번호를 설정하기 위한 프로퍼티
    @property
    def password(self):
        raise AttributeError("읽어 들일 수 없음")
    
    # 비밀번호를 설정하기 위해 setter 함수로 해시화한 비밀번호를 설정한다.
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # 비밀번호 체크를 한다.
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 이메일 주소 중복 체크를 한다.
    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
