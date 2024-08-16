#print("Alô Mundo Tarde!")
# from é o método e import é uma classe
from flask import Flask, render_template
from matematica import Matematica
from timefut_1 import TimeFut

# app (objeto) instância class Flask no parâmetro do construtor (__name__)
app = Flask(__name__)
# valor__name__:
    # a. App é uma instância
    # b. Flask() é o construtor da classe Flask
    # c. __name__: é uma variável especial em pyhon que é definida como o nome do módulo atual. 
    # Quando você passa __name__ 

# Defina uma função ola() nela retorne a mensagem Alô Mundo:
@app.route('/inicio')
def ola():
    return "Olá Mundo"

# Chame a função de execução do flask:
#app.run()

# Defina uma função ola() nela retorne a mensagem Alô Mundo:
@app.route('/olamundo')
def mostrar():
    return render_template('pagina.html')

# rota calculo/soma
@app.route('/calculosoma')
def calcular():
    mat = Matematica(10,5)
    resposta = mat.somar()
    return render_template('pag_calc.html',resultado=resposta)

@app.route('/listatimes')
def lista_times():
    t1 = TimeFut('Palmeiras',10)
    t2 = TimeFut('Botafogo',7)
    t3 = TimeFut('Flamengo',11)
    lista = [t1,t2,t3]
    return render_template('listatimestable.html',times=lista)

# Chame a função de execução do flask:
app.run(debug=True)
