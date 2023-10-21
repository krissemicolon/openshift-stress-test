import requests
import threading
import time

# Define target URLs
TARGET_URLS = [
    "http://localhost/",
    "http://localhost/app/shop.html",
    "http://localhost/app/about_us.html",
    "http://localhost/app/cart.html"
]

TRAFFIC_PATTERN = [
    (10, 50),  # 50 users over 10 seconds
    (20, 200), # 200 users over 20 seconds
    (30, 50)   # 50 users over 30 seconds
]

def make_requests(url, num_requests):
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Error for {url} with status {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed for {url} with exception: {e}")

def simulate_traffic(url, pattern):
    for duration, users in pattern:
        threads = []
        for _ in range(users):
            thread = threading.Thread(target=make_requests, args=(url, 1))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        time.sleep(duration)

if __name__ == "__main__":
    for url in TARGET_URLS:
        simulate_traffic(url, TRAFFIC_PATTERN)
