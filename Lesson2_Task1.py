

def check_string_isnumber (test_string):
    if test_string.isdigit():
        print("You entered a number")
    else:
        print("It's not a number!")

# check_string_isnumber(input("Enter string: "))




def count_symbols (new_string):
    spaces = 0
    points = 0
    for s in new_string:
        if s == " ":
            spaces += 1
        elif s == ".":
            points += 1
    print("Spaces - " + str(spaces) + "\nPoints - " + str (points))

# count_symbols("dhhj difjjk.sf jsdhfjh.h ksdjf...k")




def decorate_text (new_string, decoration_symbol, total_length):
    while len(new_string) < total_length :
        new_string = decoration_symbol + new_string + decoration_symbol
    print(new_string)
    print(len(new_string))
    return (new_string)

# print(decorate_text("homework", " ", 100).title())