from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__) #Referência ao objeto Flask, criando uma variável APP que garda os elementos


@app.route("/")#Arquivo index.hmtl. Primeira página ou qualquer site


@app.route("/soma", methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        num1 = request.form['num1'] # Convencionado sempre pegar pelo name do HTML
        num2 = request.form['num2']

        resultado = num1 + num2




def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)