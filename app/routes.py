from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Habit, HabitLog, User
from . import db
import datetime
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm

main = Blueprint("routes", __name__)


@main.route("/")
@login_required
def home():
    habits = Habit.query.filter_by(owner_id=current_user.id).all()
    logs_hoje = HabitLog.query.filter_by(data_criacao=datetime.date.today()).all()
    habitos_concluidos_hoje = {log.habit_id for log in logs_hoje}
    return render_template("index.html", habits=habits, habitos_concluidos_hoje=habitos_concluidos_hoje)

@main.route("/add_habit", methods=["POST"])
@login_required
def add_habit():
    habit_name = request.form.get("habit_name")
    if habit_name:
        new_habit = Habit(nome=habit_name, owner_id=current_user.id)
        db.session.add(new_habit)
        db.session.commit()
    return redirect(url_for("routes.home"))


@main.route("/complete_habit/<int:habit_id>")
@login_required
def complete_habit(habit_id):
    log = HabitLog(habit_id=habit_id, status=True, data_criacao=datetime.date.today())
    db.session.add(log)
    db.session.commit()
    return redirect(url_for("routes.home"))

@main.route("/delete_habit/<int:habit_id>")
@login_required
def delete_habit(habit_id):
    habit_to_delete = Habit.query.get_or_404(habit_id)
    db.session.delete(habit_to_delete)
    db.session.commit()
    return redirect(url_for("routes.home"))

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.password = form.password.data

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash(f"Conta criada com sucesso! Você agora está logando como {new_user.username}", "success")
        return redirect(url_for("routes.home"))
    
    return render_template("register.html", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(attempted_password=form.password.data):
            login_user(user)
            flash(f"Sucesso! Você está logado como {user.username}.", "success")
            return redirect(url_for("routes.home"))
        else:
            flash("Usuário ou senha inválidos. Por favor, tente novamente.","danger")
    
    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você foi desconectado com sucesso.", "info")
    return redirect(url_for("routes.login"))