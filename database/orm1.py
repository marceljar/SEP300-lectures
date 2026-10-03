from data import users

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, \
    mapped_column, Session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    balance: Mapped[float]


engine = create_engine("sqlite:///example.db")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    for u in users:
        session.add(
            User(
                user_id=int(u["user_id"]),
                first_name=u["first_name"],
                last_name=u["last_name"],
                balance=float(u["balance"])
            )
        )

    session.commit()