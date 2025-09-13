import random


def crear_matriz_temperaturas_sin_numpy():
    """
    Versión sin numpy usando listas anidadas
    """
    ciudades = ["Manta", "Babahoyo", "Guayaquil", "Quito", "Esmeraldas"]
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    semanas = 4

    # Crear matriz 3D: [ciudades][días][semanas]
    temperaturas = []

    for ciudad in range(len(ciudades)):
        matriz_ciudad = []
        for dia in range(len(dias_semana)):
            semana_temps = []
            for semana in range(semanas):
                # Temperatura aleatoria entre 10°C y 35°C
                temperatura = random.randint(10, 35)
                semana_temps.append(temperatura)
            matriz_ciudad.append(semana_temps)
        temperaturas.append(matriz_ciudad)

    return ciudades, dias_semana, semanas, temperaturas


def calcular_promedios_sin_numpy(ciudades, temperaturas):
    """
    Calcular promedios sin usar numpy
    """
    promedios = {}

    for i_ciudad, ciudad in enumerate(ciudades):
        promedios_ciudad = []

        # Para cada semana
        for semana in range(len(temperaturas[0][0])):
            suma_temp = 0
            contador = 0

            # Para cada día
            for dia in range(len(temperaturas[0])):
                temp = temperaturas[i_ciudad][dia][semana]
                suma_temp += temp
                contador += 1

            promedio = suma_temp / contador
            promedios_ciudad.append(promedio)

        promedios[ciudad] = promedios_ciudad

    return promedios


# Ejecutar versión sin numpy
ciudades, dias_semana, semanas, temperaturas = crear_matriz_temperaturas_sin_numpy()
promedios = calcular_promedios_sin_numpy(ciudades, temperaturas)

print("PROMEDIOS (versión sin numpy):")
for ciudad, promedios_sem in promedios.items():
    print(f"\n{ciudad}:")
    for i, promedio in enumerate(promedios_sem, 1):
        print(f"  Semana {i}: {promedio:.2f}°C")