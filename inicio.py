#print("Alo mundo rubronegro")
from flask import Flask, render_template
from matematica import Matematica


app = Flask(__name__)

@app.route('/inicio')
def ola():
    return "Ola Lindo Rubronegro"
#app.run() tiver outras rotas no mesmo arquivo so um executa todas

@app.route('/olamundo')
def ola2():
    return render_template('teste.html')
#app.run()

@app.route('/calculosoma')
def calcular():
    mat = Matematica(5,7)
    resposta = mat.somar()
    return render_template('calculo.html', resultado = resposta)
app.run()