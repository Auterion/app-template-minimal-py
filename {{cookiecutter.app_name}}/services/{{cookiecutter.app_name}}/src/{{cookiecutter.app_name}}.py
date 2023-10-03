#!/usr/bin/env python3

import time

if __name__ == "__main__":
    # Start timer
    start_time = time.time()

    #Print the elapsed time since the App was started
    while(True):
        delta_s = int(time.time() - start_time)
        print("Running since " + str(delta_s) + " seconds.")
        time.sleep(1)
