import sys
from datetime import datetime
from app import create_database
from models.meal import Meal
from models.mealcategory import MealCategory

create_database()

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None
def manage_categories():
    while True:
        print("\n==== Manage Meal Categories ====")
        print("1. Add Category")
        print("2. Delete Category")
        print("3. List Categories")
        print("4. Find Category by ID")
        print("5. Go Back")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter category name: ").strip()
            try:
                
                category = MealCategory(1, name)  
                print(f"Category '{category.name}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            name = input("Enter category name to delete: ").strip()
            MealCategory.delete_category(name)
            print("Category deleted.")
        elif choice == "3":
            categories = MealCategory.find_all()
            if categories:
                for category in categories:
                    category_dict = {"id": category[0], "name": category[1]}
                    print(category_dict)
            else:
                print("No categories found.")
        elif choice == "4":
            category_id = input("Enter category ID: ").strip()
            if category_id.isdigit():
                category = MealCategory.find_by_id(int(category_id))
                if category:
                    print(f"Category: {category}")
                else:
                    print("Category not found.")
            else:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def manage_meals():
     while True:
        print("\n==== Manage Meals ====")
        print("1. Add Meal")
        print("2. Delete Meal")
        print("3. List Meals")
        print("4. Find Meal by ID")
        print("5. Go Back")
        choice = input("Enter choice: ")
        if choice == "1":
           try:
            name = input("Enter meal name: ").strip()
            if not isinstance(name, str) or not name:
                    raise ValueError("Meal name must be a non-empty string.")
            date_str = input("Enter meal date (YYYY-MM-DD): ").strip()
            date = validate_date(date_str)
            if not date:
                continue
            category_name = input("Enter category name: ").strip()
            category = MealCategory.find_by_name(category_name)
            if category:
                Meal.add_meal(name, date, category[0])
                print("Meal added.")
            else:
                print("Category not found. Add the category first.")

           except ValueError as e:
                print(f"Error: {e}")
                continue
        
        elif choice == "2":
            meal_id = input("Enter meal ID to delete: ").strip()
            if meal_id.isdigit():
                Meal.delete_meal(int(meal_id))
                print("Meal deleted.")
            else:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "3":
            meals = Meal.find_all()
            if meals:
        
               meals_list = [(meal[0], meal[1], meal[2], meal[3]) for meal in meals]

               print(meals_list)
        
            else:
                print("No meals found.")
        elif choice == "4":
            meal_id = input("Enter meal ID: ").strip()
            if meal_id.isdigit():
                meal = Meal.find_by_id(int(meal_id))
                if meal:
                    print(f"Meal: {meal}")
                else:
                    print("Meal not found.")
            else:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
def main():
    while True:
        print("\n==== Meal Planner ====")
        print("1. Manage Categories")
        print("2. Manage Meals")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            manage_categories()
        elif choice == "2":
            manage_meals()
        elif choice == "3":
            print("Exiting Meal Planner. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()