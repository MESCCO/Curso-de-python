#TRISANO MESCCO CONDE 246197
N=int(input())
hora=N//3600
minutos=(N%3600)//60
segundos=(N%3600)%60
print(f"{hora}:{minutos}:{segundos}")