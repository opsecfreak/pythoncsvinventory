import csv
import os
import json
import datetime
from csv import DictReader

# Initialize log file
log_file_path = "program.log"

# CSV file
csv_file_path = "inventory.csv"


def initialize_csv():
    """Initialize the CSV file if it doesn't exist."""
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Product Name", "Category", "Model Number", "Stock", "Listings", "Notes"])
            log_activity("Initialized inventory.csv.")


def clear_screen():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux/OS X
        _ = os.system('clear')
        # If above doesn't work, fallback to printing newlines
    if _ != 0:
        print("\n" * 100)


def log_activity(activity):
    """Log activity with timestamp and initialize files if not found."""

    # Initialize log file if not found
    if not os.path.exists(log_file_path):
        open(log_file_path, 'w').close()
        log_activity("Initialized program.log.")

    # Initialize CSV file
    initialize_csv()

    # Log the activity
    with open(log_file_path, "a+") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {activity}\n")


# Initialize CSV if not existing
if not os.path.exists(csv_file_path):
    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Name", "Category", "Model Number", "Stock", "Listings", "Notes"])


def add_inventory():
    """Add new inventory."""
    product_name = input("Enter the product name: ")
    categories = [
        "Computers", "Servers", "Ram", "Graphics Cards", "Components",
        "Networking", "Monitors/Displays", "Accessories", "Specific Hardware"
    ]
    print("Choose a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    category_choice = input("Enter the category number: ")
    category = categories[int(category_choice) - 1]
    model_number = input("Enter the model number: ")
    stock = input("Enter the stock quantity: ")
    listing_links = input("Enter listing links separated by commas or leave blank: ")
    listings = json.dumps({'links': listing_links.split(',')}) if listing_links else ''
    notes = input("Enter any notes: ")
    notes = notes.replace('"', '""')  # Escape double quotes

    with open(csv_file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)  # Quote all fields
        writer.writerow([product_name, category, model_number, stock, listings, notes])

    log_activity(f"New product added: {product_name}, Category: {category}")
    print("Inventory updated.")


def update_listing():
    """Update product listing status."""
    product_name = input("Enter the product name to update its listing: ")
    with open(csv_file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        lines = list(reader)

    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i, row in enumerate(lines):
            if row[0] == product_name:
                print(f"Current listing details: {row[4]}")
                new_links = input("Enter new listing links separated by commas: ")
                new_listings = json.dumps({'links': new_links.split(',')})
                row[4] = new_listings
                log_activity(f"Listings updated for product: {product_name}")
                print("Listing updated.")
            writer.writerow(row)


def print_statistics():
    """Print inventory statistics."""
    with open(csv_file_path, "r") as csvfile:
        reader = DictReader(csvfile)
        lines = list(reader)

    try:
        total_products = len(lines)
        total_stock = sum(int(row.get("Stock", 0)) for row in lines)
    except KeyError as e:
        print(f"Error: {e} not found in row. Please make sure the CSV headers match.")
        return

    print(f"\nTotal number of products: {total_products}")
    print(f"Total stock quantity: {total_stock}")

    categories = {}
    for row in lines:
        category = row.get("Category", "Unknown")
        categories[category] = categories.get(category, 0) + 1

    print("\nProducts by category:")
    for cat, count in categories.items():
        print(f"{cat}: {count}")

    log_activity("Inventory statistics displayed.")


# Main loop
if __name__ == "__main__":
    while True:
        print("\n\n------------INVENTORY MENU-------------")
        print("1. Add Inventory")
        print("2. Update Listing")
        print("3. Print Statistics")
        print("q. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_inventory()
        elif choice == "2":
            update_listing()
        elif choice == "3":
            print_statistics()
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice. Please try again.")
        # Clear the screen
