# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    day = int(pic[0:2]) #int removes zeros (e.g. 07 -> 7)
    month = int(pic[2:4])
    year = int(pic[4:6])
    century_marker = pic[6]
    personal_id = int(pic[7:10])
    control_char = pic[10]

    if century_marker == "+":
        year += 1800
    elif century_marker == "-":
        year += 1900
    elif century_marker == "A":
        year += 2000
    else:
        return False

    
    
    control_list = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    nine_digit_number = f"{pic[:2]}{pic[2:4]}{pic[4:6]}{pic[7:10]}" #keep zeros
    remainder = (int(nine_digit_number)%31)
    true_char = control_list[remainder] #What last character should be

    if control_char != true_char or len(pic) != 11:
        return False
    #
    try:
        datetime(year,month,day)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))