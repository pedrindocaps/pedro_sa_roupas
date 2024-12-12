import mysql.connector
from mysql.connector import Error

def conectar_db():
    """Estabelece a conexão com o banco de dados MySQL"""
    try:
        db = mysql.connector.connect(
            host="localhost",  # ou o endereço do servidor MySQL
            user="root",       # seu usuário no MySQL
            password="root",   # sua senha no MySQL
            database="sa_roupas"  # nome do banco de dados onde suas tabelas estão
        )
        if db.is_connected():
            print("Conexão estabelecida com sucesso.")
            return db
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def inserir_fornecedor(cursor):
    """Insere um novo fornecedor na tabela Fornecedores"""
    insert_fornecedores = """
    INSERT INTO Fornecedores (nome, cnpj, endereco, telefone, email) 
    VALUES (%s, %s, %s, %s, %s)
    """
    valores_fornecedor = ("Fornecedor de Tecidos LTDA", "12.345.678/0001-90", "Rua das Flores, 123", "(11) 98765-4321", "contato@tecidos.com")

    try:
        cursor.execute(insert_fornecedores, valores_fornecedor)
        print(f"{cursor.rowcount} registro(s) inserido(s) na tabela Fornecedores.")
    except Error as e:
        print(f"Erro ao inserir dados na tabela Fornecedores: {e}")
        raise  # Relança o erro para garantir que a transação falhe e faça rollback

def inserir_produto(cursor):
    """Insere um novo produto na tabela Produtos"""
    insert_produtos = """
    INSERT INTO Produtos (nome, descricao, preco, quantidade_em_estoque, fornecedor_id) 
    VALUES (%s, %s, %s, %s, %s)
    """
    valores_produto = ("Camiseta Básica", "Camiseta 100% algodão, ideal para o dia a dia", 29.90, 100, 1)

    try:
        cursor.execute(insert_produtos, valores_produto)
        print(f"{cursor.rowcount} registro(s) inserido(s) na tabela Produtos.")
    except Error as e:
        print(f"Erro ao inserir dados na tabela Produtos: {e}")
        raise  # Relança o erro para garantir que a transação falhe e faça rollback

def main():
    # Conectar ao banco de dados
    db = conectar_db()
    if db is None:
        print("Falha na conexão com o banco de dados. Finalizando.")
        return

    # Criar um cursor para executar comandos SQL
    cursor = db.cursor()

    try:
        # Inserir dados nas tabelas
        inserir_fornecedor(cursor)
        inserir_produto(cursor)

        # Confirmar as transações
        db.commit()
        print("Transações confirmadas com sucesso.")

    except Error as e:
        print(f"Erro durante a execução das transações: {e}")
        db.rollback()  # Faz rollback caso algo dê errado
        print("Transações revertidas.")

    finally:
        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        db.close()
        print("Conexão com o banco de dados fechada.")

if __name__ == "__main__":
    main()
