from flask import Flask, render_template, request
import classes
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def form():
    x=float(request.form['num1'])
    y=float(request.form['num2'])


    operation_type = request.form['operation']
    if operation_type == 'add':
        operation = classes.addition(x,y)

    if operation_type == 'subtract':
        operation = classes.subtraction(x,y)

    if operation_type == 'multiply':
        operation = classes.multiplication(x,y)

    if operation_type == 'divide':
        operation = classes.division(x,y)

    return render_template('calculate.html',result=operation.do_operation())







if __name__ == "__main__":
    app.run(debug=True)