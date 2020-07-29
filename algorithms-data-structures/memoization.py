import time


prev_values = {}

def ultra_slow_func(param):
    if str(param) in prev_values:
        return prev_values[str(param)]
    time.sleep(3)
    new_value = param + 10
    prev_values[str(param)] = new_value
    return new_value

