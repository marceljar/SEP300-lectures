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

with Session(engine) as session:

    print("\nAll users:")
    users = session.query(User).order_by(User.user_id).all()

    for user in users:
        print(
            user.user_id,
            user.first_name,
            user.last_name,
            user.balance
        )


    user = session.get(User, 1)

    if user is None:
        print("No user with id 1")
    else:
        print("\nInfo about first user:")
        print(
            user.user_id,
            user.first_name,
            user.last_name,
            user.balance
        )


    print("\nUsers with balance >= 100.00 "
          "(first_name, last_name, balance):")

    users = (
        session.query(User)
        .filter(User.balance >= 100.00)
        .order_by(User.balance.desc())
        .all()
    )

    for user in users:
        print(
            user.first_name,
            user.last_name,
            user.balance
        )


    user = session.get(User, 1)
    user.balance += 10.0

    user = session.get(User, 2)
    user.last_name = "Thompson"

    session.commit()


    print("\nAfter updates (Alice, Bob):")

    users = (
        session.query(User)
        .filter(User.user_id.in_([1, 2]))
        .order_by(User.user_id)
        .all()
    )

    for user in users:
        print(
            user.user_id,
            user.first_name,
            user.last_name,
            user.balance
        )


    user = session.get(User, 12)

    if user is not None:
        session.delete(user)

    users = (
        session.query(User)
        .filter(User.balance < 10.0)
        .all()
    )

    for user in users:
        session.delete(user)

    session.commit()


    print("\nRemaining users:")

    users = session.query(User).order_by(User.user_id).all()

    for user in users:
        print(
            user.user_id,
            user.first_name,
            user.last_name,
            user.balance
        )