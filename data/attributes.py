from enum import StrEnum


class TestAttributes(StrEnum):
    NAME = 'name'
    STATUS = 'status'
    FULL_NAME = 'fullName'


class TestLabels(StrEnum):
    EPIC = 'epic'
    FEATURE = 'feature'
    STORY = 'story'
    TAG = 'tag'


class TestLinks(StrEnum):
    pass
