import time
import random
import tkinter as tk
from tkinter import simpledialog, messagebox

# List of possible plastic waste items
plastic_waste_items = ["plastic_bottle", "soda_can", "milk_jug", "plastic_bag", "food_container"]

# List of possible upcycled products for each plastic waste item
upcycled_products = {
    "plastic_bottle": ["flower_pot", "bird_feeder", "watering_can"],
    "soda_can": ["pen_holder", "mini_planter", "candle_holder"],
    "milk_jug": ["watering_can", "scoop", "storage_container"],
    "plastic_bag": ["woven_basket", "handbag", "wallet"],
    "food_container": ["storage_box", "seed_starter", "organizer"]
}

# Function to simulate collecting plastic waste
def collect_plastic_waste():
    """
    Simulates the collection of plastic waste by asking the user to select a type of plastic waste item.
    Returns the selected plastic waste item.
    """
    plastic = simpledialog.askstring("Input", f"Choose a plastic waste item: {', '.join(plastic_waste_items)}")
    if plastic not in plastic_waste_items:
        messagebox.showerror("Error", "Invalid plastic waste item selected.")
        return None
    print(f"Plastic waste collected: {plastic}")
    return plastic

# Function to simulate upcycling a given plastic waste item
def upcycle(plastic):
    """
    Simulates the upcycling process by asking the user to select an upcycled product for the given plastic waste item.
    Returns the selected upcycled product.
    """
    if plastic in upcycled_products:
        product = simpledialog.askstring("Input", f"Choose an upcycled product for {plastic}: {', '.join(upcycled_products[plastic])}")
        if product not in upcycled_products[plastic]:
            messagebox.showerror("Error", "Invalid upcycled product selected.")
            return None
        return product
    return "unknown_product"

# Function to conduct an upcycling workshop
def conduct_upcycling_workshop(collected_waste):
    """
    Conducts the upcycling workshop by upcycling the collected waste item.
    Returns the upcycled product.
    """
    upcycled_product = upcycle(collected_waste)
    if upcycled_product:
        print(f"Upcycled product from {collected_waste}: {upcycled_product}")
        return upcycled_product
    return None

# Function to log collected and upcycled data
def log_data(collected_waste, upcycled_product):
    """
    Logs the details of the collected and upcycled plastic waste items to a file.
    """
    with open("upcycling_log.txt", "a") as log_file:
        log_file.write(f"Collected: {collected_waste}, Upcycled: {upcycled_product}\n")

# Main process for the upcycling hub
def upcycling_hub_process():
    """
    Main loop for the upcycling hub process.
    Continuously collects plastic waste, conducts upcycling workshops, and logs the data.
    """
    while True:
        # Collect plastic waste from the user
        collected_waste = collect_plastic_waste()
        if collected_waste:
            # Conduct an upcycling workshop for the collected waste
            upcycled_product = conduct_upcycling_workshop(collected_waste)
            if upcycled_product:
                # Log the collected and upcycled data
                log_data(collected_waste, upcycled_product)
        # Simulate waiting time before the next workshop (10 seconds for demo purposes)
        time.sleep(10)

# Entry point of the script
if __name__ == "__main__":
    # Start the upcycling hub process
    upcycling_hub_process()
