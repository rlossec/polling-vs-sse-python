"""
Simulate user count

Every 2 seconds
- 70% of the time, the user count is incremented by a random number between -3 and +5
- 30% of the time, the user count does not change
"""

import random

MIN_USER_COUNT = 0
MAX_USER_COUNT = 200

def increment_user_count(current_user_count):
    p = random.random()
    if p < 0.7:
        new_user_count = current_user_count + random.randint(-3, 5)
        new_user_count = max(MIN_USER_COUNT, new_user_count)
        new_user_count = min(MAX_USER_COUNT, new_user_count)
        return new_user_count
    else:
        return current_user_count


