def days_to_units(num_of_days, conversion_unit ):
    if conversion_unit == "hours":
        return f"{num_of_days}  days are  {num_of_days * 24}  hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days}  days are  {num_of_days * 24 * 60}  minute"
    else:
        return "unsupported unit"

def validate_and_execute(days_and_unit_dictionary):
    #  if user_input.isdigit():
    try:
        user_input_digit = int(days_and_unit_dictionary["days"])
        if user_input_digit > 0:
            calculated_value = days_to_units(user_input_digit, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_digit == 0:
            print("you can't enter a 0 , please entet valid positive number")
        else:
            print("you ara input not a valid number")
    except ValueError:
        print("have a error")

user_input_message ="please input number of days and  conversion unit! \n"
