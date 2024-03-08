from flask import Flask, render_template, request  # Importing Flask and related modules
import classes  # Assuming this file contains definitions of classes for arithmetic operations

app = Flask(__name__)  # Creating Flask application instance

@app.route("/")  # Mapping the root URL to the home function
def home():
    return render_template('index.html')  # Rendering the index.html template for the home page

def is_numeric(value):  # Function to check if a value is numeric
    try:
        float(value)
        return True
    except ValueError:
        return False

@app.route('/calculate', methods=['POST'])  # Mapping the '/calculate' URL to the form function for POST requests
def form():
    x = request.form['num1']  # Getting the value of 'num1' from the form
    y = request.form['num2']  # Getting the value of 'num2' from the form
    operation_type = request.form['operation']  # Getting the selected operation type from the form

    warning_num1 = warning_num2 = None  # Initializing warning variables to None

    if not is_numeric(x):  # Checking if 'num1' is numeric
        warning_num1 = "Please enter a numeric value for num1."

    if not is_numeric(y):  # Checking if 'num2' is numeric
        warning_num2 = "Please enter a numeric value for num2."
    elif float(y) == 0 and operation_type == 'divide':  # Checking if 'num2' is zero when division is selected
        warning_num2 = "Can't divide by zero please enter different number"

    while warning_num1 or warning_num2:  # Continuously looping until both warnings are resolved
        return render_template('index.html', warning_num1=warning_num1, warning_num2=warning_num2)  # Rendering index.html with warnings

    # Converting 'num1' and 'num2' to float
    x = float(x)
    y = float(y)

    # Performing the selected arithmetic operation based on the operation type
    if operation_type == 'add':
        operation = classes.Addition(x, y)
    elif operation_type == 'subtract':
        operation = classes.Subtraction(x, y)
    elif operation_type == 'multiply':
        operation = classes.Multiplication(x, y)
    elif operation_type == 'divide':
        operation = classes.Division(x, y)

    # Rendering the result.html template with the result of the operation
    return render_template('result.html', result=operation.do_operation())

# Running the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
