from pydantic import BaseModel, ConfigDict

class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_path: str
    filetype: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
    

class DocumentUpdate(BaseModel):
    filename: str


class MessageResponse(BaseModel):
    message: str