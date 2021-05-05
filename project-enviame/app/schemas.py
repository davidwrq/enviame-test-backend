from typing import Any, List, Optional

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class EnterpriseBase(BaseModel):
    name: str


class EnterpriseCreate(EnterpriseBase):
    pass


class Enterprise(EnterpriseBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
