"""Helpers for ViCare."""
from PyViCare.PyViCareHeatingDevice import HeatingDevice
from PyViCare.PyViCareUtils import PyViCareNotSupportedFeatureError
from PyViCare.PyViCareRoomControl import RoomControl

def get_unique_id(api, device_config, entity_id) -> str:
    """Return unique ID for this entity."""
    tmp_id = f"{get_unique_device_id(device_config)}-{entity_id}"
    if hasattr(api, "id"):
        return f"{tmp_id}-{api.id}"
    return tmp_id


def get_unique_device_id(device_config) -> str:
    """Return unique ID for this device."""
    return f"{device_config.getConfig().id}-{device_config.getConfig().serial}-{device_config.getConfig().device_id}"


def get_device_name(device_config) -> str:
    """Return name for this device."""
    return f"{device_config.getModel()}-{device_config.getConfig().id}-{device_config.getConfig().device_id}"

def get_circuits(vicare_api):
    """Return the list of circuits."""
    if not isinstance(vicare_api, HeatingDevice):
        return []
    try:
        return vicare_api.circuits
    except PyViCareNotSupportedFeatureError:
        return []

def get_rooms(vicare_api):
    """Return the list of circuits."""
    if not isinstance(vicare_api, RoomControl):
        return []
    try:
        return vicare_api.rooms
    except PyViCareNotSupportedFeatureError:
        return []

def get_burners(vicare_api):
    """Return the list of burners."""
    if not isinstance(vicare_api, HeatingDevice):
        return []
    try:
        return vicare_api.burners
    except PyViCareNotSupportedFeatureError:
        return []

def get_compressors(vicare_api):
    """Return the list of compressors."""
    if not isinstance(vicare_api, HeatingDevice):
        return []
    try:
        return vicare_api.compressors
    except PyViCareNotSupportedFeatureError:
        return []