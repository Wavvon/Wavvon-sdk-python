from enum import StrEnum


class ReindexAdminSearchResponse202Status(StrEnum):
    ALREADY_RUNNING = "already_running"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
