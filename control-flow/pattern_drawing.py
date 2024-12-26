pattern_size = int(input("Enter the size of the pattern:"))
counter = pattern_size
while counter > 0:
    for i in range(0, pattern_size):
        print ("*", end = "")
    counter -= 1
    print()

