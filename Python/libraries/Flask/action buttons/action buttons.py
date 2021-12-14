from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            print('action1')
        elif  request.form.get('action2') == 'VALUE2':
            print('action2')
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template('index.html')

app.run()