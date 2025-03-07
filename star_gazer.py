import json

# File to store star data
STAR_DATA_FILE = 'star_data.json'

# Function to load data from file
def load_data():
    try:
        with open(STAR_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist

# Function to save data to file
def save_data(data):
    with open(STAR_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a new star
def add_star():
    name = input("Enter the star's name: ")
    star_type = input("Enter the star's type: ")
    distance = float(input("Enter the star's distance from Earth (light years): "))
    brightness = float(input("Enter the star's brightness (lumens): "))
    size = float(input("Enter the star's size (in solar radii): "))
    
    star = {
        'name': name,
        'type': star_type,
        'distance': distance,
        'brightness': brightness,
        'size': size
    }
    
    data = load_data()
    data.append(star)
    save_data(data)
    print(f"Star {name} added successfully.")

# Function to edit a star
def edit_star():
    name = input("Enter the name of the star you want to edit: ")
    data = load_data()
    star = next((star for star in data if star['name'].lower() == name.lower()), None)
    
    if star:
        print(f"Editing {name}:")
        star['type'] = input(f"Enter the star's type ({star['type']}): ") or star['type']
        star['distance'] = float(input(f"Enter the star's distance ({star['distance']} light years): ") or star['distance'])
        star['brightness'] = float(input(f"Enter the star's brightness ({star['brightness']} lumens): ") or star['brightness'])
        star['size'] = float(input(f"Enter the star's size ({star['size']} solar radii): ") or star['size'])
        
        save_data(data)
        print(f"Star {name} updated successfully.")
    else:
        print(f"Star {name} not found.")

# Function to remove a star
def remove_star():
    name = input("Enter the name of the star you want to remove: ")
    data = load_data()
    star = next((star for star in data if star['name'].lower() == name.lower()), None)
    
    if star:
        data.remove(star)
        save_data(data)
        print(f"Star {name} removed successfully.")
    else:
        print(f"Star {name} not found.")

# Function to search for a star
def search_star():
    name = input("Enter the name of the star you want to search for: ")
    data = load_data()
    star = next((star for star in data if star['name'].lower() == name.lower()), None)
    
    if star:
        print(f"Details for {name}:")
        print(f"Type: {star['type']}")
        print(f"Distance from Earth: {star['distance']} light years")
        print(f"Brightness: {star['brightness']} lumens")
        print(f"Size: {star['size']} solar radii")
    else:
        print(f"Star {name} not found.")

# Function to display top 5 closest stars
def top_closest_stars():
    data = load_data()
    sorted_stars = sorted(data, key=lambda x: x['distance'])[:5]
    
    print("\nTop 5 Closest Stars:")
    for i, star in enumerate(sorted_stars, 1):
        print(f"{i}. {star['name']} - {star['distance']} light years")

# Function to display top 5 brightest stars
def top_brightest_stars():
    data = load_data()
    sorted_stars = sorted(data, key=lambda x: x['brightness'], reverse=True)[:5]
    
    print("\nTop 5 Brightest Stars:")
    for i, star in enumerate(sorted_stars, 1):
        print(f"{i}. {star['name']} - {star['brightness']} lumens")

# Function to display top 5 largest stars
def top_largest_stars():
    data = load_data()
    sorted_stars = sorted(data, key=lambda x: x['size'], reverse=True)[:5]
    
    print("\nTop 5 Largest Stars:")
    for i, star in enumerate(sorted_stars, 1):
        print(f"{i}. {star['name']} - {star['size']} solar radii")

# Main menu
def main_menu():
    while True:
        print("\nStar Gazer Database:")
        print("1. Add a star")
        print("2. Edit a star")
        print("3. Remove a star")
        print("4. Search for a star")
        print("5. View top 5 closest stars")
        print("6. View top 5 brightest stars")
        print("7. View top 5 largest stars")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_star()
        elif choice == '2':
            edit_star()
        elif choice == '3':
            remove_star()
        elif choice == '4':
            search_star()
        elif choice == '5':
            top_closest_stars()
        elif choice == '6':
            top_brightest_stars()
        elif choice == '7':
            top_largest_stars()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()