import tkinter as tk
from tkinter import messagebox
import threading
import random
import time
import hashlib

# User profile dictionary to store points and recycling totals
user_profiles = {}
# Blockchain data to store recycling activities
blockchain = []
# Inventory for gift cards
user_inventory = []

# Function to simulate getting the current bin level from a sensor
def get_current_level():
    return random.randint(0, 100)

# Function to simulate scanning the type of plastic
def scan_plastic():
    plastic_types = ["PET", "HDPE", "PVC", "LDPE", "PP", "PS", "Other"]
    return random.choice(plastic_types)

# Function to simulate sending data to a server
def send_data_to_server(current_level, plastic_type):
    print(f"Server: Bin Level: {current_level}%, Plastic Type: {plastic_type}")

# Function to create a new blockchain block
def create_block(data, previous_hash='0'):
    block = {
        'index': len(blockchain) + 1,
        'timestamp': str(time.strftime("%Y-%m-%d %H:%M:%S")),
        'data': data,
        'previous_hash': previous_hash,
        'hash': ''
    }
    # Calculate the hash of the block
    block['hash'] = hashlib.sha256(str(block).encode()).hexdigest()
    # Add the block to the blockchain
    blockchain.append(block)
    return block

# Function to record recycling data in the blockchain
def record_recycling_data(data):
    if 'plastic_type' in data:
        previous_hash = blockchain[-1]['hash'] if blockchain else '0'
        block = create_block(data, previous_hash)
        print(f"Recorded on blockchain: {block}")
    else:
        print("Error: 'plastic_type' key is missing in data")

# Function to simulate getting the next plastic item on the conveyor belt
def get_next_item():
    items = ["bottle", "bag", "container", "wrapper"]
    return random.choice(items)

# Function to simulate identifying the type of plastic
def identify_plastic(item):
    plastic_types = ["PET", "HDPE", "PVC", "LDPE", "PP", "PS", "Other"]
    return random.choice(plastic_types)

# Function to simulate sorting the plastic item
def sort_item(item, plastic_type):
    print(f"Sorted {item} as {plastic_type}")

# Function to simulate collecting plastic waste
def collect_plastic_waste():
    print("Plastic waste collected")

# Function to simulate upcycling the plastic waste
def upcycle(plastic):
    return f"upcycled_{plastic}"

# Function to conduct an upcycling workshop
def conduct_upcycling_workshop():
    plastic = "plastic_bottle"
    upcycled_product = upcycle(plastic)
    print(f"Upcycled product: {upcycled_product}")

# Function to create a new frame to display the recycling guide
def display_recycling_guide(root):
    guide_frame = tk.Frame(root, bg="green")
    guide_frame.pack(fill="both", expand=True)
    
    guide_text = ("Know the Plastic Number: Look for the recycling symbol on plastic products. "
                  "The number inside the triangle of arrows indicates the type of plastic\n\n"
                  "PET: Found in soda bottles, water bottles, and food containers. It can be recycled into fiberfill for coats, sleeping bags, and more.\n"
                  "HDPE: Used in milk jugs, laundry detergent containers, and shampoo bottles. It’s widely accepted at recycling centers and can become toys, piping, and rope.\n"
                  "PVC: Commonly used in pipes, shower curtains, and medical tubing. Recycled PVC can be used for vinyl flooring, window frames, and piping.\n"
                  "LDPE: Found in plastic bags and some food packaging. It’s recycled into items like trash can liners and outdoor furniture.\n\n"
                  "Check Local Guidelines: Verify which types of plastics your municipality’s recycling service accepts.\n"
                  "Collection and Sorting: Collect plastic materials for recycling. Once transported to a recycling facility, they are sorted based on plastic type.\n"
                  "Washing and Resizing: Plastics are washed to remove contaminants. Then, they’re resized into smaller pieces.\n"
                  "Identification and Separation: Different plastics are identified and separated. This step ensures that each type is processed correctly.\n"
                  "Compounding: Finally, plastics are compounded or processed further to create new raw material for manufacturing.\n"
                  "Go Online to find more info at https://apps.npr.org/plastics-recycling/")
    
    tk.Label(guide_frame, text=guide_text, wraplength=600, justify="left", bg="green").pack(pady=20)
    tk.Button(guide_frame, text="Back", command=lambda: switch_frame(guide_frame, root)).pack(pady=10)

# Function to create a new frame to display the collection schedule
def show_collection_schedule(root):
    schedule_frame = tk.Frame(root, bg="green")
    schedule_frame.pack(fill="both", expand=True)

    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    schedule = ' {}'.format(random.choice(days))
    tk.Label(schedule_frame, text=f"Upcoming collection day: {schedule}", bg="green").pack(pady=20)
    tk.Button(schedule_frame, text="Back", command=lambda: switch_frame(schedule_frame, root)).pack(pady=10)

# Function to create a new frame to display user rewards
def track_rewards(root, user_id):
    rewards_frame = tk.Frame(root, bg="green")
    rewards_frame.pack(fill="both", expand=True)

    rewards = user_profiles.get(user_id, {"points": 0})["points"]
    tk.Label(rewards_frame, text=f"Current rewards: {rewards}", bg="green").pack(pady=20)
    tk.Button(rewards_frame, text="Back", command=lambda: switch_frame(rewards_frame, root)).pack(pady=10)

# Function to create a new frame to log recycling activity and award points
def log_recycling_activity(root, user_id, plastic_type, is_correct):
    if is_correct:
        profile = user_profiles.setdefault(user_id, {"recycling_total": 0, "points": 0})
        profile["recycling_total"] += 1
        profile["points"] += 10
        record_recycling_data({"user_id": user_id, "plastic_type": plastic_type})
        activity_frame = tk.Frame(root, bg="green")
        activity_frame.pack(fill="both", expand=True)
        tk.Label(activity_frame, text="Recycling activity logged. Points awarded.", bg="green").pack(pady=20)
        tk.Button(activity_frame, text="Back", command=lambda: switch_frame(activity_frame, root)).pack(pady=10)
    else:
        messagebox.showwarning("Improper Recycling", "Improper recycling detected. Please follow the guidelines.")

# Function to create a new frame to view logged plastics from the blockchain
def view_logged_plastics(root):
    logs_frame = tk.Frame(root, bg="green")
    logs_frame.pack(fill="both", expand=True)

    if blockchain:
        logs = "\n".join([f"User ID: {block['data']['user_id']}, Plastic Type: {block['data']['plastic_type']}" for block in blockchain])
    else:
        logs = "No logs available."
    
    tk.Label(logs_frame, text=logs, wraplength=600, justify="left", bg="green").pack(pady=20)
    tk.Button(logs_frame, text="Back", command=lambda: switch_frame(logs_frame, root)).pack(pady=10)

# Function to create a new frame to view the user's inventory of gift cards
def view_inventory(root):
    inventory_frame = tk.Frame(root, bg="green")
    inventory_frame.pack(fill="both", expand=True)

    if user_inventory:
        inventory = "\n".join(user_inventory)
    else:
        inventory = "No items in inventory."
    
    tk.Label(inventory_frame, text=inventory, wraplength=600, justify="left", bg="green").pack(pady=20)
    tk.Button(inventory_frame, text="Back", command=lambda: switch_frame(inventory_frame, root)).pack(pady=10)

# Function to simulate buying a gift card with points
def buy_gift_card(root, amount):
    user_id = "user123"
    profile = user_profiles.setdefault(user_id, {"recycling_total": 0, "points": 0})
    if profile["points"] >= amount:
        profile["points"] -= amount
        user_inventory.append(f"${amount} Gift Card")
        purchase_frame = tk.Frame(root, bg="green")
        purchase_frame.pack(fill="both", expand=True)
        tk.Label(purchase_frame, text=f"You bought a ${amount} gift card.", bg="green").pack(pady=20)
        tk.Button(purchase_frame, text="Back", command=lambda: switch_frame(purchase_frame, root)).pack(pady=10)
    else:
        messagebox.showwarning("Purchase Failed", "Not enough points to buy this gift card.")

# Function to handle menu choices
def handle_menu_choice(root, choice):
    user_id = "user123"

    if choice == "1":
        display_recycling_guide(root)
    elif choice == "2":
        show_collection_schedule(root)
    elif choice == "3":
        track_rewards(root, user_id)
    elif choice == "4":
        plastic_type = "PET"
        is_correct = True
        log_recycling_activity(root, user_id, plastic_type, is_correct)
    elif choice == "5":
        view_logged_plastics(root)
    elif choice == "6":
        open_shop(root)
    elif choice == "7":
        view_inventory(root)
    else:
        messagebox.showerror("Invalid Choice", "Invalid choice. Please try again.")

# Function to switch between frames
def switch_frame(current_frame, root):
    current_frame.pack_forget()
    main_menu_frame.pack(fill="both", expand=True)

# Function to open the shop for buying gift cards
def open_shop(root):
    shop_frame = tk.Frame(root, bg="green")
    shop_frame.pack(fill="both", expand=True)

    tk.Label(shop_frame, text="Shop", bg="green").pack(pady=20)
    
    tk.Button(shop_frame, text="$5 Gift Card", command=lambda: buy_gift_card(root, 5), width=20, height=2).pack(pady=5)
    tk.Button(shop_frame, text="$10 Gift Card", command=lambda: buy_gift_card(root, 10), width=20, height=2).pack(pady=5)
    tk.Button(shop_frame, text="$20 Gift Card", command=lambda: buy_gift_card(root, 20), width=20, height=2).pack(pady=5)
    tk.Button(shop_frame, text="$50 Gift Card", command=lambda: buy_gift_card(root, 50), width=20, height=2).pack(pady=5)
    tk.Button(shop_frame, text="Back", command=lambda: switch_frame(shop_frame, root), width=20, height=2).pack(pady=20)

# Function to create the main window of the app
def create_main_window():
    global main_menu_frame

    root = tk.Tk()
    root.title("Recycling App")
    root.configure(bg="green")  # Set the background color to green

    main_menu_frame = tk.Frame(root, bg="green")
    main_menu_frame.pack(fill="both", expand=True)

    tk.Label(main_menu_frame, text="Recycling App Main Menu", font=("Helvetica", 16), bg="green").pack(pady=20)

    # Creating larger buttons for a more user-friendly UI
    tk.Button(main_menu_frame, text="1. Recycling Guide", command=lambda: handle_menu_choice(root, "1"), width=30, height=2).pack(pady=10)
    tk.Button(main_menu_frame, text="2. Collection Schedule", command=lambda: handle_menu_choice(root, "2"), width=30, height=2).pack(pady=10)
    tk.Button(main_menu_frame, text="3. Track Rewards", command=lambda: handle_menu_choice(root, "3"), width=30, height=2).pack(pady=10)
    tk.Button(main_menu_frame, text="4. Log Recycling Activity", command=lambda: handle_menu_choice(root, "4"), width=30, height=2).pack(pady=10)
    tk.Button(main_menu_frame, text="5. View Logged Plastics", command=lambda: handle_menu_choice(root, "5"), width=30, height=2).pack(pady=10)
    tk.Button(main_menu_frame, text="6. Shop", command=lambda: handle_menu_choice(root, "6"), width=30, height=2).pack(pady=10)
    tk.Button(main_menu_frame, text="7. View Inventory", command=lambda: handle_menu_choice(root, "7"), width=30, height=2).pack(pady=10)

    root.mainloop()

# Background process for bin monitoring
def bin_monitoring_process():
    while True:
        current_level = get_current_level()
        plastic_type = scan_plastic()

        if current_level > 75:
            send_data_to_server(current_level, plastic_type)
            print("Alert: Bin is almost full. Collection needed.")
        else:
            send_data_to_server(current_level, plastic_type)

        time.sleep(5 * 60)  # Wait 5 minutes

# Background process for sorting plant
def sorting_process():
    while True:
        item = get_next_item()
        plastic_type = identify_plastic(item)
        sort_item(item, plastic_type)
        time.sleep(1)  # Simulate time to process each item

# Background process for recording data on the blockchain
def blockchain_process():
    while True:
        data = {"user_id": "user123", "plastic_type": "PET"}
        record_recycling_data(data)
        time.sleep(5 * 60)  # Wait 5 minutes

# Background process for upcycling hub
def upcycling_hub_process():
    while True:
        collect_plastic_waste()
        conduct_upcycling_workshop()
        time.sleep(24 * 60 * 60)  # Wait 1 day

# Function to start all background processes
def start_background_processes():
    threading.Thread(target=bin_monitoring_process, daemon=True).start()
    threading.Thread(target=sorting_process, daemon=True).start()
    threading.Thread(target=blockchain_process, daemon=True).start()
    threading.Thread(target=upcycling_hub_process, daemon=True).start()

if __name__ == "__main__":
    start_background_processes()  # Start background processes
    create_main_window()  # Create and run the main GUI window
