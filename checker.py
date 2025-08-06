# checker.py

import requests  # This allows us to make HTTP requests
import time      # We'll use this to add a delay between checks

# Optional: List of websites to check. You can also expand this later. 
websites = [
	"https://www.google.com",
	"https://www.github.com",
	"https://www.titusgitari.com",
	"https://notarealsite.fake"  #This one is intentionally fake
]

# Ask the user how often to check (in seconds)
try:
	interval = int(input("How often do you want to check the sites (in seconds)? "))
except ValueError:
	print("Invalid input. Defaulting to 60 seconds.")
	interval = 60  # Default fallback


print("\nStarting updtime checks... (Press Ctrl+C to stop)\n")

while True:
	for site in websites:
		try:
			print(f"Checking {site}...")
			response = requests.get(site, timeout=5)

			# Check for successful status code
			if response.status_code == 200:
				print(f"✅ {site} is UP ({response.status_code} OK)\n")
			else:
				print(f"⚠️ {site} returned a status code: {response.status_code}\n")

		except requests.exceptions.RequestException as e:
			# This handles any kind of error (DNS failure, timeout, etc.)
			print(f"❌ {site} is DOWN. Error: {e}\n")

	# Wait for the specified interval before checking again
	time.sleep(interval)
