"""
Python Wechaty - https://github.com/wechaty/python-wechaty

Authors:    Huan LI (李卓桓) <https://github.com/huan>
            Jingjing WU (吴京京) <https://github.com/wj-Mcat>

2018-now @copyright Wechaty

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import annotations

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Union


class ScanStatus(Enum):
    """
    scan status enum
    """
    Unknown = 0
    Cancel = 1
    Waiting = 2
    Scanned = 3
    Confirmed = 4
    Timeout = 5


@dataclass
class EventFriendshipPayload:
    friendship_id: str


@dataclass
class EventLoginPayload:
    contact_id: str


@dataclass
class EventLogoutPayload:
    contact_id: str
    data: str


@dataclass
class EventMessagePayload:
    message_id: str


@dataclass
class EventRoomInvitePayload:
    room_invitation_id: str


@dataclass
class EventRoomJoinPayload:
    # TODO -> discuss name style
    invited_ids: List[str]
    inviter_id: str
    room_id: str
    time_stamp: float


@dataclass
class EventRoomLeavePayload:
    # TODO -> discuss name style
    removed_ids: List[str]
    remover_id: str
    room_id: str
    time_stamp: float


@dataclass
class EventRoomTopicPayload:
    changer_id: str
    new_topic: str
    old_topic: str
    room_id: str
    time_stamp: float


@dataclass
class EventScanPayload:
    status: ScanStatus
    qrcode: Optional[str] = None
    data: Optional[str] = None


@dataclass
class EventDongPayload:
    data: Optional[str] = None


@dataclass
class EventErrorPayload:
    data: str


@dataclass
class EventReadyPayload:
    data: str


@dataclass
class EventResetPayload:
    data: str


@dataclass
class EventHeartbeatPayload:
    data: str


EventAllPayload = Union[EventDongPayload, EventErrorPayload, EventFriendshipPayload, EventHeartbeatPayload,
                        EventLoginPayload, EventLogoutPayload, EventMessagePayload, EventReadyPayload,
                        EventResetPayload, EventRoomInvitePayload, EventRoomJoinPayload, EventRoomLeavePayload,
                        EventRoomTopicPayload, EventScanPayload]
