from enum import Enum


class ExplainUserPermissionsResponse200SourcesItemKind(str, Enum):
    ALLOW = "allow"
    BASELINE = "baseline"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
