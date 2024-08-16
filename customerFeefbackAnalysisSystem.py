def read_feedback(filename):
    try:
        with open(filename, 'r') as file:
            feedback = []
            for line in file:
                name, comment = line.strip().split(',')
                feedback.append({'name': name, 'comment': comment})
            return feedback
    except FileNotFoundError:
        []

def categorize_comments(feedback):
    positive_keywords = ['good', 'excellent', 'happy', 'satisfied']
    negative_keywords = ['bad', 'poor', 'unhappy', 'disappointed']
    categorized = {'positive': [], 'negative': [], 'neutral': []}

    for item in feedback:
        comment = item['comment'].lower()
        if any(word in comment for word in positive_keywords):
            categorized['positive'].append(item)
        elif any(word in comment for word in negative_keywords):
            categorized['negative'].append(item)
        else:
            categorized['neutral'].append(item)
    return categorized


def display_categorized_feedback(categorized):
    for category, comments in categorized.items():
        print(f"\n{category.capitalize()} Feedback:")
        for item in comments:
            print(f"- {item['name']}: {item['comment']}")

def display_summary(categorized):
    print("\nFeedback Summary:")
    for category, comments in categorized.items():
        print(f"{category.capitalize()}: {len(comments)} comments")

def main():
    feedback = read_feedback('customer_feedback.txt')
    if not feedback:
        print("No feedback available.")
        return

    categorized = categorize_comments(feedback)

    while True:
        print("\n1. Display Categorized Feedback\n2. Display Summary\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_categorized_feedback(categorized)
        elif choice =='2':
            display_summary(categorized)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()