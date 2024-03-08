# Calculator

Simple calculator web application made with the Flask framework and HTML as the 1st assignment for the software engineering course CIE 460.

## Introduction

The calculator exhibits input validation capabilities as it handles cases of non-numeric input or division by 0, providing separate warnings for violations of the 1st number and 2nd number.

## Algorithm

The object-oriented paradigm was utilized, featuring a parent class "Operation" branching into 4 subclasses. The parent class defines the operands x and y in its constructor and has one virtual function, "do_operation()", which the subclasses override based on their specific operations.

## Usage

The main program consists of two webpages:
1. **Input Page**: Prompts the user for input and validates it.
   - Includes two text boxes for operands.
   - Includes a dropdown menu for selecting the operation.
   - Includes a button to proceed.
2. **Result Page**: Displays the calculated result.
   - Includes a text box to print the result.
   - Includes a button to return to the main page for additional operations.

If a validation violation is detected, the program displays a red warning message and prompts the user for valid input.

## File Structure


The README.md file you've written provides a good overview of your project, including its purpose, functionality, and implementation details. However, there are a few suggestions and improvements that can enhance clarity and readability:

markdown
Copy code
# Calculator

Simple calculator web application made with the Flask framework and HTML as the 1st assignment for the software engineering course CIE 460.

## Introduction

The calculator exhibits input validation capabilities as it handles cases of non-numeric input or division by 0, providing separate warnings for violations of the 1st number and 2nd number.

## Algorithm

The object-oriented paradigm was utilized, featuring a parent class "Operation" branching into 4 subclasses. The parent class defines the operands x and y in its constructor and has one virtual function, "do_operation()", which the subclasses override based on their specific operations.

## Usage

The main program consists of two webpages:
1. **Input Page**: Prompts the user for input and validates it.
   - Includes two text boxes for operands.
   - Includes a dropdown menu for selecting the operation.
   - Includes a button to proceed.
2. **Result Page**: Displays the calculated result.
   - Includes a text box to print the result.
   - Includes a button to return to the main page for additional operations.

If a validation violation is detected, the program displays a red warning message and prompts the user for valid input.