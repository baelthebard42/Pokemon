from datab import myBase
from sqlalchemy.orm import Mapped, mapped_column

class Pokemons(myBase):

    __tablename__='pokes'

    id : Mapped[str] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(nullable=False)
    image : Mapped[str] = mapped_column(nullable=False)
    type : Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) :
        return f"{self.name}"
