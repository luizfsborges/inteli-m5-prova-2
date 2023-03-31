from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.base import Base
from models.jogos import Jogos

# Criação do banco de dados
engine = create_engine("sqlite+pysqlite:///jogos.db", echo=True)

# Criação da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criação das tabelas
Base.metadata.create_all(engine)

# Inserção de dados
session.commit()

if __name__ == "__main__":

    while True:

        print("\nBem vindo ao sistema de cadastro de jogos!")
        acao = input("\nDigite a ação que deseja realizar ['I' - Inserir jogo | 'L' - Listar jogos]: ")

        if (acao == "I"):

            nome = input("Digite o nome do jogo: ")
            plataforma = input("Digite a plataforma do jogo: ")
            preco = float(input("Digite o preço do jogo: "))
            quantidade = int(input("Digite a quantidade do jogo: "))

            # Inserção de dados
            jogo = Jogos(nome=nome, plataforma=plataforma, preco=preco, quantidade=quantidade)
            session.add(jogo)
            session.commit()

            print("\nJogo cadastrado com sucesso!")

        elif (acao == "L"):
            # Listagem de dados
            jogos = session.query(Jogos).all()
            print("\n[JOGOS CADASTRADOS]:")
            for jogo in jogos:
                print("Nome: ", jogo.nome, " | Plataforma: ", jogo.plataforma, " | Preço: ", jogo.preco, " | Quantidade: ", jogo.quantidade)