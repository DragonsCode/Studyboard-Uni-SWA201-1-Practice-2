from dataclasses import dataclass
from domain.value_objects.task_status import TaskStatus


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.TODO

    def start(self) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Completed task cannot be started again")
        self.status = TaskStatus.IN_PROGRESS

    def complete(self) -> None:
        if self.status == TaskStatus.TODO:
            raise ValueError("Task must be started before completion")
        self.status = TaskStatus.DONE
