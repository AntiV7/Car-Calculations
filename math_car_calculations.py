# Link to website
website_link = "https://www.carsales.com.au/cars/details/2009-mercedes-benz-e-class-e350-avantgarde-auto-my08/OAG-AD-23285021/"

# Input Variables
car_price = 14950  # 2009 Mercedes-Benz E-Class E350
monthly_savings = 330
initial_savings = 2500


# Option 1: Lease then buy the car
def calculate_lease(total_price, lease_payment, lease_term, residual_percentage):
    print("Option 1: Lease then buy the car")
    residual_value = total_price * residual_percentage / 100
    print(f"Residual Value = Total Price * Residual Percentage / 100")
    print(f"Residual Value = {total_price} * {residual_percentage} / 100 = {residual_value}")

    total_lease_cost = lease_payment * lease_term + residual_value
    print(f"Total Lease Cost = (Lease Payment * Lease Term) + Residual Value")
    print(f"Total Lease Cost = ({lease_payment} * {lease_term}) + {residual_value} = {total_lease_cost}\n")

    return total_lease_cost


# Option 2: Family Loan
def calculate_family_loan(total_price, deposit, interest_rate, loan_term_years):
    print("Option 2: Family Loan")
    principal = total_price - deposit
    print(f"Principal = Total Price - Deposit")
    print(f"Principal = {total_price} - {deposit} = {principal}")

    total_interest = principal * interest_rate * loan_term_years
    print(f"Total Interest = Principal * Interest Rate * Loan Term (Years)")
    print(f"Total Interest = {principal} * {interest_rate} * {loan_term_years} = {total_interest}")

    total_cost = principal + total_interest
    print(f"Total Cost = Principal + Total Interest")
    print(f"Total Cost = {principal} + {total_interest} = {total_cost}\n")

    return total_cost


# Option 3: Saving up to purchase the car
def calculate_savings_goal(initial_savings, monthly_savings, interest_rate, target_amount):
    print("Option 3: Saving up to purchase the car")
    months = 0
    current_savings = initial_savings

    while current_savings < target_amount:
        # Calculate interest for the current month
        interest = current_savings * (interest_rate / 100) / 12
        current_savings += interest + monthly_savings

        # Increment the number of months
        months += 1

    print(f"Months Needed: {months}")
    print(f"Total Savings: ${current_savings:.2f}\n")

    return months, current_savings


# Option 4: Bank Car Loan
def calculate_bank_loan(principal, interest_rate, loan_term_years, deposit=0):
    print("Option 4: Bank Car Loan")
    principal -= deposit
    print(f"Adjusted Principal = Principal - Deposit")
    print(f"Adjusted Principal = {principal} - {deposit} = {principal}")

    monthly_rate = interest_rate / 100 / 12
    print(f"Monthly Rate = Interest Rate / 100 / 12")
    print(f"Monthly Rate = {interest_rate} / 100 / 12 = {monthly_rate}")

    number_of_payments = loan_term_years * 12
    print(f"Number of Payments = Loan Term (Years) * 12")
    print(f"Number of Payments = {loan_term_years} * 12 = {number_of_payments}")

    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -number_of_payments)
    print(f"Monthly Payment = Principal * Monthly Rate / (1 - (1 + Monthly Rate) ** -Number of Payments)")
    print(
        f"Monthly Payment = {principal} * {monthly_rate} / (1 - (1 + {monthly_rate}) ** -{number_of_payments}) = {monthly_payment}")

    total_cost = monthly_payment * number_of_payments + deposit
    print(f"Total Cost = (Monthly Payment * Number of Payments) + Deposit")
    print(f"Total Cost = ({monthly_payment} * {number_of_payments}) + {deposit} = {total_cost}\n")

    return total_cost


# Calculation
print(f"Car: {website_link} (2009 Mercedes-Benz E-Class E350)\n")
lease_cost = calculate_lease(car_price, 320, 60, 10)
family_loan_cost = calculate_family_loan(car_price, initial_savings, 6, 4)
saving_months, saved_amount = calculate_savings_goal(initial_savings, monthly_savings, 6, car_price)
bank_loan_cost = calculate_bank_loan(car_price, 7, 5, initial_savings)

# Output the results
print(f"Option 1: Lease then buy the car\nTotal cost: ${lease_cost:.2f}\n")
print(f"Option 2: Family Loan\nTotal cost: ${family_loan_cost:.2f}\n")
print(f"Option 3: Saving up to purchase the car\nMonths needed: {saving_months}\nTotal savings: ${saved_amount:.2f}\n")
print(f"Option 4: Bank Car Loan\nTotal cost: ${bank_loan_cost:.2f}\n")

# Compare the results
costs = {
    "Lease then buy the car": lease_cost,
    "Family Loan": family_loan_cost,
    "Saving up to purchase": saved_amount,
    "Bank Car Loan": bank_loan_cost
}

best_option = min(costs, key=costs.get)

print(f"Best Option: {best_option} with a total cost of ${costs[best_option]:.2f}")
