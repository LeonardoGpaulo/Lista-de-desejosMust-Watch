from flask import Flask, render_template, request, redirect, url_for
from models.desejos import Streaming
from models.database import init_db

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Lista de Streams')

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    streamings = None

    if request.method == 'POST':
        titulo_streaming = request.form['titulo-streaming']
        tipo_streaming= request.form['tipo-streaming']
        indicado_por = request.form['indicado-por']
        imagem = request.form.get('imagem')


        streaming = Streaming(titulo_streaming, tipo_streaming, indicado_por, imagem=imagem)
        streaming.salvar_lista()

    streamings = Streaming.obter_lista()
    return render_template('lista.html', titulo='Lista de Streams', streamings=streamings)

@app.route('/delete/<int:idStreaming>') 
def delete(idStreaming):
    streaming = Streaming.id(idStreaming)
    streaming.excluir_streaming()
    # return render_template('agenda.html', titulo="Agenda", tarefas=tarefas)
    return redirect(url_for('lista')) 



@app.route('/update/<int:idStreaming>', methods = ['GET', 'POST'])
def update(idStreaming):
        if request.method == 'POST':
            titulo = request.form['titulo-streaming']
            tipo = request.form['tipo-streaming']
            indicado = request.form['indicado-por']
            imagem = request.form.get('imagem')
            streaming = Streaming(titulo, tipo, indicado, imagem=imagem, id_streaming=idStreaming)

            streaming.atualizar_streaming()
            return redirect(url_for('lista')) #early return
            
        streamings = Streaming.obter_lista()
        streaming_selecionada = Streaming.id(idStreaming) #seleçã da streaming que sera editada
        
        return render_template('lista.html', titulo= 'Errou o streaming, refaz ai!', streamings=streamings, streaming_selecionada=streaming_selecionada)

        
    

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"