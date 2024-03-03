"""Module just for testing purposes"""

from typing import Optional
from pydantic import BaseModel


class MyClass(BaseModel):
    """
    Just a foo class
    """
    a: Optional[str] = "hey!"
