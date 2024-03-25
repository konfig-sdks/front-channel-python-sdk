import typing_extensions

from front_channel_python_sdk.paths import PathValues
from front_channel_python_sdk.apis.paths.channels_channel_id import ChannelsChannelId
from front_channel_python_sdk.apis.paths.channels_channel_id_inbound_messages import ChannelsChannelIdInboundMessages
from front_channel_python_sdk.apis.paths.channels_channel_id_outbound_messages import ChannelsChannelIdOutboundMessages

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_INBOUND_MESSAGES: ChannelsChannelIdInboundMessages,
        PathValues.CHANNELS_CHANNEL_ID_OUTBOUND_MESSAGES: ChannelsChannelIdOutboundMessages,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_INBOUND_MESSAGES: ChannelsChannelIdInboundMessages,
        PathValues.CHANNELS_CHANNEL_ID_OUTBOUND_MESSAGES: ChannelsChannelIdOutboundMessages,
    }
)
