class ShoppingCart:
    def __init__(self, customer_name, store, prices):
        self.customer_name = customer_name
        self.store = store
        self.prices = prices
        self.discount = 0.10

    def get_values(self):
        return self.prices


class TestScores:
    def __init__(self, student_name, course, scores):
        self.student_name = student_name
        self.course = course
        self.scores = scores
        self.passing_grade = 50

    def get_values(self):
        return self.scores


def sum_values(obj):
    return sum(obj.get_values())


cart = ShoppingCart(
    "Alice", 
    "Tech Store", 
    [120.00, 35.50, 80.00]
)

scores = TestScores(
    "Bob",
    "SEP300",
    [45, 72, 68, 56]
)

print(f"Cart total: {sum_values(cart)}")
print(f"Score total: {sum_values(scores)}")