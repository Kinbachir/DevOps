from flask import Flask, render_template, request

app = Flask(__name__)

# Fonctions pour les opérations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Division par zéro non permise"

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    if request.method == "POST":
        try:
            # Récupérer les données du formulaire
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]
            
            # Calculer selon l'opération choisie
            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            else:
                error = "Opération non valide."
        except ValueError:
            error = "Veuillez entrer des nombres valides."
    
    return render_template("calculator.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
