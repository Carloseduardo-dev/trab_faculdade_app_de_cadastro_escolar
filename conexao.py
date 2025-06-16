import pymysql

def conectar():
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='240301',
            database='cadastro',
        )
        print('Conectado ao banco de dados!')
        return conexao
    except pymysql.MySQLError as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None
