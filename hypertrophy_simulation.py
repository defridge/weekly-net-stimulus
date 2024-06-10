import numpy as np
import matplotlib.pyplot as plt

# Define hypertrophy gain function based on polynomial fit
def hypertrophy_gain(sets):
    a, b, c = -0.01774892, 0.31782251, 0.76738095
    return a * sets**2 + b * sets + c

# Define atrophy loss per day after the anabolic window
atrophy_loss = 0.32 / 5  # loss per day over 5 days

# Simulation function
def simulate_hypertrophy(days, workout_days, sets_per_workout):
    hypertrophy = np.zeros(days)
    
    for day in range(days):
        if day % 7 in workout_days:  # Check if it's a workout day
            hypertrophy[day] += hypertrophy_gain(sets_per_workout)
        elif day % 7 not in workout_days and day % 7 > 1:  # Atrophy days
            hypertrophy[day] -= atrophy_loss
        
        if day > 0:
            hypertrophy[day] += hypertrophy[day - 1]  # Accumulate hypertrophy
        
        # Prevent hypertrophy from going negative
        if hypertrophy[day] < 0:
            hypertrophy[day] = 0
    
    return hypertrophy

# Input parameters
days = 7  # Number of days to simulate

# Scenario 1: Input sets per workout and frequency
sets_per_workout_scenario1 = int(input("Enter the number of sets per workout for Scenario 1: "))
workout_days_scenario1 = input("Enter the workout days for Scenario 1 (comma-separated, e.g., 0,3 for Monday and Thursday): ")
workout_days_scenario1 = [int(day.strip()) for day in workout_days_scenario1.split(",")]

# Scenario 2: Input sets per workout and frequency
sets_per_workout_scenario2 = int(input("Enter the number of sets per workout for Scenario 2: "))
workout_days_scenario2 = input("Enter the workout days for Scenario 2 (comma-separated, e.g., 0 for Monday): ")
workout_days_scenario2 = [int(day.strip()) for day in workout_days_scenario2.split(",")]

# Simulate both scenarios
hypertrophy_scenario1 = simulate_hypertrophy(days, workout_days_scenario1, sets_per_workout_scenario1)
hypertrophy_scenario2 = simulate_hypertrophy(days, workout_days_scenario2, sets_per_workout_scenario2)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(hypertrophy_scenario1, label=f'{sets_per_workout_scenario1} Sets, {len(workout_days_scenario1)}x per Week')
plt.plot(hypertrophy_scenario2, label=f'{sets_per_workout_scenario2} Sets, {len(workout_days_scenario2)}x per Week')
plt.xlabel('Days')
plt.ylabel('Hypertrophy Units')
plt.title('Hypertrophy Stimulus Comparison Over 1 Week')
plt.legend()
plt.grid(True)
plt.show()
