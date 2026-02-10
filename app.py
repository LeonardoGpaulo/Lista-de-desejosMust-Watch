from flask import Flask, render_template, request, redirect, url_for
from models.streaming import Streaming
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
        tipo_streaming= request.form['data-streaming']
        streaming = Streaming(titulo_streaming, tipo_streaming)
        streaming.salvar_streaming()

    streaming = Streaming.obter_streaming()
    return render_template('lista.html', titulo='Lista de Streams', streamings=streamings)

@app.route('/delete/<int:idWatch>') 
def delete(idStreaming):
    streaming = Streaming.id(idStreaming)
    streaming.excluir_streaming()
    # return render_template('agenda.html', titulo="Agenda", tarefas=tarefas)
    return redirect(url_for('lista')) 



@app.route('/uptade/<int:idStreaming>', methods = ['GET', 'POST'])
def uptade(idStreaming):
        if request.method == 'POST':
            titulo = request.form['titulo_streaming']
            tipo = request.form['tipo_streaming']
            streaming = Streaming(titulo, tipo, idStreaming)
            streaming.atualizar_streaming()
            return redirect(url_for('lista')) #early return
            
        streamings = Streaming.obter_streamings()
        streaming_selecionada = Streaming.id(idStreaming) #seleçã da tarefa que sera editada
        
        return render_template('lista.html', titulo= f'Errou o streaming, refaz ai! ID: {idStreaming}', streamings=streamings, streaming_selecionada=streaming_selecionada)

        
    

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"