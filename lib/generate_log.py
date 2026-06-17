from datetime import datetime
import os
import requests  # <-- Add this import

def generate_log(log_data, filename=None):
    # ... (your existing generate_log function code) ...
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    if filename is None:
        date_str = datetime.now().strftime('%Y%m%d')
        filename = f"log_{date_str}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename

# --- New function to fetch data from an API ---
def fetch_data():
    """Fetch a sample post from a public API."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API request failed with status code: {response.status_code}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return {}

# --- The main execution block you provided ---
if __name__ == "__main__":
    # Example 1: Generate a log from a list (your original code)
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)

    # Example 2: Fetch data from the API and log it
    post = fetch_data()
    if post:
        # Create a log entry from the fetched post title
        log_entry = [f"Fetched Post Title: {post.get('title', 'No title found')}"]
        generate_log(log_entry, "api_log.txt")  # Save to a specific file
        print("Fetched Post Title:", post.get("title", "No title found"))
    else:
        print("Could not fetch data from the API.")