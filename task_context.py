from afaqy_integration.CRM import ServerTaskLoader, ServerTask
from abc import abstractmethod
from .helpers import crm_tasks_loader, token_manager


class TaskContext:

    # TaskContext object
    # Store in memory or cache. If storage in cache, use pydantic.model_construct
    # to retreive objects and lower computation
    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        self.import_crm_data()
        self.load_crm_devices()

    def import_crm_data(self):

        task_object = crm_tasks_loader.get_task_by_id(
            self.task_id, token_manager.get_crm_token()
        )

        self.task_object = task_object
        self.type = task_object.type
        self.title = task_object.title
        self.status = task_object.status_id
        self.assignee_name = task_object.assignee
        self.assignee_id = task_object.assignee_id

    def load_crm_devices(self):
        self.devices = crm_tasks_loader.load_task_devices(
            self.task_object, token=token_manager.get_crm_token()
        )

    def 
