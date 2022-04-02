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
from dataclasses import Field, dataclass, fields, is_dataclass, field
from typing import Any, Dict, List, Optional

from wechaty_puppet.logger import get_logger
from wechaty_puppet.schemas.base import BaseDataClass

logger = get_logger("WechatyPuppet.Schemas.Event")


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


@dataclass(init=False)
class EventFriendshipPayload(BaseDataClass):
    friendship_id: str


@dataclass(init=False)
class EventLoginPayload(BaseDataClass):
    contact_id: str


@dataclass(init=False)
class EventLogoutPayload(BaseDataClass):
    contact_id: str
    data: str


@dataclass(init=False)
class EventMessagePayload(BaseDataClass):
    message_id: str
    type: Optional[str] = None
    from_id: Optional[str] = None
    filename: Optional[str] = None
    text: Optional[str] = None
    timestamp: Optional[float] = None
    room_id: Optional[str] = None
    to_id: Optional[str] = None
    mention_ids: Optional[List[str]] = None


@dataclass(init=False)
class EventRoomInvitePayload(BaseDataClass):
    room_invitation_id: str


@dataclass(init=False)
class EventRoomJoinPayload(BaseDataClass):
    # TODO -> discuss name style
    invited_ids: List[str]
    inviter_id: str
    room_id: str
    timestamp: float

@dataclass(init=False)
class EventRoomLeavePayload(BaseDataClass):
    # TODO -> discuss name style
    removed_ids: List[str]
    remover_id: str
    room_id: str
    timestamp: float


@dataclass(init=False)
class EventRoomTopicPayload(BaseDataClass):
    changer_id: str
    new_topic: str
    old_topic: str
    room_id: str
    timestamp: float


@dataclass(init=False)
class EventScanPayload(BaseDataClass):
    status: ScanStatus
    qrcode: Optional[str] = None
    data: Optional[str] = None


@dataclass(init=False)
class EventDongPayload(BaseDataClass):
    data: Optional[str] = None


@dataclass(init=False)
class EventErrorPayload(BaseDataClass):
    data: str


@dataclass(init=False)
class EventReadyPayload(BaseDataClass):
    data: str


@dataclass(init=False)
class EventResetPayload(BaseDataClass):
    data: str


@dataclass(init=False)
class EventHeartbeatPayload(BaseDataClass):
    data: str
