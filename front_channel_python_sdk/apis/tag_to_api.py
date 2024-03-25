import typing_extensions

from front_channel_python_sdk.apis.tags import TagValues
from front_channel_python_sdk.apis.tags.messages_api import MessagesApi
from front_channel_python_sdk.apis.tags.channels_api import ChannelsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.MESSAGES: MessagesApi,
        TagValues.CHANNELS: ChannelsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.MESSAGES: MessagesApi,
        TagValues.CHANNELS: ChannelsApi,
    }
)
