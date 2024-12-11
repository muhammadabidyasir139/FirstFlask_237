from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    name = ''
    if request.method == "POST":
        name = request.form.get("name")
    return render_template('index.html', response=f"Hello, {name}!" if name else"")
    

if __name__ == "__main__":
    app.run(debug=True)
