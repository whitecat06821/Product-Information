from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Product(BaseModel):
    '''Product description'''
    title: str = Field(..., description="Title of the product")
    description: str = Field(..., description="Description of the product")
    tags: List[str] = Field(default_factory=list, description="Tags for SEO")
    colors: List[str] = Field(default_factory=list, description="Primary colors of the product")