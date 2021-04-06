#!/usr/bin/env python

def my_function():
    return 3 * 2

output = my_function()
print(output)

def format_name(f_name,l_name):
    f_name = f_name.lower()
    l_name = l_name.lower()
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    print(f_name, l_name)

format_name("tIM", "BURton")

def format_name_b(f_name,l_name):
    print(f_name.title(), l_name.title())

format_name_b("eLLIs", "ISLAnd")

def format_name_c(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name_c("ROGer", "hiKES")

def format_name_d(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    print("This is not executed!")

formated_string = format_name_d("tOm", "riCE")
print(formated_string)

def format_name_e(f_name,l_name):
    """Takes two strings and formats into titles"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name_e(input("What is your first name?"),
    input("What is your last name? ")))
