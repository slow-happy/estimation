from pathlib import Path
from flask import Flask, Blueprint, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager


# SQLAlchemy를 인스턴스화 한다. 
db = SQLAlchemy()
# csrf를 객체화한다.
csrf = CSRFProtect()
# LoginManager를 인스턴스화 한다.
login_manager = LoginManager()
# login_view속성에 미로그인 시 리다이렉트하는 엔드 포인트를 지정한다.
login_manager.login_view = "auth.login"
# login_message 속성에 로그인 후에 표시할 메시지를 지정한다.
# 여기에서는 아무것도 표시하지 않도록 공백을 둘 것임.
login_manager.login_message = ""

#create_app 함수를 작성한다.
def create_app(config_key):
    # 플라스크 인스턴스를 생성한다.
    app = Flask(__name__)

    # 앱의 config를 설정한다.
    app.config.from_object(config[config_key])
    csrf.init_app(app)
    # SQLAlchemy와 앱을 연게한다.
    db.init_app(app)
    # Migrate와 앱을 연계한다.
    Migrate(app, db)
    # login_manager를 앱과 연계한다.
    login_manager.init_app(app)
    # crud 패키지로부터 views를 import한다.
    from apps.crud import views as crud_views

    # register_blueprint를 사용해 views의 crud를 앱에 등록한다.
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # 이제부터 작성하는 auth 패키지로부터 views를 import한다.
    from apps.auth import views as auth_views

    # register_blueprint를 사용해 views의 auth를 앱에 등록한다.
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # estimate앱을 만들어 넣을 것 (여기서는 estimate가 아닌 내가 만들고 싶은 앱을 만들어 넣을 것)
    from apps.estimate import views as es_views

    # 이 것을 앱으로 등록시킴
    app.register_blueprint(es_views.est)

    return app
