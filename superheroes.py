heroe = {'A': 'Sobaco', 'B': 'Asesino', 'C': 'Capitan', 'D': 'Pezon', 'E': 'trueno', 'F': 'Lobo', 'G': 'Conejo', 'H': 'Halcón', 'I': 'Sargento', 'J': 'Prepucio', 'K': 'El Milagro', 'L': 'El rey', 'M': 'Maestro', 'N': 'Robot', 'O': 'Vigilante', 'P': 'Avispa', 'Q': 'Doctor', 'R': 'Orificio', 'S': 'Pepino', 'T': 'Principe', 'U': 'Tiburón', 'V': 'Aguijón', 'W': 'Fantasma', 'X': 'Agente', 'Y': 'Tornado', 'Z': 'Brujo'}
apellido = {'A': 'Elástico', 'B': 'Carmesí', 'C': 'Radiactivo', 'D': 'Volador', 'E': 'Espacial', 'F': 'Letal', 'G': 'Flácido', 'H': 'Marciano', 'I': 'Venenoso', 'J': 'Invisible', 'K': 'Mutante', 'L': 'Vengador', 'M': 'Amoroso', 'N': 'Apestoso', 'O': 'Mágico', 'P': 'Gigante', 'Q': 'Nazi', 'R': 'Biónico', 'S': 'Celestial', 'T': 'Sangriento', 'U': 'Rocoso', 'V': 'De Hierro', 'W': 'Psíquico', 'X': 'Maravilla', 'Y': 'Hipster', 'Z': 'Invencible'}
color = {'1': 'Dorado', '2': 'Amarillo', '3': 'Oscuro', '4': 'Verde', '5': 'Blanco', '6': 'Azul', '7': 'Gris', '8': 'Platado', '9': 'Rojo', '0': 'Escarlata'}
poder = {'1': 'Convertir todo en algodón', '2': 'Velocidad de la luz', '3': 'Hablar con animales', '4': 'Super fuerza', '5': 'Control mental', '6': 'Invisibilidad', '7': 'Control del fuego', '8': 'Crear tormentas', '9': 'Convertir agua en cerveza', '10': 'Destruir planetas', '11': 'Saltar 20 metros', '12': 'Volar'}
arma = {'1': 'Bastón', '2': 'Espada', '3': 'Hacha', '4': 'Sombrilla', '5': 'Escudo', '6': 'Barita Mágica', '7': 'Rifle', '8': 'AWP', '9': 'Bat de baseball', '10': 'Cuerda', '11': 'Arco y flecha', '12': 'Guantes de box', '13': 'Sartén', '14': 'Pistola', '15': 'Manopla', '16': 'Chacos ninja', '17': 'Martillo', '18': 'Motosierra', '19': 'Cadenas', '20': 'Destornillador', '21': 'Escoba', '22': 'Dagas', '23': 'Bumerangs', '24': 'Estrellas ninja', '25': 'Extintor', '26': 'Tijeras', '27': 'Destapacaños', '28': 'Lanza misiles', '29': 'Bastón de jockey', '30': 'Cepillo de dientes', '31': 'Espada mágica'}

class Heroe():
    def __init__(self, initial_name, initial_apell, año, mes, dia):
        self.hero = heroe[initial_name]
        self.apell = apellido[initial_apell]
        self.color = color[año]
        self.poder = poder[mes]
        self.arma = arma[dia]

    def descripcion(self):
        print('Soy {} {} {}, mi poder es el {} y voy a luchar contra la injusticia con mi {}'.format(self.hero, self.apell, self.color, self.poder, self.arma))



def nombre():
    val = False
    while not val:
        name = input('Introduce tu nombre y apellido: ').split()
        for i in name:
            for x in i:
                if not validar_nombre(x):
                    nombre()
        val = True

    initial_name = name[0][0].upper()
    initial_apell = name[1][0].upper()
    return initial_name, initial_apell

def validar_nombre(n):
    try:
        nom = float(n)
        return False
    except:
        return True
'''
def validar_fecha(x):
    try:
        a = float(x)
        return True
    except:
        return False

def fecha():
    year = False
    while not year:
        año = input("introduce año de nacimiento: ")
        if len(año) < 4 or not validar_fecha(año):
            year = False
        else:
            year = True
'''   

def crea_heroe():
    hero = nombre()
    date = input('Introducir fecha en formato YYYY MM DD ').split()
    return Heroe(hero[0], hero[1], date[0][-1], date[1], date[2])


hero = crea_heroe()
hero.descripcion()
#heroe_uno = Heroe(hero[0][0], hero[0][1], año, mes, dia)