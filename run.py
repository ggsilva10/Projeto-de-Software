from app import create_app, db
from flask_migrate import Migrate
import webbrowser
from threading import Timer

app = create_app()
migrate = Migrate(app, db)


@app.cli.command("init-db")
def init_db_command():
    """Cria as tabelas do banco de dados."""
    db.create_all()
    print("Banco de dados inicializado com sucesso.")

if __name__ == "__main__":
    url_para_abrir = "http://127.0.0.1:5000/register"

    Timer(1, lambda: webbrowser.open(url_para_abrir)).start()

    app.run(debug=True, use_reloader=False)