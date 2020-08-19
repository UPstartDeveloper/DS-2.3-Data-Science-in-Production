from flask import Flask, render_template, request
import math
from wtforms import Form, FloatField, validators
# from compute import compute

app = Flask(__name__)

# computation
def compute(r):
    return math.sin(r)
# Model
class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])

# View
"""
@app.route('/hw1', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
        return render_template("view-output.html", form=form, s=s)
    else:
        return render_template("view-input.html", form=form)
"""

@app.route('/hw2', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
    else:
        s = None

    return render_template("view.html", form=form, s=s)

if __name__ == '__main__':
    app.run(debug=True)