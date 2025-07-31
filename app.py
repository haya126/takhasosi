from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # main page

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']  # example form field
    return render_template('results.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)

