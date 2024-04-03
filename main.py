
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

optionsMenu = 0;
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
            descricao= input("Agora escreva a sua ocorrencia: ");
            comando_sql = "INSERT INTO ocorrencias (tipo, assunto, descricao) VALUES (%s, %s, %s)"
            dadosDaOcorrencia = ("elogio", assunto, descricao)
            comandosBanco.execute(comando_sql, dadosDaOcorrencia)
            db.commit(); # commitando as alteracoes (salvando os dados novos no banco)
            print("ocorrencia registrada com sucesso!") # aqui ele registra nossa ocorrencia
        
        elif optionsTicket == 2:
        
            assunto= input("Digite o assunto da sua sugestão: ");
            print();
            descricao= input("Agora escreva a sua ocorrencia: ");
            comando_sql = "INSERT INTO ocorrencias (tipo, assunto, descricao) VALUES (%s, %s, %s)"
            dadosDaOcorrencia = ("sugestao", assunto, descricao)
            comandosBanco.execute(comando_sql, dadosDaOcorrencia)
            db.commit(); # commitando as alteracoes (salvando os dados novos no banco)
            print("ocorrencia registrada com sucesso!") # aqui ele registra nossa ocorrencia
        
        elif optionsTicket == 3:
            
            assunto= input("Digite o assunto da sua reclamacao: ");
            print();
            descricao= input("Agora escreva a sua ocorrencia: ");
            comando_sql = "INSERT INTO ocorrencias (tipo, assunto, descricao) VALUES (%s, %s, %s)"
            dadosDaOcorrencia = ("reclamacao", assunto, descricao);
            comandosBanco.execute(comando_sql, dadosDaOcorrencia);
            db.commit(); # commitando as alteracoes (salvando os dados novos no banco)
            print("ocorrencia registrada com sucesso!"); # aqui ele registra nossa ocorrencia

    elif optionsMenu == 2:
        
        ### esse comando mostra os dados que estao presentes na nossa tabela - no nosso caso a tabela de ocorrencias: 
        comandosBanco.execute("SELECT * FROM ocorrencias")
        resultados = comandosBanco.fetchall();
        #itera a tabela e mostra os dados presentes em cada linha e coluna:
        for resultado in resultados:
            print("ID: ",resultado[0],"| Tipo: ",resultado[1],"| Assunto: ",resultado[2],"| Descrição: ",resultado[3])

    elif optionsMenu == 3:
        print("Deseja apagar: ")
        print("1-Ticket especifico.\n2-Apagar tudo.")
        optionsDelete = int(input())
        if optionsDelete == 1: 
                comandosBanco.execute("SELECT * FROM ocorrencias")
                resultados = comandosBanco.fetchall();
                #itera a tabela e mostra os dados presentes em cada linha e coluna:
                for resultado in resultados:
                    print("ID: ",resultado[0],"| Tipo: ",resultado[1],"| Assunto: ",resultado[2],"| Descrição: ",resultado[3])
                idOcorrencia = int(input("Digite agora o número correspondente ao ID da ocorrencia que deseja apagar: "))
                # Comando SQL para deletar a ocorrência com base no ID
                comando_sql = "DELETE FROM ocorrencias WHERE id = %s"
                dados_para_banco = (idOcorrencia,)
                # Executar o comando SQL
                comandosBanco.execute(comando_sql, dados_para_banco)
                # Salvando alteracoes:
                db.commit();
                # essa parte do codigo faz com que a contagem de id da ocorrencia volte para 1 quando recomeçar: 
                comando_sql_reset = "ALTER TABLE ocorrencias AUTO_INCREMENT = 1"
                comandosBanco.execute(comando_sql_reset);
                db.commit();
                print("Ocorrencia deletada com sucesso!");
        elif optionsDelete == 2: 
                print("AVISO: ESSA AÇÃO IRA REMOVER TODAS AS OCORRENCIAS DO SEU BANCO, TEM CERTEZA DISSO?")
                confirmacaao = input("Se sim, digite: 'sim'. Caso o contrário iremos cancelar por segurança")
                if confirmacaao == 'sim' : 
                     comando_sql = "DELETE FROM ocorrencias";
                     comandosBanco.execute(comando_sql);
                     db.commit();
                     print("Todas as ocorrencias foram deletadas com sucesso.")
                else :
                     print("operação cancelada por segurança.")

    elif optionsMenu == 4:
        print("Obrigado, finalizando seu atendimento. Bye ^^")

    else:
        print("Opçao invalida, tente novamente.")