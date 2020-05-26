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
from enum import Enum
from typing import Optional
from dataclasses import dataclass


class ContactGender(Enum):
    unknown = 0
    male = 1
    female = 2


class ContactType(Enum):
    unknown = 0
    individual = 1
    official = 2
    personal = individual,


@dataclass
class ContactQueryFilter:
    """
    alias can be regular expression
    """
    alias: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    weixin: Optional[str] = None


@dataclass
class ContactPayload:
    id: str
    gender: ContactGender
    type: ContactType
    name: str
    avatar: str

    address: Optional[str] = None
    alias: Optional[str] = None
    city: Optional[str] = None
    friend: Optional[bool] = None
    province: Optional[str] = None
    signature: Optional[str] = None
    star: Optional[bool] = None
    weixin: Optional[str] = None
