dias = int(input("Informe a quantidade de dias:"))
horas = int(input("Informe a quantidade de horas:"))
minutos = int(input("Informe a quantidade de minutos:"))
segundos = int(input("Informe a quantidade de segundos:"))
total_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print("O total em segundos é:", total_segundos)