import bd
import cherrypy
import venvsiteWeb.template.build_html as b_html

class Aplicacao(object):

    @cherrypy.expose
    def index(self):
        html = b_html.Build_html()
        return html.form_html()

    @cherrypy.expose
    def criar_conexao_firebird(self):
        banco_firebird = bd.Bd()
        resposta = banco_firebird.firebird()
        return f"Conexão com o banco de dados Firebird criada com sucesso! {resposta}"

    @cherrypy.expose
    def parar_servidor(self):
        cherrypy.engine.stop()
        return 'Serviço finalizado.'

    @cherrypy.expose
    def consultar(self, tabela):
        html = b_html.Build_html()
        return html.html_dinamico_base(tabela)

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': 'localhost', 'server.socket_port': 6969})
    cherrypy.quickstart(Aplicacao())

# pyinstaller --name siteWeb --onefile --noconsole app.py
