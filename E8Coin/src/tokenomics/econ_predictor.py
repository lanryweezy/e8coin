import matplotlib.pyplot as plt

def predict_economy(initial_supply, halving_interval, years):
    """
    Simulates the token supply over time.
    """
    print("Predicting economy...")

    supply = initial_supply
    supplies = [supply]
    for year in range(1, years + 1):
        if year % (halving_interval / 365) == 0:
            supply /= 2
        supplies.append(supply)

    plt.plot(range(years + 1), supplies)
    plt.xlabel("Years")
    plt.ylabel("Token Supply")
    plt.title("Token Supply Over Time")
    plt.savefig("token_supply.png")

    return {"prediction": "stable"}
