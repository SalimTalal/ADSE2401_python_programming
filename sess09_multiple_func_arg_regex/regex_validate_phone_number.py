# Python script/file to validate a Kenyan phone number using regular expressions : regex

# Import the regex(regular expression) module
import re

# Function to validate the phone number
def validate_phone_number(phone_number):
    """
    Validates whether a given phone number is a valid Kenyan phone number.

    The phone number must:
       - Start with the country code '+254'
       - Optionally include spaces after the country code or carrier code
       - Include a valid 3-digit carrier code starting with digits 1 to 7
       - Be followed by 6 or 7 digits

    Parameters:
       phone_number (str): The phone number to validate. Should be in international format (+254...).

    Returns:
       None: Prints a message indicating whether the phone number is valid or not.

    Example:
        >>> validate_phone_number("+254712345678")
        The number +254712345678 is a valid Kenyan phone number.

        >>> validate_phone_number("0712345678")
        The number 0712345678 is not a valid Kenyan phone number.
    """
    # Python raw string with a regex to match the Kenyan phone number
    # pattern = r"^[a-zA-Z\d.+_-]+@[a-zA-Z\d._]+\.[a-zA-Z]+$"
    pattern = r"\+254\s?([1-7]\d\d)\s?(\d){6,7}"

    if not phone_number:
        print("Please enter your phone number")
        return

    # Compare the input phone number and the pattern and display an apt message
    if re.match(pattern, phone_number):
        print(f"The number {phone_number} is a valid Kenyan phone number.")
    else:
        print(f"The number {phone_number} is not a valid Kenyan phone number.")

if __name__ == "__main__":
    phone = input("Enter phone number for validation : ")
    validate_phone_number(phone)

# Prompt the user for their phone number
phone_num = input("Please enter your phone number and I'll tell you if it's a valid"
                  " Kenyan phone number. : \n")

# Validate the user's phone number
validate_phone_number(phone_num)