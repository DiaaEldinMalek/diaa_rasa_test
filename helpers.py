from .token_manager import TokenManager
from afaqy_integration.CRM import CrmBuilder

token_manager = TokenManager()

crm_builder = CrmBuilder(stage_mode=False)
crm_data_loader = crm_builder.get_data_loader()
crm_tasks_loader = crm_builder.get_task_loader()
