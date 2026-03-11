import os
from flask import Flask
from infrastructure.repositories.in_memory_task_repository import InMemoryTaskRepository
from application.services.task_service import TaskService
from controllers.task_controller import create_task_blueprint


def create_app():
    app = Flask(__name__)

    repository = InMemoryTaskRepository()
    service = TaskService(repository)

    app.register_blueprint(create_task_blueprint(service))
    return app


if __name__ == "__main__":
    app = create_app()
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
