"""
Autor:
	https://github.com/MartinsMessias
"""

material = 500
horas = 600
t1preco = 50
t2preco = 40
t3preco = 55
t1horas = 7
t2horas = 6
t3horas = 8
t1mater = 8
t2mater = 4
t3mater =3

while True:
	print("_"*20, "\n\033[01;37mPesquisa Operacional\n")
	print("Material: ", material)
	print("Horas: ", horas)
	print("_"*20, "\n")

	quantp1 = int(input("Quantidade de portas tipo 1: "))
	quantp2 = int(input("Quantidade de portas tipo 2: "))
	quantp3 = int(input("Quantidade de portas tipo 3: "))

	qm1 = quantp1 * t1mater
	qm2 = quantp2 * t2mater
	qm3 = quantp3 * t3mater

	qh1 = quantp1 * t1horas
	qh2 = quantp2 * t2horas
	qh3 = quantp3 * t3horas

	pr1 = quantp1 * t1preco
	pr2 = quantp2 * t2preco
	pr3 = quantp3 * t3preco

	tpt = quantp1 + quantp2 + quantp3
	thp = qh1 + qh2 + qh3
	tmt = qm1 + qm2 + qm3
	luc = pr1 + pr2 + pr3

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
	
