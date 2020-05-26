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
from typing import Optional


@dataclass
class MiniProgramPayload:
    """
    mini_program payload
    """
    app_id: Optional[str] = None
    description: Optional[str] = None
    page_path: Optional[str] = None
    icon_url: Optional[str] = None
    share_id: Optional[str] = None
    thumb_key: Optional[str] = None
    thumb_url: Optional[str] = None
    title: Optional[str] = None
    user_name: Optional[str] = None
