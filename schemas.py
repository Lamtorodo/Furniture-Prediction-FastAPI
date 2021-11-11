from fastapi import Form
from pydantic import BaseModel


# https://stackoverflow.com/a/60670614
class Furniture(BaseModel):
    category: str
    sellable_online: str
    other_colors:str
    depth:str
    height:str
    width:str

    @classmethod
    def as_form(
        cls,
        category: str = Form(...),
        sellable_online: str = Form(...),
        other_colors:str = Form(...),
        depth:str = Form(...),
        height:str = Form(...),
        width:str = Form(...),
    ):
        return cls(
            category=category,
            sellable_online= sellable_online,
            other_colors=other_colors,
            depth=depth,
            height=height,
            width=width
        )