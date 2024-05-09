from flask import Flask, render_template, request #Importa a classe Flask

app = Flask(__name__) #Cria uma instancia da aplicação Flask

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():

    maior = 0
    menor = 999
    media = 0
    for i in range (10):
        numero = int(request.form["numero" + str(i)])
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        media += (numero/10)
    menor = menor
    maior = maior
    media = media

    return render_template('index.html', menor = menor, maior = maior, media=media) #o retorno

if __name__ == '__main__': # Verifica se está sendo executado diretamente
    app.run(debug=True)  # Inicia o servidor de desenvolvimento do Flask com modo de depuração ativado



