"""
doc
"""
from chatie_grpc.wechaty import EventType
from wechaty_puppet.puppet import (
    Puppet,
    PuppetOptions
)

from .file_box import FileBox

from .schemas.message import (
    MessageType,
    MessageQueryFilter,
    MessagePayload,
)

from .schemas.contact import (
    # Contact
    ContactGender,
    ContactType,
    ContactPayload,
    ContactQueryFilter
)

from .schemas.friendship import (
    FriendshipPayloadConfirm,
    FriendshipPayloadReceive,
    FriendshipPayloadVerify,
    FriendshipSceneType,
    FriendshipType,
    FriendshipPayload,
    FriendshipSearchQueryFilter
)

from .schemas.room import (
    # Room
    RoomPayload,
    RoomMemberPayload,
    RoomQueryFilter,
    RoomMemberQueryFilter,
)

from .schemas.url_link import UrlLinkPayload
from .schemas.room_invitation import RoomInvitationPayload
from .schemas.mini_program import MiniProgramPayload

from .schemas.event import (
    EventScanPayload,
    ScanStatus,

    EventDongPayload,
    EventLoginPayload,
    EventReadyPayload,
    EventLogoutPayload,
    EventResetPayload,

    EventRoomTopicPayload,
    EventRoomLeavePayload,
    EventRoomJoinPayload,
    EventRoomInvitePayload,

    EventMessagePayload,
    EventHeartbeatPayload,
    EventFriendshipPayload,
    EventErrorPayload
)

from .schemas.image import ImageType

__all__ = [
    'Puppet',
    'PuppetOptions',

    'ContactGender',
    'ContactPayload',
    'ContactQueryFilter',
    'ContactType',

    'FileBox',
    'FriendshipPayloadConfirm',
    'FriendshipPayloadReceive',
    'FriendshipPayloadVerify',
    'FriendshipSceneType',
    'FriendshipType',
    'FriendshipSearchQueryFilter',
    'FriendshipPayload',

    'MessagePayload',
    'MessageQueryFilter',
    'MessageType',

    'UrlLinkPayload',

    'RoomQueryFilter',
    'RoomPayload',
    'RoomMemberQueryFilter',
    'RoomMemberPayload',

    'RoomInvitationPayload',

    'MiniProgramPayload',

    'EventScanPayload',
    'ScanStatus',

    'EventDongPayload',
    'EventLoginPayload',
    'EventReadyPayload',
    'EventLogoutPayload',
    'EventResetPayload',
    'EventFriendshipPayload',
    'EventHeartbeatPayload',
    'EventMessagePayload',
    'EventRoomInvitePayload',
    'EventRoomJoinPayload',
    'EventRoomLeavePayload',
    'EventRoomTopicPayload',
    'EventErrorPayload',

    'ImageType',
    'EventType',
]
