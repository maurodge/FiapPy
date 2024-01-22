#criando um arquivo (nome do arquivo, modo de execução, o caso, o w significa criar novo arquivo)
arquivo = open("primeiro_arquivo.txt", "w")

#chamando metodo write para preencher o txt
arquivo.write("Hellow world")

#chamando metodo close
arquivo.close()