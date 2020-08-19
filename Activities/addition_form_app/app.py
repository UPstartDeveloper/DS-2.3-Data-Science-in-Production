from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def calculate_sum():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    if num1 and num2:
        sum = float(num1) + float(num2)
    else:
        sum = 'Not defined'
    return render_template(
        'base.html', num1=num1, num2=num2, sum=sum
    )
    # user has inputted numbersls
    if request.method == 'POST':
        return redirect(url_for('calculate_sum'))
