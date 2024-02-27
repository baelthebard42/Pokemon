from pydantic import BaseModel, ConfigDict


class PokoModel(BaseModel):

    id : str
    name: str
    image : str
    type : str

    model_config=ConfigDict(
        from_attributes=True
    )