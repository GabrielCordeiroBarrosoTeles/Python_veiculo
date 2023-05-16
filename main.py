import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prova"
)
cursor = conexao.cursor()
opcao = input('1-Inserir 2-Exibir 3-Pesquisa 4-Imprimir 5-tipo 6-aumento')
if(opcao == "1"):
    desc = input("descricao")
    marca = input("marca")
    tipo = input("tipo combustivel")
    ano_fab = input("ano fabricação")
    categoria = input("categoria")
    qtd_pass = input("quantidade de passageiros")
    valor = input("valor")

    sql = f'INSERT INTO veiculos VALUES(0,"{desc}","{marca}","{tipo}","{ano_fab}","{categoria}","{qtd_pass}","{valor}")'
    cursor.execute(sql)
    conexao.commit()
elif(opcao=="2"):
    sql = "SELECT * FROM veiculos"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)
elif(opcao =="3"):
    nome=input("nome do veiculo")
    marca = input("marca do veiculo")
    sql =f"SELECT * FROM veiculos WHERE descricao='{nome}' AND marca='{marca}'"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)

elif(opcao =="4"):
    sql ="SELECT * FROM veiculos WHERE valor>=80000"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)

elif(opcao =="5"):
    sql = "SELECT * FROM veiculos WHERE categoria='pariticular' AND valor>=80000"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)

elif(opcao =="6"):

    sql = "UPDATE veiculos SET valor=valor*1.10 WHERE tipo='gasolina'"
    cursor.execute(sql)
    conexao.commit()


    cursor.close()
    conexao.close()