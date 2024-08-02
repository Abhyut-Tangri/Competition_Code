# main.py

from Bin_containment import bin_monitoring
from sort_plant import sort_plant
from Blockchain import blockchain
from recycling_app import Recyling_Game
from Upcycling_hub import upcycling

import subprocess


# Function to run a given Python script using subprocess
def run_script(script_name):
    try:
        # Run the script and check for errors
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        # Print an error message if the script fails
        print(f"Error running {script_name}: {e}")

# Main function to sequentially run each component's script
def main():
    # List of scripts to run sequentially
    scripts = [
        r"Hackabyte_Summer_Hackathon\Code\Bin_containment\bin_monitoring.py",  # Script for Bin Containment
        r"Hackabyte_Summer_Hackathon\Code\sort_plant\sort_plant.py",       # Script for Sort Plant
         r"Hackabyte_Summer_Hackathon\Code\Blockchain\blockchain.py", # Script for Blockchain
        r"Hackabyte_Summer_Hackathon\Code\recycling_app\Recycling_Game.py",    # Script for Recycling App
        r"Hackabyte_Summer_Hackathon\Code\Upcycling_hub\upcycling.py"     # Script for Upcycling Hub
    ]

    # Iterate over the list of scripts and run each one
    for script in scripts:
        # Ask the user whether to run the current script
        user_input = input(f"Do you want to run {script}? (yes/no): ").strip().lower()
        
        if user_input == 'yes':
            print(f"Running {script}...")  # Print a message indicating which script is being run
            run_script(script)  # Run the current script
            # Adding a delay between scripts if needed
            input("Press Enter to continue to the next script...")  # Wait for user confirmation before proceeding
        else:
            print(f"Skipping {script}.")

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the process
