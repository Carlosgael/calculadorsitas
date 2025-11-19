from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        expresion = request.form.get("expresion")
        try:
            resultado = str(eval(expresion))
        except:
            resultado = "Error"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
