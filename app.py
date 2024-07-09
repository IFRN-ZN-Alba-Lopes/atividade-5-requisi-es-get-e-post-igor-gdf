from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

#Questão 1
@app.route('/filme')
def filme():
    return render_template('filme.html')

@app.route('/recebefilme', methods=['GET'])
def recebefilmefilme():
    filme = request.args['filme']
    return render_template('recebefilme.html', filme=filme)

#Questão 2
@app.route('/retangulo')
def retangulo():
    return render_template('retangulo.html')

@app.route('/calcularetangulo', methods=['POST'])
def calcularetangulo():
    l1 = float(request.form['l1'])
    l2 = float(request.form['l2'])
    area = l1*l2
    peri = (l2*2) + (l1*2)
    return render_template('calcularetangulo.html', area=area, peri=peri, l1=l1, l2=l2)

#Questão 3
@app.route('/escolhaotema')
def escolhatema():
    return render_template('escolhaotema.html')

@app.route('/exibeotema', methods=['POST'])
def exibeotema():
    tema = request.form['tema']
    return render_template('exibeotema.html', tema=tema)


#Questão 4
@app.route('/escolhaaforma')
def escolhaaforma():
    return render_template('escolhaaforma.html')

@app.route('/exibeaforma', methods=['POST'])
def exibeaforma():
    forma = request.form['forma']
    return render_template('exibeaforma.html', forma = forma)

#Questão 5
@app.route('/alergias')
def alergias():
    return render_template('alergias.html')

@app.route('/confirmaralergias', methods=['POST'])
def confirmaralergias():
    alergias = request.form.getlist('alergia')
    return render_template('confirmaralergias.html', alergias=alergias)

#Questão 6
@app.route('/addsemente')
def addsemente():
    return render_template('addsemente.html')

@app.route('/savesemente', methods=['POST'])
def savesemente():
    name = request.form['name']
    quantidade = request.form['quantidade']
    tipo = request.form['tipo']
    desc = request.form['desc']
    preferencia = request.form.getlist('preferencia')
    cuidados = request.form['cuidados']
    return render_template('savesemente.html', name=name, quantidade=quantidade, tipo=tipo, desc=desc, preferencia=preferencia, cuidados=cuidados)

if __name__ == '__main__':
    app.run()