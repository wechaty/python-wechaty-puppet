"""
Python Wechaty - https://github.com/wechaty/python-wechaty

Authors:    Huan LI (李卓桓) <https://github.com/huan>
            Jingjing WU (吴京京) <https://github.com/wj-Mcat>

2020-now @ Copyright Wechaty

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import annotations

from wechaty_grpc.wechaty.puppet import (   # type: ignore

    # Message
    MessageType,
    MessagePayloadResponse as MessagePayload,

    # Contact
    ContactGender,
    ContactType,
    ContactPayloadResponse as ContactPayload,

    # Friendship
    FriendshipType,
    FriendshipPayloadResponse as FriendshipPayload,

    # Room
    RoomPayloadResponse as RoomPayload,
    RoomMemberPayloadResponse as RoomMemberPayload,

    # UrlLink

    # RoomInvitation
    RoomInvitationPayloadResponse as RoomInvitationPayload,

    # Image
    ImageType,

    # Event
    EventType,

    # Payload type
    PayloadType
)


__all__ = [
    'MessageType',
    'MessagePayload',

    'ContactGender',
    'ContactType',
    'ContactPayload',

    'FriendshipType',
    'FriendshipPayload',

    'RoomPayload',
    'RoomMemberPayload',

    'RoomInvitationPayload',

    'ImageType',

    'EventType',

    'PayloadType'
]
