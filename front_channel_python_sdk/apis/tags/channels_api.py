# coding: utf-8

"""
    Channel API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_channel_python_sdk.paths.channels_channel_id.patch import UpdateChannel
from front_channel_python_sdk.apis.tags.channels_api_raw import ChannelsApiRaw


class ChannelsApi(
    UpdateChannel,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChannelsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChannelsApiRaw(api_client)