from mongoengine import connect, Document, IntField, \
    StringField, FloatField
from credentials import ATLAS_URI, DB_NAME, COLL_NAME

connect(db=DB_NAME, host=ATLAS_URI, alias="default")

class User(Document):
    user_id    = IntField(required=True, unique=True)
    first_name = StringField(required=True)
    last_name  = StringField(required=True)
    balance    = FloatField(required=True)

    meta = {
        "collection": COLL_NAME,
        "db_alias": "default",
        "indexes": ["user_id"],
    }

print("\nAll users:")
for u in User.objects.order_by("user_id"):
    print(u.user_id, u.first_name, u.last_name, u.balance)

u = User.objects(user_id=1).first()
#u = User.objects(first_name="Alice").first()
if u is None:
    print("No user with id 1")
else:
    print("\nInfo about first user:")
    print(f"{u.user_id} {u.first_name} \
            {u.last_name} {u.balance}")

print("\nUsers with balance >= 100")
for u in User.objects(balance__gte=100.0)\
             .order_by("-balance"):
    print(u.first_name, u.last_name, u.balance)

User.objects(user_id=1)\
    .update_one(inc__balance=10.0)
User.objects(user_id=2)\
    .update_one(set__last_name="Thompson")

print("\nAfter updates (Alice, Bob):")
for u in User.objects(user_id__in=[1, 2])\
             .order_by("user_id"):
    print(u.user_id, u.first_name, \
          u.last_name, u.balance)

User.objects(user_id=12).delete()
User.objects(balance__lt=10.0).delete()

print("\nRemaining users:")
for u in User.objects.order_by("user_id"):
    print(u.user_id, u.first_name, \
          u.last_name, u.balance)
