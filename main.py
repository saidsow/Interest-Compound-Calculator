import main as st

def compound_interest(principal, rate, time, monthly_investment):
    total_amount = principal
    monthly_data = []

    for month in range(int(12 * time)):
        principal = principal + monthly_investment  # Add monthly investment to principal at the beginning of each month
        total_amount = total_amount * (1 + rate / 100 / 12) + monthly_investment
        monthly_data.append({'Month': month + 1, 'Amount': total_amount})

    # Calculate compound interest
    interest = total_amount - principal
    return interest, total_amount, monthly_data

# Streamlit app layout
st.title("Compound Interest Calculator with Monthly Investment")

# User input section
principal_amount = st.number_input("Enter the principal amount:", min_value=0.0)
interest_rate = st.number_input("Enter the annual interest rate (%):", min_value=0.0)
investment_time = st.number_input("Enter the investment time in years:", min_value=0.0)
monthly_investment = st.number_input("Enter additional monthly investment:", min_value=0.0)

# Calculate compound interest
result, total_amount, monthly_data = compound_interest(principal_amount, interest_rate, investment_time, monthly_investment)

# Display results
st.write(f"The compound interest is: {result:.2f}")
st.write(f"The total amount after {investment_time} years with monthly investment is: {total_amount:.2f}")

# Display monthly amounts in a table
st.write("Monthly Amounts:")
st.table(monthly_data)
