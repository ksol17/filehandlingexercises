def read_attendance(filename):
    try:
        with open(filename, 'r') as file:
            attendance = {}
            for line in file:
                parts =line.strip().split(',')
                event, date = parts[0], parts[1]
                attendees = parts[2:] if len(parts) > 2 else []
                attendance[event] = {'date': date, 'attendees': attendees}
            return attendance
    except FileNotFoundError:
        {}

def write_attendance(filename, attendance):
    with open(filename, 'w') as file:
        for event, info in attendance.items():
            line = f"{event}, {info['date']},{','.join(info['attendees'])}\n"
            file.write(line)

def add_event(attendance):
    event = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    attendance[event] = {'date': date, 'attendees': []}

def register_attendee(attendance):
    event = input("Register event name: ")
    if event not in attendance:
        print("Event not found.")
    else:
        attendee = input("Enter attendee's name: ")
        attendance[event]['attendees'].append(attendee)


def generate_report(attendance):
    for event, info in attendance.items():
        print(f"\nEvent: {event} (Date: {info['date']})")
        print("Attendees:")
        for attendee in info['attendees']:
            print(f"- {attendee}")





def main():
    attendance = read_attendance('event_attendance.txt') #dictionary with nested dictionary

    while True:
        print("\n1. Add a New Event\n2. Register an Attendee\n3. Generate Attendance Report\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_event(attendance)
        elif choice == '2':
            register_attendee(attendance)
        elif choice == '3':
            generate_report(attendance)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

        write_attendance('event_attendance.txt', attendance)

if __name__ == "__main__":
    main()
