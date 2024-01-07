current_age = int(input())
est_yr = 100
est_yr_days = est_yr * 365
est_yr_weeks = est_yr * 52
est_yr_months = est_yr * 12
current_yr_days = current_age * 365
current_yr_weeks = current_age * 52
current_yr_months = current_age * 12
days_left_days = est_yr_days - current_yr_days
days_left_weeks = est_yr_weeks - current_yr_weeks
days_left_months = est_yr_months - current_yr_months
days_left_years = est_yr - current_age
print(f"i have {days_left_days} days,  {days_left_weeks} weeks ,{days_left_months} months left, {days_left_years} years.")

Output:
10
i have 32850 days,  4680 weeks ,1080 months left, 90 years.
