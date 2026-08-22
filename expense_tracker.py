import os
import json
from datetime import datetime

# ---------- variables & data types ----------
app_name = "Mini Expense Tracker"
version = 1.2
is_running = True
total_budget = 5000  # int
spent_so_far = 0.0   # float

print(f"Welcome to {app_name} (v{version})")
print("-" * 35)

# ---------- basic operators ----------
remaining = total_budget - spent_so_far
print("Budget set to:", total_budget)
print("Remaining budget:", remaining)


# ---------- class for OOP ----------
class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = datetime.now().strftime("%d-%m-%Y")

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    def summary(self):
        return f"{self.title} ({self.category}) - ₹{self.amount} on {self.date}"


# ---------- functions ----------
def save_expense(expense, filename="expenses.txt"):
    with open(filename, "a") as f:
        f.write(json.dumps(expense.to_dict()) + "\n")


def load_expenses(filename="expenses.txt"):
    if not os.path.exists(filename):
        return []
    records = []
    with open(filename, "r") as f:
        for line in f:
            records.append(json.loads(line.strip()))
    return records


def get_total(records):
    total = 0
    for r in records:
        total += r["amount"]
    return total


# ---------- lists, tuples, sets, dicts ----------
categories = ["Food", "Travel", "Shopping", "Bills", "Other"]  # list
allowed_categories = set(categories)  # set, just for quick lookup
budget_limits = {"Food": 1500, "Travel": 1000, "Shopping": 800, "Bills": 1200, "Other": 500}  # dict
sample_ranges = (0, total_budget)  # tuple, just storing min/max

print("\nAvailable categories:", categories)

# ---------- input & loop with if/elif/else ----------
expense_list = []
add_more = True

while add_more:
    title = input("\nEnter expense title (or 'done' to stop): ").strip()

    if title.lower() == "done":
        add_more = False
        break

    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (Food/Travel/Shopping/Bills/Other): ").strip().title()

        if category not in allowed_categories:
            print("Hmm, that's not a listed category, marking it as 'Other'")
            category = "Other"

        exp = Expense(title, amount, category)
        expense_list.append(exp)
        spent_so_far += amount

        # if/elif/else check against category budget
        if amount > budget_limits[category]:
            print(f"⚠️ You've crossed the usual {category} limit of ₹{budget_limits[category]}")
        elif amount == budget_limits[category]:
            print(f"You hit exactly the {category} limit, careful now")
        else:
            print("Within budget, nice.")

        save_expense(exp)

    except ValueError:
        print("That's not a valid number, try again")
    except Exception as e:
        print("Something went wrong:", e)

    another = input("Add another expense? (y/n): ").lower()
    if another != "y":
        add_more = False


# ---------- strings & string methods ----------
print("\n" + "=" * 35)
print(app_name.upper(), "- SUMMARY")
print("=" * 35)

for exp in expense_list:
    line = exp.summary()
    print(line.strip())

# ---------- reading back full history from file ----------
all_records = load_expenses()
overall_total = get_total(all_records)

print(f"\nTotal spent this session: ₹{spent_so_far}")
print(f"Total spent all-time (from file): ₹{overall_total}")
print(f"Remaining from budget: ₹{total_budget - overall_total}")

if overall_total > total_budget:
    print("You're over budget, time to cut back 😅")
else:
    print("You're doing fine, still within budget.")

print("\nThanks for using", app_name, "- see you next time!")