from pandas import *

options.display.max_rows = 100000000

temp = read_excel("src/files/BASE.xlsx", sheet_name="DB", index_col=0, header=0)

imcV = []
imcC = []
for _, row in temp.iterrows():
    imc = float("%.1f" % (row["Peso (Kg)"] / ((row["Altura(cm)"] / 100) ** 2)))

    imcV.append(imc)
    if imc < 18.5:
        imcC.append("Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        imcC.append("Adecuado")
    elif imc >= 25 and imc <= 29.9:
        imcC.append("Sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        imcC.append("Obesidad tipo I")
    elif imc >= 35 and imc <= 39.9:
        imcC.append("Obesidad tipo II")
    elif imc >= 40:
        imcC.append("Obesidad tipo III")
    else:
        imcC.append("Error")

temp.insert(4, "IMC", imcV)
temp.insert(5, "CategoriaPeso", imcC)

print(temp)
