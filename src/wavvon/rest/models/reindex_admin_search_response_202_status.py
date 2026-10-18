from enum import Enum


class ReindexAdminSearchResponse202Status(str, Enum):
    ALREADY_RUNNING = "already_running"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
