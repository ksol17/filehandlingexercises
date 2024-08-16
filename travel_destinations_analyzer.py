def read_travel_experiences(filename):
    try:
        with open(filename, 'r') as file:
            travel_data = []
            for line in file:
                name, destination = line.strip().split(': ')
                destination_set = set(destination.split(', '))
                travel_data.append((name, destination_set))
            return travel_data
    except FileNotFoundError:
        []
def analyze_unique_destinations(travel_data):
    unique_destinations = set()
    for _, destination in travel_data:
        print(destination)
        unique_destinations.update(destination)
    return unique_destinations

def main():
    travel_data = read_travel_experiences('travel_experiences.txt')
    if not travel_data:
        print("No travel data available.")
        return
    
    unique_destinations = analyze_unique_destinations(travel_data)
    print("Unique Travel Destinations:")
    for destination in unique_destinations:
        print(destination)

if __name__ == "__main__":
    main()
