from typing import Generic, TypeVar, _GenericAlias
from nptyping2.shape import Shape
import numpy as np
from types import MethodType

_ShapeType = TypeVar("_ShapeType", bound=Shape)
_DtypeType = TypeVar("_DtypeType", bound=np.dtype | type)


def _shape(self) -> _ShapeType:
    return self.__args__[0].__args__


def _dtype(self) -> _DtypeType:
    return self.__args__[1]


class NDArray(Generic[_ShapeType, _DtypeType]):
    shape: _ShapeType
    dtype: _DtypeType

    def __class_getitem__(cls, item):
        # Allow us to access args from within methods
        alias = _GenericAlias(origin=NDArray, args=item)
        alias.shape = MethodType(_shape, alias)
        alias.dtype = MethodType(_dtype, alias)
        return alias
