# cuenta-elementos-de-lista-1.py

cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += ' '

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))