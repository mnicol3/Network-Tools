import urllib.request

print("Target Website (e.g., http://google.com):")
# You MUST type http:// or https:// for this one
target = input()

print(f"Interrogating {target}...")

try:
    # 1. Make a polite request to the server
    response = urllib.request.urlopen(target)

    # 2. Ask for the 'Headers' (The ID Cards)
    headers = response.info()

    print("-" * 30)
    print("SERVER SECRETS STOLEN:")
    print("-" * 30)

    # 3. Print the specific details
    print(f"Server Type: {headers['Server']}")
    print(f"Content Type: {headers['Content-Type']}")
    print(f"Date: {headers['Date']}")

    # 4. Sometimes they hide extra info in 'X-Powered-By'
    if headers['X-Powered-By']:
        print(f"Powered By: {headers['X-Powered-By']}")

except Exception as e:
    print("Could not steal secrets.")
    print("Error:", e)
