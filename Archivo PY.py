import math
#Adrián Parra
#Creado 21/2/2023

angle=0
suma=0
ea=5
es=(0.5*(10**-8))
n=0
print("Este programa solicita un angulo y entrega el resultado de Cos(X) con menor porcentaje de error")
clase="hola"
clase=str(input("Quieres ingresar el angulo en radianes o grados: "))
clase=clase.lower()

#While parcheado el 13/2/2024
while clase!="radianes" or clase!="r" or clase!="grados" or clase!="g":
    if clase == "radianes" or clase == "r":
        print("Ingrese un angulo en radianes de la forma Xπ/n")
        x=int(input("Ingrese el X de los radianes: "))
        n=int(input("Ingrese el n de los radianes: "))
        angle=(x*math.pi)/n
        print(f"{angle} radianes")
        break
    elif clase == "grados" or clase == "g":
        print("Ingrese un angulo en grados")
        angle=float(input("Ingrese el angulo: "))
        angle=(angle*math.pi)/180
        print("El angulo se pasara a radianes")
        print(f"{angle} radianes")
        break
    else:
        print("Ingrese una opcion valida")
        clase=str(input("Quieres ingresar el angulo en radianes o grados: "))
    
opcion=str(input("Quieres imprimir solo la respuesta (S/N): "))
opcion=opcion.lower()

if opcion=="s" or opcion=="si":
  while ea>es:
    coseno=((-1)**n)*((angle**n)/math.factorial(n))
    suma+=coseno      
    if suma!=0:
      ea=abs((coseno/suma)*100)
      ea=round(ea,8)        
    n+=1
  print(f"Total: {suma}")
  print("Porcentaje de error final ",ea,"%")
  print("El numero de iteraciones totales es de:",n)
else:
  while ea>es:
    print(f"Cos({(round(angle,2))})= {suma}")
    coseno=((-1)**n)*((angle**n)/math.factorial(n))
    suma+=coseno
    print("Valor estimado: ",suma)
    if suma!=0:
      ea=abs((coseno/suma)*100)
      ea=round(ea,8)
      print("El error aproximado relativo en porcentaje es: ",ea, "%")
    n+=1
    print("Iteración número: ",n)