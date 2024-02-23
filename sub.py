import time

for i in range(10):
    print("\033c")  # コンソールをクリア
    print("Line 1: Iteration {}".format(i))
    print("Line 2: Time {}".format(time.time()))
    time.sleep(1)
