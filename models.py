from sqlmodel import SQLModel, Field, create_engine
from enum import Enum # Importar Enum para criar um campo de possíveis valores (Possibilades de escolha)


class Bancos(Enum): # Enumeração de possíveis valores para o campo banco
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'
    BRADESCO = 'Bradesco'
    ITAU = 'Itaú'
    CAIXA = 'caixa'


# Caso o usuário apague a conta
class Status(Enum):
    ATIVO = 'ativo'
    INATIVO = 'inativo'


# Criar uma tebla no banco na qual vai armazenar as contas de um usuário
# Herda SQLModel para ser reconhecida pelo SQLModel e table=True para ser reconhecida como uma tabela
class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True) # Campo id é um número inteiro e é a chave primária
    valor: float 
    banco: Bancos = Field(default=Bancos.NUBANK) # Banco é um campo com mais de 1 valor, caso não seja informado, o valor padrão é Nubank
    status: Status = Field(default=Status.ATIVO) # status é um campo com mais de 1 valor, caso não seja informado, o valor padrão é ativo


class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    id_conta: int



# Uma variavel que vai conter o nome do banco de dados, vai conter todos os dados
sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}' # URL de conexão com o banco de dados

# Fazer a conexão com o banco de dados
engine = create_engine(sqlite_url, echo=True) # echo=True para mostrar as mensagens de log de forma descritiva 

# Função para criar a tabela no banco de dados
if __name__ == '__main__': # Verifica se o arquivo está sendo executado diretamente ( No arquivo principal )
    SQLModel.metadata.create_all(engine) # Cria todas as tabelas do banco de dados
