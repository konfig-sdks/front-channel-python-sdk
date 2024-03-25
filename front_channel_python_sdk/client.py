# coding: utf-8
"""
    Channel API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

import typing
import inspect
from datetime import date, datetime
from front_channel_python_sdk.client_custom import ClientCustom
from front_channel_python_sdk.configuration import Configuration
from front_channel_python_sdk.api_client import ApiClient
from front_channel_python_sdk.type_util import copy_signature
from front_channel_python_sdk.apis.tags.channels_api import ChannelsApi
from front_channel_python_sdk.apis.tags.messages_api import MessagesApi



class FrontChannel(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.channels: ChannelsApi = ChannelsApi(api_client)
        self.messages: MessagesApi = MessagesApi(api_client)
