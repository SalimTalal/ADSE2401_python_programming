# Python script to demonstrate the filter() function

# List of Fibonacci numbers -> golden ration 1.61803
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Get and display a list of odd Fibonacci numbers using the filter() function
even_fibonacci = list(filter(lambda x: x % 2 == 0, numbers))
odd_fibonacci = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Fibonacci numbers : \n{numbers}\nOdd fibonacci numbers : \n{odd_fibonacci}")

# Set of student names
student_names = {"Abigail","Bernice","Charlene","Denise","Sue","Jim","Mark","Micha","William",
                 "Jane","Xi","Alfred","Hillary","Anthony","Brigid","Mitchell","Alice"}

# Use the filter() function to get and display the names starting with 'A'
filtered_names = list(filter(lambda name:name.startswith('A'),student_names))
print(f"All students' names : \n{student_names}\nStudent names starting with 'A' : \n{filtered_names}")

# Function to determine whether a number is prime or not
def is_prime(n):
    """
   Check if a given number is a prime number.

   A prime number is a natural number greater than 1 that has no positive divisors
   other than 1 and itself.

   Args:
   n (int): The number to be checked. Must be a non-negative integer.

   Returns:
   bool: True if the number is prime, False otherwise.

   Examples:
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(29)
    True
    >>> is_prime(100)
    False
    >>> is_prime(97)
    True

   Notes:
   - The function uses the square root to reduce the number of checks.
   - Negative numbers and numbers less than 2 are not considered prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1): # Same as [for i in range(w,int(math.sqrt(n))+1
        if n % i == 0:
            return False
    return True

# Set the range of numbers that we'd like to get prime numbers
num_range = range(1, 70)

prime_numbers = list(filter(is_prime, num_range))
print(f"The prime numbers between 1 and 70 are : \n{prime_numbers}\n")