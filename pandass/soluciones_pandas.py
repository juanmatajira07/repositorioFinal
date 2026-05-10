import pandas as pd
df = pd.read_csv('notas.csv', index_col = 0)
#Ejercicio1
def DecilFinal(estudiante):
    notas = df.mean(axis=1)
    notas_ordenadas = notas.sort_values(ascending=True)
    posicion = notas_ordenadas.index.get_loc(estudiante)
    decil = int((posicion / len(notas_ordenadas)) * 10) + 1 
    return decil
#Ejercicio2
def RankingFinal():
    df_rank = df.copy()
    df_rank['nota_final'] = df_rank.mean(axis=1)
    df_rank = df_rank.sort_values(by='nota_final', ascending=False)
    df_rank.index = range(1, len(df_rank) + 1)
    return df_rank
#faltan ejercicio 3 y 4
