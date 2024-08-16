def read_recipes(filename):
    try:
        with open(filename, 'r') as file:
            recipes = []
            for line in file:
                name, ingredient, steps = line.strip().split(';')
                recipes.append({'name': name, 'ingredients': ingredient.split(','), 'steps': steps})
            return recipes
    except FileNotFoundError:
        []

def write_recipes(filename, recipes):
    with open(filename, 'a') as file:
        last_recipe = recipes[-1]
        file.write(f"{last_recipe['name']};{','.join(last_recipe['ingredients'])};{last_recipe['steps']}\n")

def add_recipes(recipes):
    name = input("Enter recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    steps = input("Enter preparation steps: ")
    recipes.append({'name': name, 'ingredients': ingredients, 'steps': steps})

def search_by_ingredient(recipes):
    ingredient = input("Enter ingredient to search for: ")
    found_recipes = [recipe['name'] for recipe in recipes if ingredient in recipe['ingredients']]
    print("Recipes with", ingredient, ":", ', '.join(found_recipes))

def list_all_recipes(recipes):
    for recipe in recipes: 
        print(recipe['name'])





def main():
    recipes = read_recipes('recipes_collection.txt')

    while True:
        print("\n1. Add a New Recipe\n2. Search by Ingredients\n3. List All Recipes\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_recipes(recipes)
            write_recipes('recipes_collection.txt', recipes)
        elif choice == '2':
            search_by_ingredient(recipes)
        elif choice == '3':
            list_all_recipes(recipes)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
        

if __name__ == "__main__":
    main()
