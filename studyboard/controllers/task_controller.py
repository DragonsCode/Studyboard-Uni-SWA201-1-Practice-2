from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from domain.value_objects.task_status import TaskStatus


def create_task_blueprint(service):
    bp = Blueprint("tasks", __name__)

    @bp.get("/")
    def index():
        tasks = service.list_tasks()
        return render_template("index.html", tasks=tasks, statuses=TaskStatus)

    @bp.post("/tasks")
    def add_task():
        service.create_task(
            request.form["title"],
            request.form["description"]
        )
        return redirect(url_for("tasks.index"))

    @bp.post("/tasks/<int:task_id>/status")
    def update_status(task_id: int):
        service.change_status(
            task_id,
            TaskStatus(request.form["status"])
        )
        return redirect(url_for("tasks.index"))

    @bp.get("/api/tasks")
    def api_tasks():
        tasks = service.list_tasks()
        return jsonify([
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status.value
            }
            for task in tasks
        ])

    return bp
