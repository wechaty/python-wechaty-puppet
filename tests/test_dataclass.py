"""Unit test for dataclass initialization"""
from __future__ import annotations

from typing import List

import pytest

from wechaty_puppet.schemas.event import EventRoomTopicPayload
from wechaty_puppet.schemas.event import EventFriendshipPayload, EventResetPayload
from wechaty_puppet.schemas.contact import ContactQueryFilter
from wechaty_puppet.file_box import FileBoxOptionsUrl, FileBoxType


def test_event_friendship_payload():
    """Unit test for EventFriendshipPayload initialization"""
    payload_data = {"friendship_id": 2323, "error_field": "error_value"}
    invalid_field_names: List[str] = EventFriendshipPayload.check_fields(payload_data)
    assert len(invalid_field_names) == 1
    assert invalid_field_names[0] == 'error_field'


def test_contact_query_filter_dataclass():
    """Unit test for ContactQueryFilter initialization"""
    payload_data = {"id": "test", "name": "test", "weixin": "test", "error_field": "error_value"}
    invalid_field_names: List[str] = ContactQueryFilter.check_fields(payload_data)
    assert len(invalid_field_names) == 1

    query_filter = ContactQueryFilter(**payload_data)
    assert query_filter.id == 'test'


def test_file_box_option_url():
    """Unit test for FileBoxOptionsUrl initialization"""
    option_url_data = {"name": "test", "url": "test", "headers": {"test": "test"}}
    option_url = FileBoxOptionsUrl(**option_url_data)
    assert option_url.name == 'test'
    assert option_url.type == FileBoxType.Url

def test_value_error():
    """Unit test for ValueError initialization"""
    with pytest.raises(ValueError):
        event_reset_payload_data = {"error_field": "error_value"}
        EventResetPayload(**event_reset_payload_data)


def test_empty_field():
    """test dataclass when there is empty field in the input data"""
    kwargs = {
        'changer_id': 'wxid_gwemn8cbz51621',
        'new_topic': '小助手个人测试群',
        'old_topic': '',
        'room_id': '20019749229@chatroom',
        'timestamp': 1650525123,
    }
    payload = EventRoomTopicPayload(**kwargs)
    assert payload.old_topic == ''
