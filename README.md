# MEAL PLANNER CLI APPLICATION

A command-line interface (CLI) tool for planning and managing meals, built in Python
BY Mary Gichana

## Description

The Meal Planner CLI Application is a minimalist yet functional tool designed to help users organize their meals efficiently. It demonstrates key programming concepts such as working with models, file handling, and command-line interfaces in Python. Users can add, view, edit, and delete meals and meal categories.

## Features

- Add, view ,delete meals and mealcategories
- Categorize meals by meal types (e.g., Breakfast, Lunch, Dinner)
- Search functionality to find specific meals and meal categories
- User-friendly CLI interface

## How to Use

### Requirements

- A computer with Python 3.8+ installed
- Basic understanding of how to use a terminal or command line

### Installation Process

1. Clone this repository using:
   - git clone git@github.com:Mary-Gichana/Cli-Meal-planner.git
2. Navigate to the project directory:
   cd Cli-MealPlanner
3. Install the required dependencies:
   - pipenv install
   - pipenv shell
4. run the application
   python cli.py
5. Choose from the main menu
   When the application starts, you’ll see the main menu:
   ==== Meal Planner ====

   1. Manage Categories
   2. Manage Meals
   3. Exit

   ### - Input Options:

   - Enter 1 to manage meal categories.
   - Enter 2 to manage meals.
   - Enter 3 to exit the program.
     If you select Manage Categories, the following options are displayed:
     ==== Manage Meal Categories ====

   1. Add Category
   2. Delete Category
   3. List Categories
   4. Find Category by ID
   5. Go Back

   - Input Options

   1. Add Category:
      Input the category name to create a new meal category.
   2. Delete Category:
      Enter the name of the category to delete it from the list.
   3. List Categories:
      Displays all meal categories along with their IDs.
   4. Find Category by ID:
      Enter an ID to retrieve the details of the specific meal category.
   5. Go Back:
      Returns to the main menu.

   If you select Manage Meals, the following options are displayed:
   ==== Manage Meals ====

   1. Add Meal
   2. Delete Meal
   3. List Meals
   4. Find Meal by ID
   5. Go Back

   ### - Input Options:

   1. Add Meal:
      Input details such as the meal name, date, and category ID to add a new meal.
   2. Delete Meal:
      Enter the ID of the meal to remove it from the list.
   3. List Meals:
      Displays all meals along with their IDs, names, and categories.
   4. Find Meal by ID:
      Enter an ID to retrieve the details of a specific meal.
   5. Go Back:
      Returns to the main menu.

## Technologies Used

- Python 3.8+
- SQLite (for data persistence)
- CLI (Command Line Interface)
