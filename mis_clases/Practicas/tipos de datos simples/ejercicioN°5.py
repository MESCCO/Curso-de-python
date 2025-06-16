"""Escribir un programa que pregunte al usuario por
el número de horas trabajadas y el coste 
por hora. Después debe mostrar por pantalla
la paga que le corresponde."""
horas=int(input("Ingrese las horas trabajadas : "))
precio=int(input("Ingrese el costo por hora trabajada en $: "))
paga=horas*precio
print(f"El pago que le corresponde es $: {paga}")