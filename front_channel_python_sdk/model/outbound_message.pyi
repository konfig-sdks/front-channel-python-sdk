# coding: utf-8

"""
    Channel API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

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


class OutboundMessage(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Payload to receive an outbound message from an external system into Front.
    """


    class MetaOapg:
        required = {
            "metadata",
            "to",
            "body",
        }
        
        class properties:
            
            
            class to(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "handle",
                            }
                            
                            class properties:
                                name = schemas.StrSchema
                                handle = schemas.StrSchema
                                __annotations__ = {
                                    "name": name,
                                    "handle": handle,
                                }
                        
                        handle: MetaOapg.properties.handle
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "handle", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "handle", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            handle: typing.Union[MetaOapg.properties.handle, str, ],
                            name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                handle=handle,
                                name=name,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'to':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            body = schemas.StrSchema
            
            
            class metadata(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "external_conversation_id",
                        "external_id",
                    }
                    
                    class properties:
                        
                        
                        class external_id(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class external_conversation_id(
                            schemas.StrSchema
                        ):
                            pass
                        __annotations__ = {
                            "external_id": external_id,
                            "external_conversation_id": external_conversation_id,
                        }
                
                external_conversation_id: MetaOapg.properties.external_conversation_id
                external_id: MetaOapg.properties.external_id
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["external_conversation_id"]) -> MetaOapg.properties.external_conversation_id: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["external_id", "external_conversation_id", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["external_conversation_id"]) -> MetaOapg.properties.external_conversation_id: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["external_id", "external_conversation_id", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    external_conversation_id: typing.Union[MetaOapg.properties.external_conversation_id, str, ],
                    external_id: typing.Union[MetaOapg.properties.external_id, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'metadata':
                    return super().__new__(
                        cls,
                        *args,
                        external_conversation_id=external_conversation_id,
                        external_id=external_id,
                        _configuration=_configuration,
                        **kwargs,
                    )
            sender_name = schemas.StrSchema
            subject = schemas.StrSchema
            author_id = schemas.StrSchema
            delivered_at = schemas.IntSchema
            
            
            class attachments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.BinarySchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachments':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "to": to,
                "body": body,
                "metadata": metadata,
                "sender_name": sender_name,
                "subject": subject,
                "author_id": author_id,
                "delivered_at": delivered_at,
                "attachments": attachments,
            }

    
    metadata: MetaOapg.properties.metadata
    to: MetaOapg.properties.to
    body: MetaOapg.properties.body
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender_name"]) -> MetaOapg.properties.sender_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_id"]) -> MetaOapg.properties.author_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivered_at"]) -> MetaOapg.properties.delivered_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["to", "body", "metadata", "sender_name", "subject", "author_id", "delivered_at", "attachments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender_name"]) -> typing.Union[MetaOapg.properties.sender_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_id"]) -> typing.Union[MetaOapg.properties.author_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivered_at"]) -> typing.Union[MetaOapg.properties.delivered_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["to", "body", "metadata", "sender_name", "subject", "author_id", "delivered_at", "attachments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, ],
        to: typing.Union[MetaOapg.properties.to, list, tuple, ],
        body: typing.Union[MetaOapg.properties.body, str, ],
        sender_name: typing.Union[MetaOapg.properties.sender_name, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        author_id: typing.Union[MetaOapg.properties.author_id, str, schemas.Unset] = schemas.unset,
        delivered_at: typing.Union[MetaOapg.properties.delivered_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OutboundMessage':
        return super().__new__(
            cls,
            *args,
            metadata=metadata,
            to=to,
            body=body,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            delivered_at=delivered_at,
            attachments=attachments,
            _configuration=_configuration,
            **kwargs,
        )
