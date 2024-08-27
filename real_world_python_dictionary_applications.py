restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Task 1. Add category called "Beverages", update steak to 17.99, remove "Bruschetta"
restaurant_menu["Beverages"] = ["Soda", 1.99]
updated_steak = {"Steak": 17.99}
restaurant_menu["Main Course"].update(updated_steak)
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)