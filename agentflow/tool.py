from typing import Callable, Any
from pydantic import BaseModel, Field

class Tool(BaseModel):
    name: str
    description: str
    func: Callable[..., Any] = Field(exclude=True) # The actual Python function, excluded from serialization

    def run(self, *args, **kwargs) -> Any:
        return self.func(*args, **kwargs)
