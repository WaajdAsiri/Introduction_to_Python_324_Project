import re
import matplotlib.pyplot as plt


def input_weather_data():
    date = input("Enter date (YYYY-MM-DD): ")
    temp = float(input("Enter temperature (°C): "))
    humidity = float(input("Enter humidity (%): "))
    rain = input("Did it rain? (yes/no): ").strip().lower()

    with open("weather_data.txt", 'a') as file:
        file.write(f"{date}, Temp: {temp}, Humidity: {humidity}, Rain: {rain}\n")
        file.flush()
    print("Weather data added.")


def load_weather_data():
    dates = []
    temps = []
    humidities = []
    rains = []

    with open("weather_data.txt", 'r') as file:
        for line in file:
            try:
                parts = line.strip().split(',')

                date = parts[0].strip()
                temp = float(parts[1].split(':')[1].strip())
                humidity = float(parts[2].split(':')[1].strip())
                rain = parts[3].split(':')[1].strip().lower()

                dates.append(date)
                temps.append(temp)
                humidities.append(humidity)
                rains.append(rain)
            except (IndexError, ValueError) as e:
                print(f"Skipping malformed line: {line.strip()}")

    return dates, temps, humidities, rains



def calculate_statistics():
    _, temps, humidities, rains = load_weather_data()

    avg_temp = sum(temps) / len(temps)
    avg_humidity = sum(humidities) / len(humidities)
    highest_temp = max(temps)
    lowest_temp = min(temps)
    rain_days = rains.count("yes")

    print("Average Temperature:", avg_temp)
    print("Average Humidity:", avg_humidity)
    print("Highest Temperature:", highest_temp)
    print("Lowest Temperature:", lowest_temp)
    print("Number of Rainy Days:", rain_days)


def visualize_weather_data():
    dates, temps, humidities, _ = load_weather_data()

    plt.plot(dates, temps, marker='o')
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.scatter(temps, humidities, color='green')
    plt.title("Temperature vs. Humidity")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Humidity (%)")
    plt.grid(True)
    plt.show()


def display_summary():
    dates, temps, humidities, rains = load_weather_data()

    print("Total Days of Weather Data:", len(dates))
    print("Average Temperature:", sum(temps) / len(temps))
    print("Average Humidity:", sum(humidities) / len(humidities))

    hottest_day = dates[temps.index(max(temps))]
    coldest_day = dates[temps.index(min(temps))]

    print("Hottest Day:", hottest_day)
    print("Coldest Day:", coldest_day)


# Menu like your grade analyzer
print("Welcome to the Weather Data Analyzer!")
while True:
    choice = input("\nChoose an option:\n"
                   "1 - Input Weather Data\n"
                   "2 - Calculate Statistics\n"
                   "3 - Visualize Weather Data\n"
                   "4 - Display Summary\n"
                   "5 - Exit\n"
                   "Enter your choice: ")

    if choice == "1":
        input_weather_data()
    elif choice == "2":
        calculate_statistics()
    elif choice == "3":
        visualize_weather_data()
    elif choice == "4":
        display_summary()
    elif choice == "5":
        print("Thanks for using the Weather Data Analyzer. Goodbye!")
        break
    else:
        print("Invalid input. Please choose a valid option.")
