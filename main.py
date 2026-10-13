import os
import time
import random
import string
import tempfile
import shutil

# --- Configuration ---
NUM_DUMMY_FILES = 10000 # Number of dummy files to create for demonstration
TARGET_FILENAME = "important_report_Q4_2023_final.docx"
TARGET_CONTENT = "This is the secret content of the important report."

def generate_random_filename(length=15):
    """Generates a random filename."""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length)) + random.choice(['.txt', '.pdf', '.docx', '.xlsx'])

def create_dummy_files(directory, num_files):
    """Creates a specified number of dummy files in a directory."""
    print(f"Creating {num_files} dummy files in {directory}...")
    # Create the target file
    target_path = os.path.join(directory, TARGET_FILENAME)
    with open(target_path, 'w') as f:
        f.write(TARGET_CONTENT)

    # Create other random files
    for _ in range(num_files - 1):
        filename = generate_random_filename()
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            f.write(f"Some random content for {filename}")
    print("Dummy files created.")

def linear_search(directory, search_filename):
    """
    Performs a linear search by iterating through every file in the directory.
    This simulates a brute-force approach, checking each item one by one.
    """
    start_time = time.perf_counter()
    found_path = None
    for root, _, files in os.walk(directory):
        for filename in files:
            # This is the 'check every file' step, typical of traditional linear search.
            if filename == search_filename: # Direct comparison
                found_path = os.path.join(root, filename)
                break
        if found_path:
            break
    end_time = time.perf_counter()
    return found_path, (end_time - start_time) * 1000 # Time in ms

def elimination_search(directory, search_filename):
    """
    Performs a faster search by first eliminating non-matching files
    based on simple, fast-to-check criteria (e.g., file extension, partial name match),
    then performing a more precise search on the reduced set.
    This demonstrates how fast search tools work by quickly discarding irrelevant items.
    """
    start_time = time.perf_counter()
    found_path = None
    
    # Step 1: Broad elimination based on easily accessible metadata (filename parts)
    # This quickly discards a large number of irrelevant files without detailed checks.
    potential_matches = []
    
    # Extract simple, fast-to-check criteria from the target filename.
    # For this demo, we use prefix and suffix as 'hints'.
    prefix_hint = search_filename.split('_')[0] # e.g., "important"
    suffix_hint = search_filename.split('.')[-1] # e.g., "docx"

    for root, _, files in os.walk(directory):
        for filename in files:
            # The 'elimination' step: quickly filter based on simple checks.
            # Files not matching these broad criteria are immediately discarded.
            if filename.startswith(prefix_hint) and filename.endswith(suffix_hint):
                potential_matches.append(os.path.join(root, filename))
    
    # Step 2: Detailed search on the much smaller set of potential matches.
    # Only a few files remain after the elimination, making this step very fast.
    for filepath in potential_matches:
        if os.path.basename(filepath) == search_filename: # Precise check
            found_path = filepath
            break
            
    end_time = time.perf_counter()
    return found_path, (end_time - start_time) * 1000 # Time in ms

def main():
    temp_dir = None
    try:
        temp_dir = tempfile.mkdtemp(prefix="file_search_demo_")
        create_dummy_files(temp_dir, NUM_DUMMY_FILES)

        print(f"\nSearching for: '{TARGET_FILENAME}'")

        # --- Linear Search ---
        print("\n--- Performing Linear Search ---")
        found_linear, time_linear = linear_search(temp_dir, TARGET_FILENAME)
        if found_linear:
            print(f"Linear Search: Found '{os.path.basename(found_linear)}' at '{found_linear}' in {time_linear:.2f} ms")
        else:
            print("Linear Search: File not found.")

        # --- Elimination Search ---
        print("\n--- Performing Elimination Search ---")
        found_elimination, time_elimination = elimination_search(temp_dir, TARGET_FILENAME)
        if found_elimination:
            print(f"Elimination Search: Found '{os.path.basename(found_elimination)}' at '{found_elimination}' in {time_elimination:.2f} ms")
        else:
            print("Elimination Search: File not found.")

        print(f"\nComparison:")
        print(f"Linear Search Time: {time_linear:.2f} ms")
        print(f"Elimination Search Time: {time_elimination:.2f} ms")
        if time_linear > 0:
            print(f"Elimination search was {time_linear / time_elimination:.2f}x faster.")

    finally:
        if temp_dir and os.path.exists(temp_dir):
            print(f"\nCleaning up temporary directory: {temp_dir}")
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
