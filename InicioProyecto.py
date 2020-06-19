import random

def CreaCedulas():
    numeroCed = random.randint(100000000,799999999)
    cedula = str(numeroCed)
    return cedula
#Falta edad y grupo etario
def listaFormaRostro():
    lista = ["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado","Rectangular"]
    return lista
def listaColoPiel():
    lista = ["Negra","Marrón", "Morena", "Clara", "Blanca"]
    return lista
def listaEmociones():
    lista = ["Enfado","Desprecio","Disgusto","Miedo","Sorpresa","Alegría","Neutral","Tristeza"]
    return lista
def listaDensidadCabello():
    lista = ["Escaso", "Moderado","Abundante"]
    return lista
def listaTexturaCabello():
    lista = ["Lacio","Ondulado","Rizado"]
    return lista
def listaColorCabello():
    lista = ["Negro","Rubio","Café","Castaño","Gris","Blanco"]
    return lista
def listaAccesorios():
    lista = ["Lentes","Aretes","Piercing","Sombrero","Anillo","Collar","Bufanda","Reloj","Brazalete","Pulseras"]
    return lista
def listaGenero():
    lista = ["Femenino", "Masculino"]
    return lista
def listaProvincia():
    lista = ["San José","Alajuela","Cartago","Heredia","Puntarenas","Guanacaste","Limón"]
    return lista
def listaFormaOjos():
    lista = ["Almendrados","Separados", "Redondos", "Caídos", "Saltones","Juntos", "Profundos", "Asiáticos"]
    return lista
def listaColorOjos():
    lista = ["Negro","Castaño","Ámbar","Avellana","Verde", "Azul","Gris"]
    return lista
def listaGrupoEtario():
    lista = ["Bebé", "Niño", "Adolescente","Adulto", "Adulto Mayor"]
    return lista
def listaRopa():
    lista = ["Formal", "Informal", "Casual","Deportivo","Baño", "Etiqueta", "Invierno","Gala","Playa","Disfraz"]
    return lista
def listaCalzado():
    lista = ["botas", "tenis", "zapatilla", "sandalias", "mocasines", "náuticos","pantunflas","vaqueros","tacones","ballerinas"]
    return lista


class FormaRostro():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class ColorPiel():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Emocion():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Genero():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Provincia():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre

class FormaOjos():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class ColorOjos():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Ojos():
    def __init__(self):
        self.forma = ""
        self.color = ""
        return
    def set_forma(self,forma):
        self.forma = forma
        return
    def get_forma(self):
        return self.forma
    def set_color(self,color):
        self.color = color
        return
    def get_color(self):
        return self.color

class TexturaCabello():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class ColorCabello():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class DensidadCabello():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Cabello():
    def __init__(self):
        self.textura = ""
        self.color = ""
        self.densidad = ""
        return
    def set_textura(self,textura):
        self.textura = textura
        return
    def get_textura(self):
        return self.textura
    def set_color(self,color):
        self.color = color
        return
    def get_color(self):
        return self.color
    def set_densidad(self,densidad):
        self.densidad = densidad
        return
    def get_densidad(self):
        return self.densidad

class Accesorio():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Ropa():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Calzado():
    def __init__(self):
        self.nombre = ""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
class Vestuario():
    def __init__(self):
        self.accesorio = ""
        self.ropa = ""
        self.calzado = ""
        return
    def set_accesorio(self,accesorio):
        self.accesorio = accesorio
        return
    def get_accesorio(self):
        return self.accesorio
    def set_ropa(self,ropa):
        self.ropa = ropa
        return
    def get_ropa(self):
        return self.ropa
    def set_calzado(self,calzado):
        self.calzado = calzado
        return
    def get_calzado(self):
        return self.calzado


  #Revisar Clase persona
class persona():
    def __init__(self):
        self.cedula = ""
        self.edad = ""
        self.vestuario = ""
        self.ojos = ""
        self.cabello = ""
        self.colorPiel = ""
        self.genero = ""
        self.formaRostro = ""
        self.emocion = ""
        self.provincia = ""
        return
    def set_cedula(self,cedula):
        self.cedula = cedula
        return
    def get_cedula(self):
        return self.cedula
    def set_edad(self,edad):
        self.edad = edad
        return
    def get_edad(self):
        return self.edad
    def set_vestuario(self,vestuario):
        self.vestuario = vestuario
        return
    def get_vestuario(self):
        return self.vestuario
    def set_ojos(self,ojos):
        self.ojos = ojos
        return
    def get_ojos(self):
        return self.ojos
    def set_cabello(self,cabello):
        self.cabello = cabello
        return
    def get_cabello(self):
        return self.cabello
    def set_colorPiel(self,colorPiel):
        self.colorPiel = colorPiel
        return
    def get_colorPiel(self):
        return self.colorPiel
    def set_genero(self,genero):
        self.genero = genero
        return
    def get_genero(self):
        return self.genero
    def set_formaRostro(self, formaRostro):
        self.formaRostro = formaRostro
        return
    def get_formaRostro(self):
        return self.formaRostro
    def set_emocion(self, emocion):
        self.emocion = emocion
        return
    def get_emocion(self):
        return self.emocion
    def set_provincia(self, provincia):
        self.provincia = provincia
        return
    def get_provincia(self):
        return self.provincia

def creaObjetoFormaRostro():
    listaFormas = []
    Formas = listaFormaRostro()
    for forma in Formas:
        f = FormaRostro()
        f.set_nombre(forma)
        listaFormas.append(f)
    return listaFormas
def creaObjetoColorPiel():
    lista = []
    Colores = listaColoPiel()
    for color in Colores:
        c = ColorPiel()
        c.set_nombre(color)
        lista.append(c)
    return lista
def creaObjetoEmocion():
    lista = []
    Emociones = listaEmociones()
    for emocion in Emociones:
        e = Emocion()
        e.set_nombre(emocion)
        lista.append(e)
    return lista
def creaObjetoGenero():
    lista = []
    Generos = listaGenero()
    for genero in Generos:
        g = Genero()
        g.set_nombre(genero)
        lista.append(g)
    return lista
def creaObjetoProvincia():
    lista = []
    Provincias = listaProvincia()
    for provincia in Provincias:
        p = Provincia()
        p.set_nombre(provincia)
        lista.append(p)
    return lista

def creaObjetoFormaOjos():
    lista = []
    Formas = listaFormaOjos()
    for ojos in Formas:
        o = FormaOjos()
        o.set_nombre(ojos)
        lista.append(o)
    return lista
def creaObjetoColorOjos():
    lista = []
    ColorO = listaColorOjos()
    for color in ColorO:
        co = ColorOjos()
        co.set_nombre(color)
        lista.append(co)
    return lista
def creaObjetoOjos():
    forma = creaObjetoFormaOjos()
    color = creaObjetoColorOjos()
    lista = []
    for formaOjo in forma:
        for colorOjo in color:
            o = Ojos()
            o.set_forma(formaOjo)
            o.set_color(colorOjo)
            lista.append(o)
    return lista

def creaObjetoTexturaCabello():
    lista = []
    Texturas = listaTexturaCabello()
    for textura in Texturas:
        t = TexturaCabello()
        t.set_nombre(textura)
        lista.append(t)
    return lista
def creaObjetoColorCabello():
    lista = []
    ColorC = listaColorCabello()
    for color in ColorC:
        cc = ColorCabello()
        cc.set_nombre(color)
        lista.append(cc)
    return lista
def creaObjetoDensidadCabello():
    lista = []
    Densidades = listaDensidadCabello()
    for densidad in Densidades:
        d = DensidadCabello()
        d.set_nombre(densidad)
        lista.append(d)
    return lista
def creaObjetoCabello():
    textura = creaObjetoTexturaCabello()
    color = creaObjetoColorCabello()
    densidad = creaObjetoDensidadCabello()
    lista = []
    for texturaC in textura:
        for colorC in color:
            for densidadC in densidad:
                c = Cabello()
                c.set_textura(texturaC)
                c.set_color(colorC)
                c.set_densidad(densidadC)
                lista.append(c)
    return lista

def creaObjetoAccesorio():
    lista = []
    accesorios = listaAccesorios()
    for accesorio in accesorios:
        a = Accesorio()
        a.set_nombre(accesorio)
        lista.append(a)
    return lista
def creaObjetoRopa():
    lista = []
    Ropas = listaRopa()
    for ropa in Ropas:
        r = Ropa()
        r.set_nombre(ropa)
        lista.append(r)
    return lista
def creaObjetoCalzado():
    lista = []
    Calzados = listaCalzado()
    for calzado in Calzados:
        c = Calzado()
        c.set_nombre(calzado)
        lista.append(c)
    return lista

#Falta Clase Vestuario