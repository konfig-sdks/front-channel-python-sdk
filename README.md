<div align="left">

[![Visit Front](./header.png)](https://front.com)

# Front<a id="front"></a>

Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.

With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`frontchannel.channels.update_channel`](#frontchannelchannelsupdate_channel)
  * [`frontchannel.messages.import_received_message`](#frontchannelmessagesimport_received_message)
  * [`frontchannel.messages.import_synced_message`](#frontchannelmessagesimport_synced_message)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Front&serviceName=Channel&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from front_channel_python_sdk import FrontChannel, ApiException

frontchannel = FrontChannel(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Update Channel
    frontchannel.channels.update_channel(
        body=None,
        channel_id="cha_123",
        status="offline",
    )
except ApiException as e:
    print("Exception when calling ChannelsApi.update_channel: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from front_channel_python_sdk import FrontChannel, ApiException

frontchannel = FrontChannel(

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Update Channel
        await frontchannel.channels.aupdate_channel(
            body=None,
            channel_id="cha_123",
            status="offline",
        )
    except ApiException as e:
        print("Exception when calling ChannelsApi.update_channel: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from front_channel_python_sdk import FrontChannel, ApiException

frontchannel = FrontChannel(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Update Channel
    update_channel_response = frontchannel.channels.raw.update_channel(
        body=None,
        channel_id="cha_123",
        status="offline",
    )
    pprint(update_channel_response.headers)
    pprint(update_channel_response.status)
    pprint(update_channel_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ChannelsApi.update_channel: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `frontchannel.channels.update_channel`<a id="frontchannelchannelsupdate_channel"></a>

Update a channel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontchannel.channels.update_channel(
    body=None,
    channel_id="cha_123",
    status="offline",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The Channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### status: `str`<a id="status-str"></a>

Status of the channel

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateChannel`](./front_channel_python_sdk/type/update_channel.py)
Channel details

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontchannel.messages.import_received_message`<a id="frontchannelmessagesimport_received_message"></a>

Import a message that was received by the channel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_received_message_response = frontchannel.messages.import_received_message(
    body=None,
    sender={
        "handle": "handle_example",
    },
    body="string_example",
    metadata={
        "external_id": "external_id_example",
        "external_conversation_id": "external_conversation_id_example",
    },
    channel_id="cha_123",
    subject="string_example",
    delivered_at=1,
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sender: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_channel_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sender-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_channel_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Data of the sender

##### body: `str`<a id="body-str"></a>

Body of the message

##### metadata: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_channel_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_channel_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### channel_id: `str`<a id="channel_id-str"></a>

The channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### subject: `str`<a id="subject-str"></a>

Subject of the message

##### delivered_at: `int`<a id="delivered_at-int"></a>

Time in seconds at which message was created in external system

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InboundMessage`](./front_channel_python_sdk/type/inbound_message.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MessagesImportReceivedMessageResponse`](./front_channel_python_sdk/pydantic/messages_import_received_message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/inbound_messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontchannel.messages.import_synced_message`<a id="frontchannelmessagesimport_synced_message"></a>

Import a message that was sent from the channel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_synced_message_response = frontchannel.messages.import_synced_message(
    body=None,
    to=[
        {
            "handle": "handle_example",
        }
    ],
    body="string_example",
    metadata={
        "external_id": "external_id_example",
        "external_conversation_id": "external_conversation_id_example",
    },
    channel_id="cha_123",
    sender_name="string_example",
    subject="string_example",
    author_id="string_example",
    delivered_at=1,
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### to: List[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="to-listdictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Data of the message recipient

##### body: `str`<a id="body-str"></a>

Body of the message

##### metadata: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_channel_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_channel_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### channel_id: `str`<a id="channel_id-str"></a>

The channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### sender_name: `str`<a id="sender_name-str"></a>

Name of the sender

##### subject: `str`<a id="subject-str"></a>

Subject of the message

##### author_id: `str`<a id="author_id-str"></a>

ID of the teammate on behalf of whom the message is sent

##### delivered_at: `int`<a id="delivered_at-int"></a>

Time in seconds at which message was created in external system

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OutboundMessage`](./front_channel_python_sdk/type/outbound_message.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MessagesImportReceivedMessageResponse`](./front_channel_python_sdk/pydantic/messages_import_received_message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/outbound_messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
