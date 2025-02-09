from enum import StrEnum


class MainAttributes(StrEnum):
    NAME = 'name'
    STATUS = 'status'
    FULL_NAME = 'fullName'
    LABELS = 'labels'
    LINKS = 'links'
    PARAMETERS = 'parameters'


class LabelTypes(StrEnum):
    EPIC = 'epic'
    FEATURE = 'feature'
    STORY = 'story'
    TAG = 'tag'
    ID = 'as_id'


class ParametersTypes(StrEnum):
    PARAM = 'param'
    VALUE = 'value'


class Links(StrEnum):
    URL = 'url'
