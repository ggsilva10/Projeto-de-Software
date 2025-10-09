from flask import Blueprint, render_template, request, redirect, url_for
from .models import Habit, HabitLog
from . import db
import datetime
from flask import flash
from flask_login import login_user
from .forms import RegisterForm
from .models import User

main = Blueprint("routes", __name__)


@main.route("/")
def home():
    habits = Habit.query.all()
    logs_hoje = HabitLog.query.filter_by(data_criacao=datetime.date.today()).all()
    habitos_concluidos_hoje = {log.habit_id for log in logs_hoje}
    return render_template("index.html", habits=habits, habitos_concluidos_hoje=habitos_concluidos_hoje)

@main.route("/add_habit", methods=["POST"])
def add_habit():
    habit_name = request.form.get("habit_name")
    if habit_name:
        new_habit = Habit(nome=habit_name)
        db.session.add(new_habit)
        db.session.commit()
    return redirect(url_for("routes.home"))


@main.route("/complete_habit/<int:habit_id>")
def complete_habit(habit_id):
    log = HabitLog(habit_id=habit_id, status=True, data_criacao=datetime.date.today())
    db.session.add(log)
    db.session.commit()
    return redirect(url_for("routes.home"))

@main.route("/delete_habit/<int:habit_id>")
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
    
    if form.errors:
        for error_field, error_messages, in form.errors.items():
            for error in error_messages:
                flash(f"Erro no campo '{getattr(form, error_field).label.text}': {error}", "danger")
    
    return render_template("register.html", form=form)