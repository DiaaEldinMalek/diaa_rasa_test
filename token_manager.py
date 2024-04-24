from afaqy_integration.CRM import CrmToken
from afaqy_integration.AVL import SessionTokenObj


class TokenManager:
    def __init__(self) -> None:
        pass

    def get_crm_token(self) -> CrmToken:
        """Retrieve admin token for the CRM from cache or system if necessary"""
        ...
