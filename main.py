from game import SlidingPuzzle

if __name__ == "__main__":
    print("Choose puzzle size:")
    print("1. 3x3")
    print("2. 4x4")
    print("3. 5x5")

    choice = input("Enter your choice (1/2/3): ").strip()

    sizes = {"1": 3, "2": 4, "3": 5}

    if choice in sizes:
        SlidingPuzzle(sizes[choice]).run()
    else:
        print("Invalid choice.")