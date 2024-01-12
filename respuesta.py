import datetime

class Greeter:
    def __init__(self):
        pass

    def greet(self, name):
        # Recortar el input
        name = name.strip()
        
        # Capitalizar la primera letra del nombre
        name = name.capitalize()
        
        # Obtener la hora actual
        current_time = datetime.datetime.now().time()
        
        # Determinar el saludo apropiado según la hora
        if datetime.time(6, 0) <= current_time < datetime.time(12, 0):
            saludo = "Buenos días"
        elif datetime.time(18, 0) <= current_time < datetime.time(22, 0):
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"
        
        # Combinar el saludo con el nombre
        mensaje_saludo = f"{saludo} {name}"
        
        # Registrar en la consola
        print(mensaje_saludo)
        
        # Devolver el mensaje de saludo
        return mensaje_saludo
