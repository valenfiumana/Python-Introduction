def subsecuencias_suma(lista, objetivo):
    def backtrack(inicio, sumaval, subsecuencia_actual):
        if sumaval == objetivo:
            res.append(subsecuencia_actual)
            return
        for i in range(inicio, len(lista)):
            if sumaval + lista[i] <= objetivo:
                backtrack(i+1, sumaval+lista[i], subsecuencia_actual+[lista[i]])

    res = []
    backtrack(0, 0, [])
    return res

lista = [1, 2, 3, 4, 5]
objetivo = 7
resultados = subsecuencias_suma(lista, objetivo)
print(resultados)