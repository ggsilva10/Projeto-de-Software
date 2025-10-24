import calendar
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
    today = datetime.date.today
    user_habit_ids = {habit.id for habit in habits}
    logs_today = HabitLog.query.filter(
        HabitLog.habit_id.in_(user_habit_ids),
        HabitLog.creation_date == today()
    ).all()
    completed_habits_today = {log.habit_id for log in logs_today}
    return render_template("index.html", habits=habits, completed_habits_today=completed_habits_today)

@main.route("/add_habit", methods=["POST"])
@login_required
def add_habit():
    habit_name = request.form.get("habit_name")
    if habit_name:
        new_habit = Habit(name=habit_name, owner_id=current_user.id)
        db.session.add(new_habit)
        db.session.commit()
    return redirect(url_for("routes.home"))


@main.route("/complete_habit/<int:habit_id>")
@login_required
def complete_habit(habit_id):
    log = HabitLog(habit_id=habit_id, is_completed=True, creation_date=datetime.date.today())
    db.session.add(log)
    db.session.commit()
    return redirect(url_for("routes.home"))

@main.route("/delete_habit/<int:habit_id>")
@login_required
def delete_habit(habit_id):
    habit_to_delete = Habit.query.get_or_404(habit_id)
    if habit_to_delete.owner_id != current_user.id:
        flash("Acesso não autorizado.", "danger")
        return redirect(url_for('routes.home'))
    
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

@main.route("/habit/<int:habit_id>")
@login_required
def habit_details(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    if habit.owner_id != current_user.id:
        flash("Acesso não autorizado.", "danger")
        return redirect(url_for('routes.home'))
    
    logs = HabitLog.query.filter_by(habit_id=habit.id).order_by(HabitLog.creation_date.desc()).all()
    today = datetime.date.today()
    year = today.year
    month = today.month

    cal = calendar.Calendar()
    month_calendar = cal.monthdayscalendar(year, month)
    calendar_title = datetime.date(year, month, 1).strftime('%B de %Y').capitalize()
    current_day_number = today.day

    completed_days = {log.creation_date.day for log in logs if log.creation_date.month == month and log.creation_date.year == year}

    total_completions = len(logs)

    current_streak = 0
    all_completed_dates = {log.creation_date for log in logs}
    streak_check_days = today
    
    while streak_check_days  in all_completed_dates:
        current_streak += 1
        streak_check_days -= datetime.timedelta(days=1)
    

    return render_template("habit_details.html",
                           habit = habit,
                           logs=logs,
                           month_calendar=month_calendar,
                           completed_days=completed_days,
                           calendar_title=calendar_title,
                           current_day_number=current_day_number,
                           total_completions=total_completions,
                           current_streak=current_streak)