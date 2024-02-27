from pathlib import Path

basedir = Path(__file__).parent.parent

# user1 = "superpower"
# pw1 = "mecha75"
# ip1 = "192.168.0.10"
# db1 = "flask_web"
# mysql_url = f"mysql+pymysql://{user1}:{pw1}@{ip1}/{db1}?charset=utf8"


user1 = "superpower"
pw1 = "mecha75"
ip1 = "svc.sel5.cloudtype.app:31693"
db1 = "flask_web"
mysql_url = f"mysql+pymysql://{user1}:{pw1}@{ip1}/{db1}?charset=utf8"


# BaseConfig 클리스 작성하기
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBs"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"
    # 이미지 업로드 경로에 apps/images를 지정한다.
    UPLOAD_FOLDER = str(Path(basedir,"apps","uploadfiles/est"))
    UPLOAD_FOLDER_fx = str(Path(basedir,"apps","uploadfiles/fx"))

# BaseConfig 클래스를 상속하여 LocalConfig 클래스를 작성한다.
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = mysql_url
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

# BaseConfig 클래스를 상속하여 TestingConfig 클래스를 작성한다.
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = mysql_url
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

# config 사전에 매핑한다.
config = {
    "testing": TestingConfig,
    "local": LocalConfig
}