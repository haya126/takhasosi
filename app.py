from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    # Get form data
    name = request.form.get('name')
    gpa = request.form.get('gpa')
    math_score = request.form.get('math_score')
    english_score = request.form.get('english_score')
    arabic_score = request.form.get('arabic_score')

    # Example calculation for معدل المكافئ
    # You can replace weights with real Kuwait University formula
    composite_score = (float(gpa) * 0.4) + (float(math_score) * 0.2) + (float(english_score) * 0.2) + (float(arabic_score) * 0.2)

    return render_template(
        'results.html',
        name=name,
        composite_score=round(composite_score, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
