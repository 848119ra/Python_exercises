"""
Fibonacci sequence. Implement a program that prints the Fibonacci sequence for
a number of times set by the user.
"""
def main():
    number_of_Fibonacci = int(input("How many Fibonacci numbers do you want? "))
    repetition_counter = 1
    previous_fib = 1
    current_fib = 1
    while repetition_counter <= number_of_Fibonacci:
        print(repetition_counter, ". ", previous_fib, sep="")
        next_fib = previous_fib + current_fib
        previous_fib = current_fib
        current_fib = next_fib
        repetition_counter += 1
if __name__ == "__main__":
    main()