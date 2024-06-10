import numpy as np
import matplotlib.pyplot as plt

# Define hypertrophy gain function based on the provided data points
def hypertrophy_gain(sets):
    # Polynomial fit coefficients based on provided data points
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

# Function to plot hypertrophy over time
def plot_hypertrophy(sets_per_workout1, workout_days1, sets_per_workout2, workout_days2):
    days = 7  # Simulate for 1 week
    hypertrophy_scenario1 = simulate_hypertrophy(days, workout_days1, sets_per_workout1)
    hypertrophy_scenario2 = simulate_hypertrophy(days, workout_days2, sets_per_workout2)
    
    plt.figure(figsize=(12, 6))
    plt.plot(hypertrophy_scenario1, label=f'{sets_per_workout1} Sets, {len(workout_days1)}x per Week')
    plt.plot(hypertrophy_scenario2, label=f'{sets_per_workout2} Sets, {len(workout_days2)}x per Week')
    plt.xlabel('Days')
    plt.ylabel('Hypertrophy Units')
    plt.title('Hypertrophy Stimulus Comparison Over 1 Week')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
plot_hypertrophy(3, [0, 2, 4], 6, [0, 3])
