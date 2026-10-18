from enum import StrEnum


class ExplainUserPermissionsResponse200SourcesItemKind(StrEnum):
    ALLOW = "allow"
    BASELINE = "baseline"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
