from decimal import Decimal
from sqlalchemy import create_engine, select, \
    delete, Integer, String, Numeric
from sqlalchemy.orm import DeclarativeBase, \
    Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = \
             mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = \
             mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = \
             mapped_column(String(30), nullable=False)
    balance: Mapped[Decimal] =\
             mapped_column(Numeric(10, 2), nullable=False)

engine = create_engine("sqlite:///example.db", echo=False)

with Session(engine) as session:
    print("\nAll users:")
    for u in session.scalars(select(User)\
                            .order_by(User.user_id)):
        print(u.user_id, u.first_name, \
            u.last_name, u.balance)

with Session(engine) as session:
    #row = session.get(User, 1)
    row = session.execute(select(User)\
                          .where(User.first_name == "Alice"))\
                          .scalar_one_or_none()

if row is None:
    print("No user with id 1")
else:
    print("\nInfo about first user:")
    print(f"{row.user_id} {row.first_name} \
            {row.last_name} {row.balance}")

with Session(engine) as session:
    print("\nUsers with balance >= 100")
    for u in session.scalars(select(User)\
                    .where(User.balance >= Decimal("100.00"))\
                    .order_by(User.user_id)):
        print(u.user_id, u.first_name, \
              u.last_name, u.balance)

with Session(engine) as session:
    u1 = session.get(User, 1)
    if u1:
        u1.balance += Decimal("10.00")
    u2 = session.get(User, 2)
    if u2:
        u2.last_name = "Thompson"
    session.commit()

with Session(engine) as session:
    print("\nAfter updates (Alice, Bob):")
    for u in session.scalars(
        select(User).where(User.user_id.in_([1, 2]))\
                    .order_by(User.user_id)
    ):
        print(u.user_id, u.first_name, \
              u.last_name, u.balance)

with Session(engine) as session:
    u12 = session.get(User, 12)
    if u12:
        session.delete(u12)
    session.execute(delete(User)\
                    .where(User.balance < Decimal("10.00")))
    session.commit()

with Session(engine) as session:
    print("\nRemaining users:")
    for u in session.scalars(select(User)\
                             .order_by(User.user_id)):
        print(u.user_id, u.first_name, \
              u.last_name, u.balance)
           
