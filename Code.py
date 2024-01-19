#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID: W2052759
#Date:2023/12/13

#import the graphics.py module (must be in the same folder this file)
from graphics import *

# Function to validate input for credits
def validate_input(credit_type, input_value):
    try:
        credit_value = int(input_value)
# Check if the credit value is within the specified range
        if credit_value not in [0, 20, 40, 60, 80, 100, 120]:
            return 'Out of range'
        return credit_value
    except ValueError:
        return 'Integer required'

# Function to calculate the progression outcome based on credits    
def calculate_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

# Check if the total credits equal 120
    if total_credits != 120:
        return 'Total incorrect'

# Determine the progression outcome based on credit distribution
    if fail_credits >= 80:
        return 'Exclude'
    elif fail_credits >= 60:
        return 'Retriever'
    elif pass_credits == 120:
        return 'Progress'
    elif pass_credits == 100:
        return 'Trailer'
    else: return 'Retriever'

# Function to display histogram of progression outcomes
def display_histogram(progress_count,trailing_count, retriever_count, exclude_count):
    win = GraphWin("Histogram", 600, 400)
    labels = ["Progress", "Trailer", "Retriever", "Exclude"]
    counts = [progress_count, trailing_count, retriever_count, exclude_count]
    colors = ["green", "yellow", "orange", "red"]
    x = 50

# Iterate through each outcome, draw a bar, label, and count
    for i in range(4):
        if counts[i] > 0:
            bar = Rectangle(Point(x, 330), Point(x + 75, 330 - counts[i] * 5))
            bar.setFill(colors[i])
            bar.draw(win)

            label = Text(Point(x + 37.5, 350), labels[i])
            label.draw(win)

            total_label = Text(Point(x + 37.5, 340 - counts[i] * 5 - 20), str(counts[i]))
            total_label.setSize(12)
            total_label.draw(win)

        x += 150

    total_label = Text(Point(300, 380), f"Total Students: {sum(counts)}")
    total_label.draw(win)

    win.getMouse()
    win.close()

# Main function    
def main():
    progression_data = []

    outcomes = {"Progress": 0, "Trailer": 0, "Retriever": 0, "Exclude": 0}
    
# Input loop for entering credits and calculating outcomes   
    while True:
        pass_credits = input("Enter your total PASS credits: ")
        defer_credits = input("Enter your total DEFER credits: ")
        fail_credits = input("Enter your total FAIL credits: ")

        pass_validation = validate_input('pass', pass_credits)
        defer_validation = validate_input('defer', defer_credits)
        fail_validation = validate_input('fail', fail_credits)

# Check if input is valid integers
        if isinstance(pass_validation, int) and isinstance(defer_validation, int) and isinstance(fail_validation, int):
            outcome = calculate_outcome(pass_validation, defer_validation, fail_validation)
            print(outcome)

# Store the data
            progression_data.append((pass_validation, defer_validation, fail_validation, outcome))   
            print("  ")
            continue_input = input("Would you like to enter another set of data? (Enter 'y' for yes, 'q' to quit): ")
            while continue_input not in ['y','q']:
                continue_input = input("Would you like to enter another set of data? (Enter 'y' for yes, 'q' to quit): ")
            if continue_input.lower() == 'q':
                break
            else:
                continue
        else:
            print(pass_validation)
    
# Part 2: Displaying stored data
    print("\nPart 2: Displaying stored data")
    for data in progression_data:
        print(f"{data[3]} - {data[0]}, {data[1]}, {data[2]}")

    outcomes["Progress"],
    outcomes["Trailer"],
    outcomes["Retriever"],
    outcomes["Exclude"]

# Part 3: Save data to a text file
    print("\nPart 3: Reading and Writing data to Textfile")
    with open("progression_data.txt", "w") as file:
        for data in progression_data:
            file.write(f"{data[3]} - {data[0]}, {data[1]}, {data[2]}\n")

# Part 3: Display data from the text file
    with open("progression_data.txt", "r") as file:
        for line in file:
            print(line.strip())

# Count and display outcomes and display the histogram
    for _, _, _, outcome in progression_data:
        outcomes[outcome] += 1
        
    display_histogram(outcomes["Progress"], outcomes["Trailer"], outcomes["Retriever"], outcomes["Exclude"])

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
