def remove_odds(number_list):

    return [num for num in number_list if num % 2 == 0]

def main():

    original_list = [5, 12, 7, -3, 8, 14, 21, -6]


    filtered_list = remove_odds(original_list)

    print("Original list:", original_list)
    print("Filtered list (even numbers only):", filtered_list)


main()
