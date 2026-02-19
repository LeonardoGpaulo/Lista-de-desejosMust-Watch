from models.database import Database
from typing import Optional, Self, Any
from sqlite3 import Cursor

class Streaming:
    """
        Classe para representar uma streaming, com métodos para salvar, obter, excluir tarefas em um banco de dados usando a classe `Database`.
    """
    def __init__(self: Self, titulo_streaming: Optional[str], tipo_streaming: Optional[str], indicado_por: Optional[str], id_streaming: Optional[int] = None, imagem: Optional[str] = None):
        self.titulo_streaming: Optional[str] = titulo_streaming
        self.tipo_streaming: Optional[str] = tipo_streaming
        self.indicado_por: Optional[str] = indicado_por
        self.imagem: Optional[str] = imagem
        self.id: Optional[int] = id_streaming

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_streaming, tipo_streaming, indicado_por, id_streaming, imagem FROM streamings WHERE id_streaming = ?;'
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)

            [[titulo,tipo,indicado, id, imagem]] = resultado

        return cls(id_streaming=id, titulo_streaming=titulo, tipo_streaming=tipo, indicado_por=indicado, imagem=imagem)

    def salvar_lista(self: Self) -> None:
        with Database () as db:
            query: str = "INSERT INTO streamings (titulo_streaming, tipo_streaming, indicado_por, imagem)VALUES (?, ?, ?, ?);"
            params: tuple = (self.titulo_streaming, self.tipo_streaming, self.indicado_por, self.imagem)
            db.executar(query, params)

    @classmethod
    def obter_lista(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_streaming, tipo_streaming, indicado_por, id_streaming, imagem FROM streamings;'
            resultados: list[Any] = db.buscar_tudo(query)
            streamings: list[Self] = [cls(titulo_streaming, tipo_streaming, indicado_por, id_streaming, imagem) for titulo_streaming, tipo_streaming, indicado_por, id_streaming, imagem in resultados]
            return streamings
        
    def excluir_streaming(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM streamings WHERE id_streaming = ?;'
            params:tuple = (self.id,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        
    def atualizar_streaming(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE streamings SET titulo_streaming = ?, tipo_streaming = ?, indicado_por = ?, imagem = ? WHERE id_streaming = ?;'
            params:tuple = (self.titulo_streaming, self.tipo_streaming, self.indicado_por, self.imagem, self.id)
            resultado: Cursor = db.executar(query, params)
            return resultado