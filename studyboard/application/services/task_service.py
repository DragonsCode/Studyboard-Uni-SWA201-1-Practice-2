from domain.entities.task import Task
from domain.value_objects.task_status import TaskStatus


class TaskService:
    def __init__(self, repository) -> None:
        self.repository = repository

    def create_task(self, title: str, description: str) -> Task:
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(
            id=0,
            title=title.strip(),
            description=description.strip()
        )
        self.repository.add(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self.repository.get_all()

    def change_status(self, task_id: int, new_status: TaskStatus) -> Task:
        task = self.repository.get_by_id(task_id)
        if task is None:
            raise ValueError("Task not found")

        if new_status == TaskStatus.IN_PROGRESS:
            task.start()
        elif new_status == TaskStatus.DONE:
            task.complete()
        else:
            task.status = TaskStatus.TODO

        self.repository.update(task)
        return task
