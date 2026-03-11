import unittest

from application.services.task_service import TaskService
from infrastructure.repositories.in_memory_task_repository import InMemoryTaskRepository
from domain.value_objects.task_status import TaskStatus


class TaskServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryTaskRepository()
        self.service = TaskService(self.repository)

    def test_create_task(self):
        task = self.service.create_task("Prepare report", "Write architecture report")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Prepare report")
        self.assertEqual(task.status, TaskStatus.TODO)

    def test_change_status(self):
        task = self.service.create_task("Fix bugs", "Resolve critical issues")
        self.service.change_status(task.id, TaskStatus.IN_PROGRESS)
        self.service.change_status(task.id, TaskStatus.DONE)

        updated_task = self.repository.get_by_id(task.id)
        self.assertEqual(updated_task.status, TaskStatus.DONE)

    def test_empty_title_should_fail(self):
        with self.assertRaises(ValueError):
            self.service.create_task("", "Description")


if __name__ == "__main__":
    unittest.main()
