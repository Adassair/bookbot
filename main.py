with open("books/frankenstein.txt", "r") as file:
    contents = file.read()


word_inbook = contents.split()

def counting ():
    with open("books/frankenstein.txt", "r") as file:
        contents = file.read()

    word_inbook = contents.split()
    number = 0
    for element in word_inbook:
     number += 1

    return number

word_count = counting()


def get_chars_dict(contents):
    chars = {}
    for c in contents:
            lowered = c.lower()
            if lowered in chars:
              chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

number_of_c = get_chars_dict(contents)
print (f"The number of character in the book is {number_of_c}")

def report (number_of_c):
    list_dico = []
    for character, number in number_of_c.items():
        list_dico.append({"Character":character, "Iteration":number})
    return list_dico

dict_report = report(number_of_c)


def sort_on(dict):
    return dict["Iteration"]

def final_report(report_list):
    report_list.sort(reverse=True, key=sort_on)
    return report_list


list_report = report(number_of_c)
the_report = final_report(list_report)
print(the_report)


#NOW USE A LOOP TO PRINT THE LINES ONE BY ONE#
print("--- Begin Report Of Book : Frankenstein ---")
print(f"The book contains {word_count} words.")

for char_data in the_report:
        char = char_data['Character']
        count = char_data['Iteration']
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

print("--- End Of The Report ---")