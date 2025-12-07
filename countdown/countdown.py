import sys
import time

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    count = int(user_input)
    print(f"Your input was {count}!")
    print("------------------")
    print("Starting the countdown!")
else:
    print("No input provided, default is 60")
    count = 10

increment = 0

for i in range(1, (count + 1)):
    print(i, end="         ", flush=True)
    increment += 1
    if increment >= 5:
        print()
        increment = 0
    time.sleep(1)    
    
print("\nDone counting!")