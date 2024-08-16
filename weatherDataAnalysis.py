def read_weather_data(filename):
    try:
        with open(filename, 'r') as file:
            weather_data = []
            for line in file:
                date, temp, rainfall = line.strip().split(',')
                weather_data.append({'date': date, 'temperature': float(temp), 'rainfall': float(rainfall)})
            return weather_data
    except FileNotFoundError:
        return []


def calculate_average_temperature(weather_data):
    total_temp = sum(item['temperature'] for item in weather_data)
    avg_temp = total_temp / len(weather_data)
    print(f"Average Temperature: {avg_temp:.2f}°F")

def list_significant_rainfall(weather_data, threshold):
    significant_days = [item['date'] for item in weather_data if item['rainfall'] > threshold]
    print("Days with significant rainfall:")
    for day in significant_days:
        print(day)

def analyze_temperature_trends(weather_data):
    print("Temperature Trends:")
    for i in range(1, len(weather_data)):
        temp_diff = weather_data[i]['temperature'] - weather_data[i-1]['temperature']
        trend = "increased" if temp_diff > 0 else "decreased"
        print(f"{weather_data[i]['date']}: Temperature {trend} by {abs(temp_diff):.2f}°F")


def main():
    weather_data = read_weather_data('weather_data.txt')
    if not weather_data:
        print("No weather data available.")
        return
    
    while True:
        print("\n1. Calculate Average Temperature\n2. List Days with Significant Rainfall\3. Analyze Temperature Trends\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1': 
            calculate_average_temperature(weather_data)
        elif choice == '2':
            threshold = float(input("Enter rainfall threshold (mm): "))
            list_significant_rainfall(weather_data, threshold)
        elif choice == '3':
            analyze_temperature_trends(weather_data)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()