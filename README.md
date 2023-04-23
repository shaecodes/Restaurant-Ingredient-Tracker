# Restaurant-Ingredient-Tracker

The Restaurant Ingredient Tracker is a Python program that allows restaurants to manage their ingredient inventory. It provides functionalities such as restocking ingredients, checking stock levels, using ingredients, adding new ingredients, and deleting ingredients. The program also keeps a log of ingredient stock activities for record-keeping purposes.  


# Features
Restock ingredients: The program allows users to restock ingredients by specifying the amount to be added to the stock quantity. The stock quantity is automatically updated and a log is recorded.

- **Check stock levels**: Users can check the current stock quantity of ingredients. If the stock quantity falls below a threshold, a low stock alert is generated and recorded in the log.

- **Use ingredients**: The program allows users to use ingredients by specifying the amount to be used. The stock quantity is automatically updated and a log is recorded. If the stock quantity falls below a threshold after usage, a low stock alert is generated and recorded in the log.

- **Add new ingredients**: Users can add new ingredients to the inventory by providing the name, stock quantity, and threshold. The new ingredient is added to the inventory and a log is recorded.

- **Delete ingredients**: Users can delete ingredients from the inventory by providing the name. The ingredient is removed from the inventory and a log is recorded.

- **Log tracking**: The program keeps a log of all ingredient stock activities, including restocking, low stock alerts, ingredient usage, addition of new ingredients, and deletion of ingredients. The log is recorded in a separate file for easy tracking and record-keeping purposes.

# Usage
- Run the Python program ingredient.py in a Python environment.  

- Use the menu options to perform different operations on the ingredient inventory, such as restocking, checking stock levels, using ingredients, adding new ingredients, and deleting ingredients.  

- The program will automatically update the stock quantities and record logs for each activity.  

# File Descriptions  

- ingredient.py: Contains the main Python code for the Restaurant Ingredient Tracker program, including the Ingredient class and its methods for managing ingredient inventory.  

- log_file.txt: The log file that stores all ingredient stock activities in a formatted manner for easy tracking and record-keeping purposes.  

- ingredients.txt: The text file that stores the ingredient inventory, including the name, stock quantity, and threshold for each ingredient. The file is updated automatically when restocking, using, adding, or deleting ingredients.  

# Requirements
The Restaurant Ingredient Tracker program requires the following:

- Python 3.x environment  

- datetime module for date and time handling  

- os module for file handling  

# Contributions  

Contributions to the Restaurant Ingredient Tracker program are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.




