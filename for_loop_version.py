def get_starting_number():
    while True:
        try:
            starting_bottles = int(input("Enter the number of starting bottles: "))
            if starting_bottles >= 1:
                return starting_bottles
        except ValueError:
            print("Invalid input. Please enter a number.")

def sing(num_bottles):
    for n in range(num_bottles, 0, -1):
        if n > 1:
            print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
            if n-1 == 1:
                print(f"Take one down, pass it around, {n-1} bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {n-1} bottles of beer on the wall.\n")
        else:
            print(f"{n} bottle of beer on the wall, {n} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")

if __name__ == "__main__":
    num_bottles = int(input("How many bottles of beer on the wall? "))
    sing(num_bottles)