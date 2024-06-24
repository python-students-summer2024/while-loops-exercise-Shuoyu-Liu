def get_starting_number():
    while True:
        try:
            starting_bottles = int(input("Enter the number of starting bottles: "))
            if starting_bottles >= 1:
                return starting_bottles
        except ValueError:
            print("Invalid input. Please enter a number.")

def sing(starting_bottles):
    bottles = starting_bottles
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        if bottles == 1:
            print(f"Take one down, pass it around, {bottles} bottle of beer on the wall.\n")
        else:
            print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
    print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
    print("Take it down, pass it around, no more bottles of beer on the wall!\n")
    # print("No more bottles of beer on the wall, no more bottles of beer.")
    # print("Go to the store and buy some more, no more bottles of beer on the wall.")

if __name__ == "__main__":
    num_bottles = get_starting_number()
    sing(num_bottles)