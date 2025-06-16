#calculadora 
nro1 = int(input("Dame el primer numero: "))
nro2 = int(input("Dame el segundo numero: "))
#operacion
operacion = input("introduce una operacion (+ - * /): ")

match operacion:
    case "+":
        res = nro1+nro2
    case "*":
        res = nro1*nro2
    case "-":
        res = nro1-nro2
    case "/":
        res = nro1/nro2
  
  print(f"El resultado de {nro1} {operacion} {nro2} = ",res)