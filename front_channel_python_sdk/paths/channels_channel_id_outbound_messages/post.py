# coding: utf-8

"""
    Channel API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from front_channel_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from front_channel_python_sdk.api_response import AsyncGeneratorResponse
from front_channel_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from front_channel_python_sdk import schemas  # noqa: F401

from front_channel_python_sdk.model.messages_import_received_message_response import MessagesImportReceivedMessageResponse as MessagesImportReceivedMessageResponseSchema
from front_channel_python_sdk.model.outbound_message import OutboundMessage as OutboundMessageSchema

from front_channel_python_sdk.type.outbound_message import OutboundMessage
from front_channel_python_sdk.type.messages_import_received_message_response import MessagesImportReceivedMessageResponse

from ...api_client import Dictionary
from front_channel_python_sdk.pydantic.outbound_message import OutboundMessage as OutboundMessagePydantic
from front_channel_python_sdk.pydantic.messages_import_received_message_response import MessagesImportReceivedMessageResponse as MessagesImportReceivedMessageResponsePydantic

from . import path

# Path params
ChannelIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'channel_id': typing.Union[ChannelIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_channel_id = api_client.PathParameter(
    name="channel_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ChannelIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = OutboundMessageSchema


request_body_outbound_message = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'http',
]
SchemaFor202ResponseBodyApplicationJson = MessagesImportReceivedMessageResponseSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: MessagesImportReceivedMessageResponse


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: MessagesImportReceivedMessageResponse


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '202': _response_for_202,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _import_synced_message_mapped_args(
        self,
        to: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
        body: str,
        metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        channel_id: str,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        delivered_at: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if sender_name is not None:
            _body["sender_name"] = sender_name
        if to is not None:
            _body["to"] = to
        if subject is not None:
            _body["subject"] = subject
        if author_id is not None:
            _body["author_id"] = author_id
        if body is not None:
            _body["body"] = body
        if metadata is not None:
            _body["metadata"] = metadata
        if delivered_at is not None:
            _body["delivered_at"] = delivered_at
        if attachments is not None:
            _body["attachments"] = attachments
        args.body = _body
        if channel_id is not None:
            _path_params["channel_id"] = channel_id
        args.path = _path_params
        return args

    async def _aimport_synced_message_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Sync outbound message
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/channels/{channel_id}/outbound_messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_outbound_message.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _import_synced_message_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Sync outbound message
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/channels/{channel_id}/outbound_messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_outbound_message.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ImportSyncedMessageRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aimport_synced_message(
        self,
        to: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
        body: str,
        metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        channel_id: str,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        delivered_at: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._import_synced_message_mapped_args(
            body=body,
            to=to,
            body=body,
            metadata=metadata,
            channel_id=channel_id,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            delivered_at=delivered_at,
            attachments=attachments,
        )
        return await self._aimport_synced_message_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def import_synced_message(
        self,
        to: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
        body: str,
        metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        channel_id: str,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        delivered_at: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._import_synced_message_mapped_args(
            body=body,
            to=to,
            body=body,
            metadata=metadata,
            channel_id=channel_id,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            delivered_at=delivered_at,
            attachments=attachments,
        )
        return self._import_synced_message_oapg(
            body=args.body,
            path_params=args.path,
        )

class ImportSyncedMessage(BaseApi):

    async def aimport_synced_message(
        self,
        to: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
        body: str,
        metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        channel_id: str,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        delivered_at: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        validate: bool = False,
        **kwargs,
    ) -> MessagesImportReceivedMessageResponsePydantic:
        raw_response = await self.raw.aimport_synced_message(
            body=body,
            to=to,
            body=body,
            metadata=metadata,
            channel_id=channel_id,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            delivered_at=delivered_at,
            attachments=attachments,
            **kwargs,
        )
        if validate:
            return MessagesImportReceivedMessageResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MessagesImportReceivedMessageResponsePydantic, raw_response.body)
    
    
    def import_synced_message(
        self,
        to: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
        body: str,
        metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        channel_id: str,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        delivered_at: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        validate: bool = False,
    ) -> MessagesImportReceivedMessageResponsePydantic:
        raw_response = self.raw.import_synced_message(
            body=body,
            to=to,
            body=body,
            metadata=metadata,
            channel_id=channel_id,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            delivered_at=delivered_at,
            attachments=attachments,
        )
        if validate:
            return MessagesImportReceivedMessageResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MessagesImportReceivedMessageResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        to: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
        body: str,
        metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        channel_id: str,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        delivered_at: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._import_synced_message_mapped_args(
            body=body,
            to=to,
            body=body,
            metadata=metadata,
            channel_id=channel_id,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            delivered_at=delivered_at,
            attachments=attachments,
        )
        return await self._aimport_synced_message_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        to: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
        body: str,
        metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        channel_id: str,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        delivered_at: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._import_synced_message_mapped_args(
            body=body,
            to=to,
            body=body,
            metadata=metadata,
            channel_id=channel_id,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            delivered_at=delivered_at,
            attachments=attachments,
        )
        return self._import_synced_message_oapg(
            body=args.body,
            path_params=args.path,
        )

