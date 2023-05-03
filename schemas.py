from pydantic import BaseModel


class ResponseModel(BaseModel):
  id: int
  name: str
  status: str
  action: str
  date: str