from typing import List
from dataclasses import dataclass


@dataclass
class RoomInvitationPayload:
    id: str
    inviter_id: str
    topic: str
    avatar: str
    invitation: str
    member_count: int
    member_ids: List[str]  # Friends' Contact Id List of the Room
    timestamp: int  # Unix Timestamp, in seconds or milliseconds
    receiver_id: str  # the room invitation should send to which contact.
