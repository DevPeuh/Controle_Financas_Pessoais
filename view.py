from models import Conta, engine, Bancos, Status
from sqlmodel import Session, select # Session para fazer a conexão com o banco de dados rápida e select para fazer a seleção de dados

# With é uma forma de abrir um arquivo, conexão com o banco de dados, e garantir que ele será fechado ao final do bloco
def criar_conta(conta: Conta):
    with Session(engine) as session: # Abre a conexão com o banco de dados criado antes
        statement = select(Conta).where(Conta.banco == conta.banco) # Seleciona a conta onde o banco é igual ao banco informado
        result = session.exec(statement).all() # Executa a seleção e armazena o resultado em uma lista

        if result:
            raise ValueError('Conta já existe') # Caso a conta já exista, retorna um erro

        session.add(conta) # Determninar uma determinada linha/tabela no banco de dados
        session.commit() # Salvar as alterações no banco de dados
        return conta


def listar_contas():
    with Session(engine) as session: 
        statement = select(Conta) # Seleciona todas as contas
        result = session.exec(statement).all() 
    return result # Retorna todas as contas


def desativar_conta(id):
    with Session(engine) as session:
        statement = select(conta).where(conta.id == id) # Seleciona a conta onde o id é igual ao id informado
        conta = session.exec(statement).first() # Executa a seleção e armazena o resultado na variável result, traz o primeiro resultado 

        if conta.valor > 0:
            raise ValueError('Conta com saldo positivo não pode ser desativada') # Caso a conta tenha saldo positivo, retorna um erro
        
        conta.status = Status.INATIVO # Altera o status da conta para inativo
        session.commit()


def transferir_saldo(id_conta_saida, id_conta_entrada, valor): # Transferir saldo de uma conta para outra
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id_conta_saida) # Seleciona a conta onde o id é igual ao id informado
        conta_saida = session.exec(statement).first() # Executa a seleção e armazena o resultado na variável conta, traz o primeiro resultado

        if conta_saida.valor < valor:
            raise ValueError('Saldo insuficiente') # Caso o saldo da conta seja menor que o valor informado, retorna um erro

        statement = select(Conta).where(Conta.id == id_conta_entrada) 
        conta_entrada = session.exec(statement).first()

        conta_saida.valor -= valor # tirar o valor da conta de saída
        conta_entrada.valor += valor # adicionar o valor na conta de entrada
        session.commit()

#conta = Conta(valor=140, banco=Bancos.NUBANK)
#criar_conta(conta)

#transferir_saldo(1, 2, 50)

