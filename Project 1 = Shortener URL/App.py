from flask import Flask, render_template, request
from flask import *
import re
import random, string
app = Flask(__name__)
data = {}

@app.route('/')
def home_get():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    original = request.form.get('originalurl')
    x = re.match("^https://[\d\D\w\W\s\S^\b\f\r\t\v]*$", original)
    if x:
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        code = random.randint(100000, 999999)
        domain = "http://127.0.0.1:5000/"
        ans = "".join([domain, x,str(code)])

        if ans in data.keys():
            x = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            code = random.randint(1000, 9999)
            ans = "".join([domain, x,str(code)])

        else:
            data[ans] = original

    else:
        flash("Invalid url ")
    return render_template('index.html',ans = ans,original = original)

@app.route('/history')
def history_get():


    return render_template('history.html', data = data.items())

if __name__ == "__main__":
    app.run(debug=True)

