from .task_context import TaskContext
from abc import abstractmethod
from typing import Generic, TypeVar

TaskId = int

class TaskManagers:
    """Bridge between Toolkit services and TaskContexts"""

    def __init__(self):
        self.__open_tasks: dict[TaskId, TaskContext] = {}
        self.__queued_tasks: dict[TaskId, TaskContext] = {}
        self.__closed_tasks: dict[TaskId, TaskContext] = {}

    def init_task(self, task_id: int):
        self.__open_tasks[task_id] = TaskContext(task_id)

    def close_task(self, task_id: int):
        self.__closed_tasks[task_id] = self.__open_tasks.pop(task_id)

    def load_member_tasks(self, )