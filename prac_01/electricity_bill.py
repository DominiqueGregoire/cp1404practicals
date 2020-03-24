
print("Electricity bill estimator")

cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
billing_period_in_days = int(input("Enter number of days in billing period: "))

estimated_bill = (cents_per_kwh * daily_use_in_kwh * billing_period_in_days) / 100

print('Estimated bill: $', format(estimated_bill, ".2f"))

# 3 tariff

print("Electricity bill estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

cents_per_kwh = int(input("Which tariff? 11 or 31: "))
daily_use_in_kwh_2 = float(input("Enter daily use in kWh: "))
billing_period_in_days_2 = int(input("Enter number of days in billing period: "))


if cents_per_kwh == 11:
    cents_per_kwh = TARIFF_11
elif cents_per_kwh == 31:
    cents_per_kwh = TARIFF_31

estimated_bill_2 = cents_per_kwh * daily_use_in_kwh_2 * billing_period_in_days_2

print("Estimated bill: $", format(estimated_bill_2, ".2f"))
