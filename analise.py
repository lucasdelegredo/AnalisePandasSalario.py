import pandas as pd

df = pd.read_csv('Salaries.csv')

#PESQUISAR POR NOME encontrar Emprego
#nome_input = input("Digite o nome desejado: ")
#encontrar_trabalhador = df['EmployeeName']==nome_input
#emprego_trabalhador = df[encontrar_trabalhador]
#print(emprego_trabalhador['JobTitle'].values[0])

#ENCONTRANDO SALARIO MÁXIMO
#maxsalario = df['BasePay'].max()
#QUEM RECEBE O MAIOR SALARIO
#max_salario = df['BasePay'].max()
#linha_max_salario = df['BasePay']==max_salario
#trabalhador = df[linha_max_salario]
#print("O trabalhador que mais recebe é: "+trabalhador['EmployeeName'].values[0]+" total de R$ "+str(max_salario))


#MEDIA DE SALARIO POR ANO
anos = df['Year'].unique()
i=0

while i<len(anos):
    anual = df['Year']==anos[i]
    df_anual = df[anual]

    #Media por ano:
    media_anual = df_anual['BasePay'].mean()
    #Maximo por ano:
    maximo_anual = df_anual['BasePay'].max()
    #Minimo por ano:
    minimo_anual = df_anual['BasePay'].min()
    #Formatar casas decimais
    media_anual = "{:.2f}".format(media_anual)

    #saida das informações por ano
    print("Ano: "+str(anos[i])+" média R$ "+str(media_anual)+" Máximo R$ "+str(maximo_anual)+" Minimo R$ "+str(minimo_anual))
    i=i+1


#CRIAR UMA COLUNA PARA ANALISAR SALARIO
#percorrer linha por linha para identificar
j = 0
df['Analise'] = "x"
analise = []
print(df['BasePay'][3])

while j<len(df):
    salario = df['BasePay'][j]
    salario = float(salario) 

    if(salario>100000):
        analise.append("ACIMA 100K")

    if(salario<=100000 and salario>50000):
        analise.append("ENTRE 50K E 100K")

    if(salario<=50000 and salario>35000):
        analise.append("ENTRE 35K E 50K")

    if(salario<=35000):
        analise.append("ATÉ 35K")

    df['Analise'][j] = analise[j]

    j = j + 1
    
print(df)

