from afaqy_integration.CRM import ServerTaskUnit, Prerequisites
from .helpers import avl_handler, token_manager


class DeviceContext:
    """Incomplete implementation of the DeviceContext object."""

    def __init__(self, crm_device: ServerTaskUnit, server_info: Prerequisites) -> None:
        plate = avl_handler.get_plate(server_info.target_system)
        self.crm_data = crm_device
        self.avl_data = plate.get_unit_data(
            crm_device.imei, token_manager.get_avl_token(server_info)
        )

    def add_to_server(self):
        """Adds itself to server if self.crm_data.device_added is False"""

    def check_signal(self):
        """Checks device signal"""
