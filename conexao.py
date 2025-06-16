import pymysql

def conectar():
    try:
        conexao = pymysql.connect(
            host='host',
            user='usuario',
            password='sua_senha',
            database='nome_database',
        )
        print('Conectado ao banco de dados!')
        return conexao
    except pymysql.MySQLError as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None
