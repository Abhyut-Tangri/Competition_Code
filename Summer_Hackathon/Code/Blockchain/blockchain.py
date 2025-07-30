import hashlib
import time

# Initialize an empty list to store the blockchain
blockchain = []

# Function to create a new block in the blockchain
def create_block(data, previous_hash='0'):
    # Create a block with the following attributes:
    block = {
        'index': len(blockchain) + 1,  # The block's index in the blockchain
        'timestamp': str(time.strftime("%Y-%m-%d %H:%M:%S")),  # The current timestamp
        'data': data,  # The data to be stored in the block
        'previous_hash': previous_hash,  # The hash of the previous block
        'hash': ''  # Placeholder for the current block's hash
    }
    # Calculate the SHA-256 hash of the block
    block['hash'] = hashlib.sha256(str(block).encode()).hexdigest()
    # Add the block to the blockchain
    blockchain.append(block)
    return block

# Function to record recycling data in the blockchain
def record_recycling_data(data):
    # Get the hash of the previous block, or '0' if this is the first block
    previous_hash = blockchain[-1]['hash'] if blockchain else '0'
    # Create a new block with the provided data and previous hash
    block = create_block(data, previous_hash)
    # Print the newly created block
    print(f"Recorded on blockchain: {block}")

# Main process for recording data on the blockchain
def blockchain_process():
    while True:
        # Example data to be recorded on the blockchain
        data = {"user_id": "user123", "data": "recycling_data"}
        # Record the data on the blockchain, only prints the data 20 times maximum per run
        for i in range(20):
            record_recycling_data(data)
            # Wait for 10 seconds  before recording the next data
            time.sleep(1 * 10)
        
        

# Entry point of the script
if __name__ == "__main__":
    # Start the blockchain recording process
    blockchain_process()
