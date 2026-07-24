'''
Question 1: Sliding Window Rate Limiter
Problem Statement
You are building a rate-limiter system for an API endpoint.
Write a Python class called SlidingWindowRateLimiter that limits requests based on a sliding time window.
Requirements
•	Initialization parameters: 
o	max_requests: Maximum number of allowed requests per key within the window. 
o	window_seconds: Duration of the sliding window in seconds. 
•	Implement the method: 
allow_request(key: str) -> bool
•	Return True if the request is allowed. 
•	Return False if the rate limit is exceeded. 
•	Remove expired requests to avoid memory leaks. 
•	Ensure the implementation is thread-safe for multi-threaded environments. 


'''
import time
# Used to get the current timestamp.

import threading
# Used to make our code thread-safe.

from collections import defaultdict, deque
# defaultdict -> Automatically creates an empty deque for a new key.
# deque -> Fast insertion/removal from both ends (O(1)).


class SlidingWindowRateLimiter:

    def __init__(self, max_requests, window_seconds):
        # Maximum requests allowed in one window.
        self.max_requests = max_requests
        # Size of the sliding window (in seconds).
        self.window_seconds = window_seconds
        # Stores timestamps for every key.
        # Example:
        # {
        #   "user_1": deque([100,102,105]),
        #   "user_2": deque([99,104])
        # }
        self.requests = defaultdict(deque)
        # Lock is used so that multiple threads cannot modify
        # the shared dictionary at the same time.
        self.lock = threading.Lock()


    def allow_request(self, key: str) -> bool:
        # Get current time.
        current_time = time.monotonic()
        # Acquire the lock.
        # Only one thread can execute this block at a time.
        with self.lock:
            # Get request timestamps for this user.
            # If user doesn't exist, defaultdict creates an empty deque.
            requests_time = self.requests[key]
            # Calculate the oldest valid timestamp.
            # Any request older than this should be removed.
            window_start = current_time - self.window_seconds
            # Remove all expired requests.
            while requests_time and requests_time[0] <= window_start:
                requests_time.popleft()

            # If user has already reached the limit,
            # reject the request.
            if len(requests_time) >= self.max_requests:
                return False

            # Otherwise, store the current request timestamp.
            requests_time.append(current_time)

            # Allow the request.
            return True


# ----------------------------------------------------
# Test Case
# ----------------------------------------------------

# Allow maximum 3 requests every 10 seconds.
rate_limiter = SlidingWindowRateLimiter(
    max_requests=3,
    window_seconds=10
)

# First request
# Queue:
# user_1 -> [t1]
print(rate_limiter.allow_request("user_1"))      # True

# Second request
# Queue:
# user_1 -> [t1,t2]
print(rate_limiter.allow_request("user_1"))      # True

# Third request
# Queue:
# user_1 -> [t1,t2,t3]
print(rate_limiter.allow_request("user_1"))      # True

# Fourth request
# Queue already contains 3 requests within the last 10 seconds.
# Limit reached.
# No request is removed because 10 seconds have not passed.
print(rate_limiter.allow_request("user_1"))      # False

'''
Time Complexity: O(1) per request because every timestamp is inserted once and removed once. Worst case is O(n) when many expired requests are removed in a single call.

Space Complexity: O(k × m), where k is the number of unique users and m is the maximum requests stored per user within the sliding window.

Thread Safety: Achieved using threading.Lock().

Memory Leak Prevention: Expired timestamps are continuously removed using popleft(), so memory usage stays bounded.

'''