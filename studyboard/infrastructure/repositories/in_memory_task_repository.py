from domain.entities.task import Task
from domain.repositories.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self.next_id = 1

    def add(self, task: Task) -> None:
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)

    def get_all(self) -> list[Task]:
        return self.tasks

    def get_by_id(self, task_id: int) -> "Task | None":
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task: Task) -> None:
        # Для хранения в памяти отдельная логика обновления не нужна,
        # так как объект уже хранится по ссылке.
        pass
