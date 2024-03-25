# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from front_channel_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CHANNELS_CHANNEL_ID = "/channels/{channel_id}"
    CHANNELS_CHANNEL_ID_INBOUND_MESSAGES = "/channels/{channel_id}/inbound_messages"
    CHANNELS_CHANNEL_ID_OUTBOUND_MESSAGES = "/channels/{channel_id}/outbound_messages"
