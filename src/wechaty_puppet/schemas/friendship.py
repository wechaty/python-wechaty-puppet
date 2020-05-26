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

from dataclasses import dataclass
from typing import Optional, Union
from enum import Enum


class FriendshipType(Enum):
    Unknown = 0
    Confirm = 1
    Receive = 2
    Verify = 3

class FriendshipSceneType(Enum):
    Unknown = 0,
    QQ = 1,
    Email = 2,
    Weixin = 3,
    QQtbd = 12,
    Room = 14,
    Phone = 15,
    Card = 17,
    Location = 18,
    Bottle = 25,
    Shaking = 29,
    QRCode = 30,


@dataclass
class FriendshipPayloadBase:
    id: str
    contactId: str
    timestamp: int
    hello: Optional[str]


class FriendshipPayloadConfirm(FriendshipPayloadBase):
    type: FriendshipType.Confirm


class FriendshipPayloadReceive(FriendshipPayloadBase):
    ticket: str
    type: FriendshipType.Receive
    scene: Optional[FriendshipSceneType] = None
    stranger: Optional[str] = None


class FriendshipPayloadVerify(FriendshipPayloadBase):
    type: FriendshipType.Verify


FriendshipPayload = Union[FriendshipPayloadConfirm, FriendshipPayloadReceive, FriendshipPayloadVerify]


@dataclass
class FriendshipSearchCondition:
    phone: Optional[str]
    weixin: Optional[str]


@dataclass
class FriendshipSearchQueryFilter:
    phone: Optional[str]
    weixin: Optional[str]
