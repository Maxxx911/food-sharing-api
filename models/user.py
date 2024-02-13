from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str # TODO make hashed
    rate: int
