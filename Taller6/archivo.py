from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        
        direccion_a_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
            "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }

        
        total_temperatura = 0
        total_humedad = 0
        total_presion = 0
        total_velocidad_viento = 0
        direccion_viento_grados = []

        try:
            with open(self.nombre_archivo, 'r') as file:
                # Leer el archivo línea por línea
                for line in file:
                    if line.startswith("Temperatura:"):
                        total_temperatura += float(line.split(":")[1].strip())
                    elif line.startswith("Humedad:"):
                        total_humedad += float(line.split(":")[1].strip())
                    elif line.startswith("Presion:"):
                        total_presion += float(line.split(":")[1].strip())
                    elif line.startswith("Viento:"):
                        viento_info = line.split(":")[1].strip().split(',')
                        velocidad_viento = float(viento_info[0])
                        direccion_viento = viento_info[1]
                        total_velocidad_viento += velocidad_viento
                        direccion_viento_grados.append(direccion_a_grados[direccion_viento])

               
                cantidad_registros = len(direccion_viento_grados)
                temperatura_promedio = total_temperatura / cantidad_registros
                humedad_promedio = total_humedad / cantidad_registros
                presion_promedio = total_presion / cantidad_registros
                velocidad_viento_promedio = total_velocidad_viento / cantidad_registros

              
                direccion_prominente_grados = sum(direccion_viento_grados) / cantidad_registros
                direccion_prominente = None
                min_diferencia = float('inf')

                for direccion, grados in direccion_a_grados.items():
                    diferencia = abs(direccion_prominente_grados - grados)
                    if diferencia < min_diferencia:
                        min_diferencia = diferencia
                        direccion_prominente = direccion

                return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_prominente)

        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no se encontró.")
            return (0.0, 0.0, 0.0, 0.0, "N/A")

archivo = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(archivo)
resultados = datos.procesar_datos()
print("Temperatura promedio:", resultados[0])
print("Humedad promedio:", resultados[1])
print("Presión promedio:", resultados[2])
print("Velocidad promedio del viento:", resultados[3])
print("Dirección predominante del viento:", resultados[4])
