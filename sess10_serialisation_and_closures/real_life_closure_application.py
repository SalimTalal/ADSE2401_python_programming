# Python file to demonstrate real life uses of closures

# 1. Closure to calculate discount at a store
def discount_calculator(discount_percentage):
    def calculate(price):
        return price * (1 - discount_percentage / 100) # or price - (price * discount_percentage / 100)
    return calculate

print(discount_calculator(100))

black_friday = discount_calculator(20)
christmas_sale = discount_calculator(30)

print(f"Normal price : Kes. 1000\nBlack Friday deal Kes. {black_friday(1000)}")
print(f"Normal price : Kes. 1000\nChristmas Sale deal Kes. {christmas_sale(1000)}")

# 2. Closure for an email template generator
def email_template(name):
    greetings = f"Dear {name}, \n"
    def format_message(body):
        return f"{greetings}{body}\nBest Regards,\n\nEdulink International College Nairobi."
    return format_message

# Use the email template closure to notify a student to collect their transcript
student_result = email_template("Abigail")
print(f"{student_result('Please come for your ADSE Diploma Certificate')}")

print("-" * 42)

# Use the email template closure to request a supplier to deliver a product
supplier_reminder = email_template("Computer Technologies Ltd.")
print(f"{supplier_reminder('Please update us on the status of 16 GB RAM modules you were to deliver')}")

# Inspect the above for __closure__
print(student_result.__closure__) # Tuple with one cell
print(student_result.__closure__[0].cell_contents) # "Dear Abigail,"

print(supplier_reminder.__closure__) # Tuple with one cell
print(supplier_reminder.__closure__[0].cell_contents) # "Dear Computer Technologies,"