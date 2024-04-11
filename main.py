# Xinyu Shen

def encode_password(encode):
            encoded_password = ""
            for digit in encode:
                encoded_digit = (int(digit) + 3) % 10
                encoded_password += str(encoded_digit)
            return encoded_password
    
def main():
while True:
    print("Menu \n-------------\n1. Encode \n2. Decode \n3. Quit")
    print()
    option = int(input("Please enter an option: "))
    if option == 1:
        encode = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        print()

    elif option == 2:
        print(f"The encoded password is {encode_password(encode)}, "
              f"and the original password is {encode}.")
        print()

    elif option == 3:
        break

if __name__ == "__main__":
    main()
