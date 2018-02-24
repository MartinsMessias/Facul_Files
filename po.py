"""
Autor:
	https://github.com/MartinsMessias
"""

material = 500	# Quantidade de material max
horas = 600	# Quantidade de horas max
t1preco = 50	# Preço da porta tipo 1
t2preco = 40	# Preço da porta tipo 2
t3preco = 55	# Preço da porta tipo 3
t1horas = 7	# Tempo de produção porta 1
t2horas = 6	# Tempo de produção porta 2
t3horas = 8	# Tempo de produção porta 3
t1mater = 8	# material usado na porta 1
t2mater = 4	# material usado na porta 2
t3mater =3	# material usado na porta 3

while True:
	print("_"*20, "\n\033[01;37mPesquisa Operacional\n")
	print("Material: ", material)
	print("Horas: ", horas)
	print("_"*20, "\n")

	quantp1 = int(input("Quantidade de portas tipo 1: "))
	quantp2 = int(input("Quantidade de portas tipo 2: "))
	quantp3 = int(input("Quantidade de portas tipo 3: "))

	qm1 = quantp1 * t1mater	# Total de material porta 1
	qm2 = quantp2 * t2mater	# Total de material porta 2
	qm3 = quantp3 * t3mater	# Total de material porta 3

	qh1 = quantp1 * t1horas	# Total de horas porta 1
	qh2 = quantp2 * t2horas	# Total de horas porta 2
	qh3 = quantp3 * t3horas	# Total de horas porta 3

	pr1 = quantp1 * t1preco	# Total de lucro sobre porta 1
	pr2 = quantp2 * t2preco	# Total de lucro sobre porta 2
	pr3 = quantp3 * t3preco	# Total de lucro sobre porta 3

	tpt = quantp1 + quantp2 + quantp3 # Total de portas
	thp = qh1 + qh2 + qh3	# Total de horas
	tmt = qm1 + qm2 + qm3	# Total de material
	luc = pr1 + pr2 + pr3	# Total de lucro

	print("Foram produzidas \033[01;32m", tpt, " portas\033[00;37m")
	print("\033[01;37mEm \033[01;32m", thp, " horas\033[00;37m")
	print("\033[01;37mUsando \033[01;32m", tmt, "kg de material\033[00;37m")
	print("\033[01;37mLUCRO:  \033[01;32m €", luc, " Euros\033[00;37m")
	print("_" *20)

	if thp > horas:
		print("\033[01;31m\nTOTAL DE HORAS ULTRAPASSADO\033[00;37m")
		print("Em ", thp - horas, "hs")

	if tmt > material:
		print("\n\033[01;31mTOTAL DE MATERIAL ULTRAPASSADO\033[00;37m")
		print("Em ", tmt - material, "kg\n")
		
	test = str(input("\033[01;37mExecutar novamente ?  [S/n]\n :: \033[00;37m")).lower()
	
	if test  != 's':
		break
	
