# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PutApiV4BroadcastMessagesIdRequest(BaseModel):
    """
    PutApiV4BroadcastMessagesIdRequest
    """ # noqa: E501
    message: Optional[StrictStr] = Field(default=None, description="Message to display")
    starts_at: Optional[datetime] = Field(default=None, description="Starting time")
    ends_at: Optional[datetime] = Field(default=None, description="Ending time")
    color: Optional[StrictStr] = Field(default=None, description="Background color")
    font: Optional[StrictStr] = Field(default=None, description="Foreground color")
    target_access_levels: Optional[List[StrictInt]] = Field(default=None, description="Target user roles")
    target_path: Optional[StrictStr] = Field(default=None, description="Target path")
    broadcast_type: Optional[StrictStr] = Field(default=None, description="Broadcast Type")
    dismissable: Optional[StrictBool] = Field(default=None, description="Is dismissable")
    __properties: ClassVar[List[str]] = ["message", "starts_at", "ends_at", "color", "font", "target_access_levels", "target_path", "broadcast_type", "dismissable"]

    @field_validator('target_access_levels')
    def target_access_levels_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set([10, 20, 30, 40, 50]):
                raise ValueError("each list item must be one of (10, 20, 30, 40, 50)")
        return value

    @field_validator('broadcast_type')
    def broadcast_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['banner', 'notification']):
            raise ValueError("must be one of enum values ('banner', 'notification')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PutApiV4BroadcastMessagesIdRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PutApiV4BroadcastMessagesIdRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "starts_at": obj.get("starts_at"),
            "ends_at": obj.get("ends_at"),
            "color": obj.get("color"),
            "font": obj.get("font"),
            "target_access_levels": obj.get("target_access_levels"),
            "target_path": obj.get("target_path"),
            "broadcast_type": obj.get("broadcast_type"),
            "dismissable": obj.get("dismissable")
        })
        return _obj


