
import time

wait_time = 1
retries = 0

while retries < 5:
    print("Retry:", retries + 1)
    print("Waiting:", wait_time, "seconds")

    time.sleep(wait_time)

    wait_time = wait_time * 2
    retries = retries + 1

print("Maximum retries reached")
