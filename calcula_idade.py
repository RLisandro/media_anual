from datetime import datetime
data_nascimento = input("Digite sua data de nascimento: (dd/mm/aa):  ")
nasc = datetime.strptime(data_nascimento,"%d/%m/%Y")
hoje = datetime.today() 
idade = hoje.year  -  nasc.year
print(f"Sua idade é: {idade} ano.")
print("Acima sua idade!!")

