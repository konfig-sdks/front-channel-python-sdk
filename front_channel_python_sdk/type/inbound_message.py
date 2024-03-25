# coding: utf-8

"""
    Channel API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredInboundMessage(TypedDict):
    # Data of the sender
    sender: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Body of the message
    body: str

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalInboundMessage(TypedDict, total=False):
    # Subject of the message
    subject: str

    # Time in seconds at which message was created in external system
    delivered_at: int

    # Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.
    attachments: typing.List[typing.IO]

class InboundMessage(RequiredInboundMessage, OptionalInboundMessage):
    pass
