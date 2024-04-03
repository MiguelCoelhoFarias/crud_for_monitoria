
#import para conectar o código com o banco de dados

#CRUD OUVIDORIA (CREATE - READ - UPDATE - DELETE)


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="miguelroot",
    passwd="root123",
    database= "banco"
    ### lembrar que o database só é adicionado nesse escopo depois de criado!
);

print(db); ### comando para printar a conexão com banco! 

### criando uma variavel para comandos direto no banco:
comandosBanco = db.cursor();
### criando um banco na sua conexão: 
###comandosBanco.execute("CREATE DATABASE banco");



###agora comando para criar a tabela dentor do seu Schema: 
###comandosBanco.execute("CREATE TABLE ocorrencias (tipo VARCHAR(255), assunto VARCHAR(255), descricao VARCHAR(255))")

### alterando a tabela para criar uma chave primaria para cada dado que entrar:
comandosBanco.execute("CREATE TABLE IF NOT EXISTS ocorrencias (id INT AUTO_INCREMENT PRIMARY KEY, tipo VARCHAR(255), assunto VARCHAR(255), descricao VARCHAR(255))")

### esse comando mostra os dados que estao presentes na nossa tabela - no nosso caso a tabela de ocorrencias: 

comandosBanco.execute("SELECT * FROM ocorrencias")
resultados = comandosBanco.fetchall();

for resultado in resultados:
    print(resultado)

optionsMenu = 0
print("Bem vindo ao sistema de ouvidoria da unifacisa. By: Miguelzin ^^")
while optionsMenu != 4:
    print("1-Criar um ticket.\n2-Listar Ticket\n3-Apagar ticket(s)\n4-Sair.")
    optionsMenu = int(input("Digite um numero correspondente a opcao desejada"))
    if optionsMenu == 1:
        print("Qual a categoria do seu ticket?")
        print("1-Elogio\n2-Sugestão\n3-Reclamação")
        optionsTicket = int(input())
        if optionsTicket == 1:
            assunto= input("Digite o assunto do seu elogio: ");
            print();
            descricao= input("Agora escreva a sua ocorrencia");
            comando_sql = "INSERT INTO ocorrencias (tipo, assunto, descricao) VALUES (%s, %s, %s)"
            dadosParaBanco = ("elogio", assunto, descricao)
            comandosBanco.execute(comando_sql, dadosParaBanco)
            db.commit();
            print("ocorrencia registrada com sucesso!") # aqui ele registra nossa ocorrencia
        elif optionsTicket == 2:
            print()
        elif optionsTicket == 3:
            print()
    elif optionsMenu == 2:
        print("aqui estao os tickets salvos em nosso sistema:")

    elif optionsMenu == 3:
        print("Deseja apagar: ")
        print("1-Ticket especifico.\n2-Apagar tudo.")

    elif optionsMenu == 4:
        print("Obrigado, finalizando seu atendimento. Bye ^^")

    else:
        print("Opçao invalida, tente novamente.")