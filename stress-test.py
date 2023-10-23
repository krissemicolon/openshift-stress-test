import requests
import threading
import time
import matplotlib.pyplot as plt

TARGET_URLS = [
    "http://localhost/",
    "http://localhost/app/shop.html",
    "http://localhost/app/about_us.html",
    "http://localhost/app/cart.html"
]

TRAFFIC_PATTERN = [
    (10, 50),
    (20, 200),
    (30, 50)
]

def make_requests(url, num_requests, timings):
    for _ in range(num_requests):
        start_time = time.time()
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Error for {url} with status {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed for {url} with exception: {e}")
        end_time = time.time()

        timings.append(end_time - start_time)

def simulate_traffic(url, pattern):
    global timings
    timings = []
    for duration, users in pattern:
        threads = []
        for _ in range(users):
            thread = threading.Thread(target=make_requests, args=(url, 1, timings))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        time.sleep(duration)

    plt.plot(timings)
    plt.ylabel('Response Time (s)')
    plt.xlabel('Request Number')
    plt.title(f'Performance Analysis for {url}')
    plt.show()

if __name__ == "__main__":
    for url in TARGET_URLS:
        simulate_traffic(url, TRAFFIC_PATTERN)
