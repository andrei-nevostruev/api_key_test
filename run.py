"""Flask CLI/Application entry point."""
import os

from src.flask_api_tutorial import create_app, db
from src.flask_api_tutorial.models.user import User

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db, "User": User}
