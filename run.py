from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)


@app.cli.command("init-db")
def init_db_command():
    """Cria as tabelas do banco de dados."""
    db.create_all()
    print("Banco de dados inicializado com sucesso.")

if __name__ == "__main__":
    app.run(debug=True)