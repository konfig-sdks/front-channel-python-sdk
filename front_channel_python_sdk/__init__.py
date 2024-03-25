# coding: utf-8

# flake8: noqa

"""
    Channel API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

__version__ = "1.0.0"

# import ApiClient
from front_channel_python_sdk.api_client import ApiClient

# import Configuration
from front_channel_python_sdk.configuration import Configuration

# import exceptions
from front_channel_python_sdk.exceptions import OpenApiException
from front_channel_python_sdk.exceptions import ApiAttributeError
from front_channel_python_sdk.exceptions import ApiTypeError
from front_channel_python_sdk.exceptions import ApiValueError
from front_channel_python_sdk.exceptions import ApiKeyError
from front_channel_python_sdk.exceptions import ApiException

from front_channel_python_sdk.client import FrontChannel
