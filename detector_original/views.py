from flask import (Blueprint, render_template, redirect, url_for, 
                    current_app, send_from_directory)
from apps.app import db
from apps.crud.models import User
from apps.detector.models import UserImage
import uuid
# path를 import한다.
from pathlib import Path
from apps.detector.forms import UploadImageForm
from flask_login import current_user, login_required


# dt를 블루프린트화한다.
dt = Blueprint("detector", __name__, template_folder="templates")


# dt 애플리케이션을 사용하여 앤드 포인트를 작성한다.
@dt.route("/")
def index():
    # User와 UserImage를 Join해서 이미지 열람을 취득한다.
    user_images = (
        db.session.query(User, UserImage)
        .join(UserImage)
        .filter(User.id == UserImage.user_id)
        .all()
    )
    return render_template("detector/index.html", user_images=user_images)


@dt.route("/images/<path:filename>")
def image_file(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)


@dt.route("/upload", methods=["GET","POST"])
# 로그인 필수로 한다.
@login_required
def upload_image():
    form=UploadImageForm()
    if form.validate_on_submit():
        # 업로드된 이미지 파일을 취득한다.
        file=form.image.data
        # 파일의 파일명과 확장자를 취득하고, 파일명을 uuid로 변화한다.
        ext = Path(file.filename).suffix
        image_uuid_file_name = str(uuid.uuid4()) + ext
        # 이미지를 저장한다.
        image_path = Path(current_app.config["UPLOAD_FOLDER"], image_uuid_file_name)
        file.save(image_path)

        # DB에 저정한다.
        user_image = UserImage(
            user_id=current_user.id, image_path=image_uuid_file_name
        )
        db.session.add(user_image)
        db.session.commit()

        return redirect(url_for("detector.index"))

    return render_template("detector/upload.html", form=form)
