# Example

Scratch pad for now...

```python
from pydantic import BaseModel
from pydantic.config import ConfigDict
from nptyping2 import NDArray, Shape

class MyModel(BaseModel):
    array: NDArray[Shape[1, 2, 3], int]
    model_config = ConfigDict(arbitrary_types_allowed=True)
```

Get the args...

```python
>>> array = MyModel.model_fields["array"].annotation
>>> array.shape()
(1,2,3)
>>> array.dtype()
<class 'int'>
```