from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greeting.html', name=name)
    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=4000)
