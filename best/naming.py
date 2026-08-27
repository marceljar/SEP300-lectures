# right: Uppercase
MAX_USERS = 100
DEFAULT_TIMEOUT = 30

# wrong!
maxUsers = 100
DefaultTimeout = 30

# right: snake case
def calculate_total(price, quantity):
    total_price = price * quantity
    return total_price

# wrong!
def CalculateTotal(Price, Quantity):
    TotalPrice = Price * Quantity
    return TotalPrice

# right: camel case
class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# wrong!
class user_profile:
    def __init__(self, UserName, EmailAddress):
        self.UserName = UserName   
        self.EmailAddress = EmailAddress
