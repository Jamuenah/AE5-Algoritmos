seguir= True
totalobtenido=0
porcentajesobtenidos= 0
aprobar=4.0
while seguir:
    nota = float(input("coloca tu nota: "))
    if nota ==-1:
        seguir=False
        break
    porcentaje = float(input("¿A cuanto porcentaje equivale esa nota?: "))
    totalobtenido= totalobtenido+(nota*porcentaje/100)
    porcentajesobtenidos= porcentajesobtenidos+porcentaje
    PorcentajeFaltante= 1.0-(porcentajesobtenidos/100)
    if porcentajesobtenidos > 100:
        print("Porcentajes suman mas que 100%")
        break
NotasNecesarias=(aprobar-totalobtenido)/PorcentajeFaltante
if 7>=NotasNecesarias:
    print(f"Necestias un {NotasNecesarias} en el {PorcentajeFaltante} que te queda de notas")
else:
    print(f"NECESITAS LAS NOTAS RESTANTES SUPERIOR A 7! ESO NO SE PUEDE")
