import time

while True:
    try:
        print("Press Enter To Start. CTRL + C To Stop")
        input()
        start = time.time()
        print("Started")
        while True:
            timeString = " Time: " + str(round(time.time() - start, 0)) + " secs"
            print(timeString, end='')
            time.sleep(1)
            print("\b" * len(timeString), end='', flush=True)

    except KeyboardInterrupt:
        print("\n\nStopped...")
        break