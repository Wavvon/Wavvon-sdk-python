from enum import StrEnum


class CreateAllianceChannelBodyForumRemoteWrite(StrEnum):
    NONE = "none"
    POSTS_AND_REPLIES = "posts_and_replies"
    REPLIES_ONLY = "replies_only"

    def __str__(self) -> str:
        return str(self.value)
