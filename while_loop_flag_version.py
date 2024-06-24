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
    continue_singing = True
    while continue_singing:
        if bottles > 0:
            if bottles == 1:
                print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            else:
                print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles -= 1
            if bottles == 1:
                print(f"Take one down, pass it around, {bottles} bottle of beer on the wall.\n")
            elif bottles == 0:
                print(f"Take it down, pass it around, no more bottles of beer on the wall!\n")
            else:
                print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
        else:
            continue_singing = False

if __name__ == "__main__":
    num_bottles = get_starting_number()
    sing(num_bottles)