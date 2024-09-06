from sqlmodel import SQLModel


class Item(SQLModel):
    phone: str
    address: str
