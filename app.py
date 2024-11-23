from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_ppm(a, b):
    return abs(a * b) // calculate_pgcd(a, b)

@app.route("/", methods=["GET", "POST"])
def index():
    result_pgcd = None
    result_ppm = None
    error_message = None

    if request.method == "POST":
        try:
            num1 = int(request.form.get("num1"))
            num2 = int(request.form.get("num2"))
            result_pgcd = calculate_pgcd(num1, num2)
            result_ppm = calculate_ppm(num1, num2)
        except ValueError:
            error_message = "Please enter valid integers."

    return render_template("index.html", result_pgcd=result_pgcd, result_ppm=result_ppm, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
