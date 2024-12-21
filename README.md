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

1.  Clone this repository using:

    ```
    git clone git@github.com:Mary-Gichana/Cli-Meal-planner.git
    ```

2.  Navigate to the project directory:

    ```
    cd Cli-MealPlanner

    ```

3.  Install the required dependencies:

    ```
    pipenv install then
    pipenv shell

    ```

4.  run the application

    ```
    python cli.py

    ```

5.  Choose from the main menu
    When the application starts, you’ll see the main menu:

    ==== Meal Planner ====

        1. Manage Categories
        2. Manage Meals
        3. Exit

    Main Menu

    ==== Meal Planner ====

    1. Manage Categories - choose this if you want to manage meal categories add, delete,find meal category by id,view all meal categories.
    2. Manage Meals - choose this if you want to manage meal categories add, delete,find meal by id,view all meals.
    3. Exit - choose if you want to exit the program.

    If you select Manage Categories, the following input options are displayed:

    ==== Manage Meal Categories ====

        1. Add Category
        2. Delete Category
        3. List Categories
        4. Find Category by ID
        5. Go Back

    Manage Meal Categories Menu

    1. Add Category:select this if you want to add a meal category, you will be prompted to Enter the name of the category.
    2. Delete Category:select this if you want to delete a meal category, you will be prompted to Enter the name of the category you want to delete from the list.
    3. List Categories:select this if you want to View all existing meal categories along with their IDs.
    4. Find Category by ID:select this if you want to find a category by its id, you will be prompted to Enter a specific ID to retrieve the details of the corresponding meal category.
    5. Go Back:select this if you want to Return to the main menu.

    If you select Manage Meals, the following options are displayed:

    ==== Manage Meals ====

        1. Add Meal
        2. Delete Meal
        3. List Meals
        4. Find Meal by ID
        5. Go Back

    Manage Meals Menu

    1. Add Meal:select this if you want to add a new meal, you will be prompted to Enter the meal's name, date (in YYYY-MM-DD format), and category ID.
    2. Delete Meal:select this if you want to delete a meal, you will be prompted to Enter the name of the meal you want to remove from the list.
    3. List Meals:select this if you want to View all existing meals, including their IDs, names, dates, and associated categories.
    4. Find Meal by ID:select this if you want to find a meal by its id, you will be prompted to Enter a specific ID to retrieve the details of the corresponding meal.
    5. Go Back:select this if you want to Return to the main menu .

    If you select Exit

    - You will exit the program.

## Technologies Used

- Python 3.8+
- SQLite (for data persistence)
- CLI (Command Line Interface)

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

Email: marygichana95@gmail.com

## License

MIT License

Copyright (c) 2024 Mary Gichana

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
