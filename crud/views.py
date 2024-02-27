# 만들어둔 UserForm을 Import하여 사용한다.
from apps.crud.forms import UserForm
from flask import Blueprint, render_template, redirect, url_for
from apps.crud.models import User
from apps.app import db
from flask_login import login_required


# Blueprint로 crud 앱을 생성한다.
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# index 엔드 포인트를 작성하고 index.html을 반환한다.
@crud.route("/")
@login_required
def index():
    return render_template("crud/index.html")


# 새 회원을 등록하기 위한 엔드포인트(route)를 생성한다.
@crud.route("/users/new", methods=["GET","POST"])
@login_required
def create_user():
    #UserForm을 인스턴스화한다.
    form = UserForm()
    # 폼의 값을 검증한다.
    if form.validate_on_submit():
        # 사용자를 작성한다.
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # 사용자를 추가하고 커밋한다.
        db.session.add(user)
        db.session.commit()
        # 사용자의 일람 화면으로 리다이렉트 한다.
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)


# 회원들 리스트를 볼수 있는 화면을 만든다.
@crud.route("/users",methods=["GET"])
@login_required
def users():
    """사용자의 일람을 취득한다."""
    users = User.query.all()
    return render_template("crud/index.html", users=users)


# 회원정보를 수정하는 화면을 만든다. methods에 GET과 POST를 지정한다. 
@crud.route("/users/<user_id>", methods=["GET","POST"])
@login_required
def edit_user(user_id):
    form = UserForm()

    # User 모델을 이용하여 사용자를 취득한다.
    user = User.query.filter_by(id=user_id).first()

    # form으로부터 제출된 경우는 사용자를 갱신하여 사용자의 열람 화면으로 리다이렉트한다.
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit
        return redirect(url_for("crud.users"))
    
    # GET의 경우는 HTML을 반환한다.
    return render_template("crud/edit.html", user=user, form=form)


#사용자를 삭제하는 화면 만들기
@crud.route("/users/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
