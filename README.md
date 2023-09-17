# Complete Python Inventory System
# Inventory Management System - Documentation
# Project Description

The Inventory Management System is a Python-based application designed to manage and maintain an inventory of various types of products. The system is console-based and allows for various operations, such as adding new inventory items, updating existing listings, and generating statistics.
#Features

    Add Inventory: Allows users to add new inventory items, specifying details like product name, category, model number, and stock quantity.

    Update Listing: Enables users to update the listing links of existing inventory items.

    Print Statistics: Provides basic statistics like total number of items and total stock.

    Logging: All major actions are logged with a timestamp.

    CSV Compatibility: All data is saved and loaded from a CSV file, which ensures that the data is easily portable and editable.

    Input Validation and Sanitization: Handles special characters in CSV, and all inputs are treated as strings to prevent format errors.
#User Interaction
Main Menu

When the program starts, the user is presented with a main menu that lists the available actions:

    Add Inventory
    Update Listing
    Print Statistics
    Exit (or 'q' to quit)

The user chooses an action by entering the corresponding number.
Add Inventory

    The user is prompted to enter various details such as product name, category, model number, stock quantity, listing links, and additional notes.
    The user can choose a category from a predefined list.

Update Listing

    The user is asked to enter the name of the product for which they want to update the listings.
    After entering the name, the current listing details are displayed, and the user can enter new listing links.

Print Statistics

    The user can view statistics related to the inventory, such as total items, total stock, etc.

Logging

    Actions such as adding a new product or updating listings are logged with a timestamp. The log is stored in a file (program.log) where each log entry contains the  date and time of the action along with a description of the action taken.
    
Exiting
    
    The user can exit the program by choosing 'Exit' or by entering 'q' at the main menu.
Data Storage
    Inventory Data
    
    All inventory data is stored in a CSV file (inventory.csv). The CSV format was chosen for its simplicity and wide range of compatibility with various software. Each row in the CSV file corresponds to a single product in the inventory, and each column represents a specific attribute of the product (e.g., name, category, model number, stock, listings, notes).
    Listings

The listing links are stored as a JSON object within a CSV column. JSON is used to maintain the structure and enable future extensibility, like adding additional metadata to each listing link.

Log File

    Log details are stored in a plain text file (program.log). Each action is logged with a timestamp, allowing for easy tracking and auditing of actions performed in the system.

Input Sanitization

    To ensure that special characters like commas and quotes do not interfere with the CSV formatting, all inputs are sanitized. Special characters are appropriately escaped, and all inputs are treated as strings to maintain consistency and prevent type errors.

By combining the use of CSV for data storage, JSON for structured data within CSV, and plain text for logging, the system creates a cohesive yet modular architecture that is easy to maintain and expand.

Installation

    Clone the repository or download the source code.
    Run the Python script main.py to start the application.

Dependencies

    Python 3.x
    CSV standard library (pre-installed with Python)
    json for handling JSON data (pre-installed with Python)
