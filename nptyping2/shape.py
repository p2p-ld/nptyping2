from typing import Generic, TypeVarTuple

Dimensions = TypeVarTuple("Dimensions")


class Shape(Generic[*Dimensions]):
    pass
