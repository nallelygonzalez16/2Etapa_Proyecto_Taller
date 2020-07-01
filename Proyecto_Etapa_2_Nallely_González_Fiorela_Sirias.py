"""The following commands are for importing the libraries that are used for the development of the program."""
import random
import datetime
from datetime import date

def CreaCedulas():
    """Function that creates a list of 10,000 randomly generated id numbers with a defined range.
       :returns the list called "numeroCed". """
    numeroCed = random.sample(range(100000000,800000000),10000)
    return numeroCed
def listaFormaRostro():
    """Function that stores burned data, in the form of a list containing different face shapes.
       :returns the list called "listaFormaR"."""
    listaFormaR = ["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado","Rectangular"]
    return listaFormaR
def listaColoPiel():
    """Function that stores burned data, in the form of a list containing different skin colors.
       :returns the list called "listaColorP"."""
    listaColorP = ["Negra","Marrón", "Morena", "Clara", "Blanca"]
    return listaColorP
def listaEmociones():
    """Function that stores burned data, in the form of a list containing different emotions.
       :returns the list called "listaEmocion"."""
    listaEmocion = ["Enfado","Desprecio","Disgusto","Miedo","Sorpresa","Alegría","Neutral","Tristeza"]
    return listaEmocion
def listaDensidadCabello():
    """Function that stores burned data, in the form of a list containing different hair densities.
       :returns the list called "listaDensidades"."""
    listaDensidades = ["Escaso", "Moderado","Abundante"]
    return listaDensidades
def listaTexturaCabello():
    """Function that stores burned data, in the form of a list containing different hair textures.
       :returns the list called "listaTexturas"."""
    listaTexturas = ["Lacio","Ondulado","Rizado"]
    return listaTexturas
def listaColorCabello():
    """Function that stores burned data, in the form of a list containing different hair colors.
       :returns the list called "listaColoresC"."""
    listaColoresC = ["Negro","Rubio","Café","Castaño","Gris","Blanco"]
    return listaColoresC
def listaAccesorios():
    """Function that stores burned data, in the form of a list containing different accessories.
       :returns the list called "listaTexturas"."""
    listaAccesorio = ["Lentes","Aretes","Piercing","Sombrero","Anillo","Collar","Bufanda","Reloj","Brazalete","Pulseras"]
    return listaAccesorio
def listaGenero():
    """Function that stores burned data, in the form of a list containing different genres.
       :returns the list called "listaGen "."""
    listaGen = ["Femenino", "Masculino"]
    return listaGen
def listaProvincia():
    """Function that stores burned data, in the form of a list containing different provinces.
       :returns the list called "listaProvin "."""
    listaProvin = ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
    return listaProvin
def listaFormaOjos():
    """Function that stores burned data, in the form of a list containing eyes shapes.
       :returns the list called "listaFormaO"."""
    listaFormaO = ["Almendrados","Separados", "Redondos", "Caídos", "Saltones","Juntos", "Profundos", "Asiáticos"]
    return listaFormaO
def listaColorOjos():
    """Function that stores burned data, in the form of a list containing different eyes colors.
       :returns the list called "listaColorO"."""
    listaColorO = ["Negro","Castaño","Ámbar","Avellana","Verde", "Azul","Gris"]
    return listaColorO
def listaRopa():
    """Function that stores burned data, in the form of a list containing different clothes.
       :returns the list called "listaRop"."""
    listaRop = ["Camisa", "Blusa", "Pantalón","Short","Falda", "Overol", "Vestido","Traje de baño","Camiseta","Disfraz"]
    return listaRop
def listaCalzado():
    """Function that stores burned data, in the form of a list containing different shoes.
       :returns the list called "listaZapatos"."""
    listaZapatos = ["Botas", "Tenis", "Zapatilla", "Sandalias", "Mocasines", "Náuticos","Pantunflas","Vaqueros","Tacones","Ballerinas"]
    return listaZapatos
def listaGrupoEtario():
    """Function that stores burned data, in the form of a list containing different age groups.
       :returns the list called "listaGrupoE"."""
    listaGrupoE = ["Bebé","Niño","Adolescente","Adulto","Adulto Mayor"]
    return listaGrupoE
# .........................................................
class grupoEtario():
    """Creation of the "grupoEtario" class, which allows the creation of an object with the attributes "nombre" and "identificador", type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class FormaRostro():
    """Creation of the "FormaRostro" class, which allows the creation of an object with the attributes "nombre" and "identificador", type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class ColorPiel():
    """Creation of the "ColorPiel" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Emocion():
    """Creation of the "Emocion" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Genero():
    """Creation of the "Genero" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Provincia():
    """Creation of the "Provincia" class, which allows the creation of an object with the attributes "nombre" and "identificador", type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
       
class FormaOjos():
    """Creation of the "FormaOjos" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class ColorOjos():
    """Creation of the "ColorOjos" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Ojos():
    """Creation of the "Ojos" class, which allows the creation of an object with the attributes "forma" and "ojos",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
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
    """Creation of the "TexturaCabello" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class ColorCabello():
    """Creation of the "ColorCabello" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class DensidadCabello():
    """Creation of the "DensidadCabello" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Cabello():
    """Creation of the "DensidadCabello" class, which allows the creation of an object with the attributes "textura" , "color" and "densidad",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
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
    """Creation of the "Accesorio" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Ropa():
    """Creation of the "Ropa" class, which allows the creation of an object with the attributes "nombre" and "identificador",type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Calzado():
    """Creation of the "Calzado" class, which allows the creation of an object with the attributes "nombre" and "identificador".type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.nombre = ""
        self.identificador=""
        return
    def set_nombre(self,nombre):
        self.nombre = nombre
        return
    def get_nombre(self):
        return self.nombre
    def set_identificador(self,id):
        self.identificador = id
        return
    def get_identificador(self):
        return self.identificador
class Vestuario():
    """Creation of the "Vestuario" class, which allows the creation of an object with the attributes :
       "accesorio" :type list
       "ropa" :type list
       "calzado" :type string
       *Contains the respective constructor and methods set: to assign the values to the attributes and get:to return them"""
    def __init__(self):
        self.accesorio = []
        self.ropa = []
        self.calzado = ""
        return
    def set_accesorio(self,accesorio):
        self.accesorio.append(accesorio)
        return
    def get_accesorio(self):
        return self.accesorio
    def set_ropa(self,ropa):
        self.ropa.append(ropa)
        return
    def get_ropa(self):
        return self.ropa
    def set_calzado(self,calzado):
        self.calzado = calzado
        return
    def get_calzado(self):
        return self.calzado
# .........................................................
class Persona():
    """Creation of the "Persona" class.
        This class begins with a constructor method in which the attributes that the object will have and the 
        type of value that they are going to store are established, that is: numbers, lists, strings or others.
        The person class has the following attributes:
            "cedula" :type string                    "colorPiel" :type string                 
            "edad" :type list                        "genero" :type string
            "grupoEtario" :type string               "formaRostro" :type string
            "vestuario" :type list                   "emocion" :type string
            "ojos" :type string                      "provincia" :type string
            "cabello" :type string
        Each attribute in this class has the following methods:
        THE SET METHOD: this receives a value and places it on a certain attribute of the perosna object.
        THE gET METHOD: this is used to access the values ​​of the attributes and to show the value that each 
        attribute has, whether they are numbers, words or others.
        """
    def __init__(self):
        self.cedula = ""
        self.edad = []
        self.grupoEtario=""
        self.vestuario = []
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
    def set_edad(self,año,mes,dia):
        self.edad.append(año)
        self.edad.append(mes)
        self.edad.append(dia)
        return self.edad
    def get_edad(self):
        return self.edad
    def set_grupoEtario(self,grupo):
        self.grupoEtario = grupo
        return
    def get_grupoEtario(self):
        return self.grupoEtario
    def set_vestuario(self,vestuarioPersona):
        self.vestuario.append(vestuarioPersona)
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
# .........................................................
def creaObjetoGrupoEtario():
    """Function that performs the instantiation of the class "grupoEtario" to create the age group objects.
       Invokes the function "listaGrupoEtario" and scrolls through the list , so that each item in the list will be the
       name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
       Stores all created objects in the list called "listaGE"
       :returns the list"""
    listaGE = []
    grupos = listaGrupoEtario()
    contador=1
    for grupo in grupos:
        g = grupoEtario()
        g.set_nombre(grupo)
        g.set_identificador(contador)
        listaGE.append(g)
        contador=contador+1
    return listaGE
def creaObjetoFormaRostro():
    """Function that performs the instantiation of the class "FormaRostro" to create the shapes faces objects.
         Invokes the function "listaFormaRostro" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "listaFormas"
         :returns the list"""
    listaFormas = []
    Formas = listaFormaRostro()
    contador=1
    for forma in Formas:
        f = FormaRostro()
        f.set_nombre(forma)
        f.set_identificador(contador)
        listaFormas.append(f)
        contador=contador+1
    return listaFormas
def creaObjetoColorPiel():
    """Function that performs the instantiation of the class "ColorPiel" to create the skin colors objects.
         Invokes the function "listaColoPiel" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    Colores = listaColoPiel()
    contador=1
    for color in Colores:
        c = ColorPiel()
        c.set_nombre(color)
        c.set_identificador(contador)
        lista.append(c)
        contador=contador+1
    return lista
def creaObjetoEmocion():
    """Function that performs the instantiation of the class "Emocion" to create the emotions objects.
         Invokes the function "listaEmociones" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    Emociones = listaEmociones()
    contador=1
    for emocion in Emociones:
        e = Emocion()
        e.set_nombre(emocion)
        e.set_identificador(contador)
        lista.append(e)
        contador=contador+1
    return lista
def creaObjetoGenero():
    """Function that performs the instantiation of the class "Genero" to create the gender objects.
         Invokes the function "listaGenero" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    Generos = listaGenero()
    contador=1
    for genero in Generos:
        g = Genero()
        g.set_nombre(genero)
        g.set_identificador(contador)
        lista.append(g)
        contador=contador+1
    return lista
def creaObjetoProvincia():
    """Function that performs the instantiation of the class "Provincia" to create the provinces objects.
         Invokes the function "listaProvincia" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    Provincias = listaProvincia()
    contador=1
    for provincia in Provincias:
        p = Provincia()
        p.set_nombre(provincia)
        p.set_identificador(contador)
        lista.append(p)
        contador=contador+1
    return lista

def creaObjetoFormaOjos():
    """Function that performs the instantiation of the class "FormaOjos" to create the eyes shapes objects.
         Invokes the function "listaFormaOjos" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    Formas = listaFormaOjos()
    contador=1
    for ojos in Formas:
        o = FormaOjos()
        o.set_nombre(ojos)
        o.set_identificador(contador)
        lista.append(o)
        contador=contador+1
    return lista
def creaObjetoColorOjos():
    """Function that performs the instantiation of the class "ColorOjos" to create the eyes colors objects.
         Invokes the function "listaColorOjos" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    ColorO = listaColorOjos()
    contador=1
    for color in ColorO:
        co = ColorOjos()
        co.set_nombre(color)
        co.set_identificador(contador)
        lista.append(co)
        contador=contador+1
    return lista
def creaObjetoOjos():
    """Function that performs the instantiation of the class "Ojos" to create the objects eyes.
         It invokes the functions "creaObjetoFormaOjos" and "creaObjetoColorOjos", goes through
         both lists simultaneously, and creates each "ojos" object with different combinations between
         the objects of shapes and color of eyes
         Stores all the objects created in the list called "list
         :returns the list"""
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
    """Function that performs the instantiation of the class "TexturaCabello" to create the hair textures objects.
         Invokes the function "listaTexturaCabello" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    Texturas = listaTexturaCabello()
    contador=1
    for textura in Texturas:
        t = TexturaCabello()
        t.set_nombre(textura)
        t.set_identificador(contador)
        contador=contador+1
        lista.append(t)
    return lista
def creaObjetoColorCabello():
    """Function that performs the instantiation of the class "ColorCabello" to create the hair colors objects.
         Invokes the function "listaColorCabello" and scrolls through the list , so that each item in the list will be the
         name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
         Stores all created objects in the list called "lista"
         :returns the list"""
    lista = []
    ColorC = listaColorCabello()
    contador=1
    for color in ColorC:
        cc = ColorCabello()
        cc.set_nombre(color)
        cc.set_identificador(contador)
        lista.append(cc)
        contador=contador+1
    return lista
def creaObjetoDensidadCabello():
    """Function that performs the instantiation of the class "DensidadCabello" to create the hair densitys objects.
          Invokes the function "listaDensidadCabello" and scrolls through the list , so that each item in the list will be the
          name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
          Stores all created objects in the list called "lista"
          :returns the list"""
    lista = []
    Densidades = listaDensidadCabello()
    contador=1
    for densidad in Densidades:
        d = DensidadCabello()
        d.set_nombre(densidad)
        d.set_identificador(contador)
        lista.append(d)
        contador=contador+1
    return lista
def creaObjetoCabello():
    """Function that performs the instantiation of the class "Cabello" to create the objects Cabello.
         It invokes the functions "creaObjetoTexturaCabello", "creaObjetoColorCabello" and "creaObjetoDensidadCabello",
         goes through all the lists simultaneously, and creates each "Cabello" object with different combinations between
         of hair color, density and texture.
         Stores all the objects created in the list called "list
         :returns the list"""
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
    """Function that performs the instantiation of the class "Accesorio" to create the accesories objects.
          Invokes the function "listaAccesorios" and scrolls through the list , so that each item in the list will be the
          name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
          Stores all created objects in the list called "lista"
          :returns the list"""
    lista = []
    accesorios = listaAccesorios()
    contador=1
    for accesorio in accesorios:
        a = Accesorio()
        a.set_nombre(accesorio)
        a.set_identificador(contador)
        lista.append(a)
        contador=contador+1
    return lista
def creaObjetoRopa():
    """Function that performs the instantiation of the class "Ropa" to create the clothes objects.
          Invokes the function "listaRopa" and scrolls through the list , so that each item in the list will be the
          name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
          Stores all created objects in the list called "lista"
          :returns the list"""
    lista = []
    Ropas = listaRopa()
    contador=1
    for ropa in Ropas:
        r = Ropa()
        r.set_nombre(ropa)
        r.set_identificador(contador)
        lista.append(r)
        contador=contador+1
    return lista
def creaObjetoCalzado():
    """Function that performs the instantiation of the class "Calzado" to create the shoes objects.
          Invokes the function "listaCalzado" and scrolls through the list , so that each item in the list will be the
          name of the object, and declares a counter initialised at 1 and incremented by 1, to assign an identifier to each of the elements.
          Stores all created objects in the list called "lista"
          :returns the list"""
    lista = []
    Calzados = listaCalzado()
    contador=1
    for calzado in Calzados:
        c = Calzado()
        c.set_nombre(calzado)
        c.set_identificador(contador)
        lista.append(c)
        contador=contador+1
    return lista
def crearObjetoVesturio():
    conjuntoVestuario=[]
    calzado=creaObjetoCalzado()
    ropa=creaObjetoRopa()
    accesorios=creaObjetoAccesorio()
    for zapato in calzado:
        usados=[]
        v=Vestuario()
        v.set_calzado(zapato)
        cantidadAccesorios=random.randint(1,5)
        cantidadAcce=0
        while cantidadAcce <= cantidadAccesorios:
            accesorioPersona=random.choice(accesorios)
            if accesorioPersona not in usados:
                usados.append(accesorioPersona)
                cantidadAcce=cantidadAcce+1
                v.set_accesorio(accesorioPersona)
        cantidadRopa=random.randint(1,3)
        cantidadRo=0
        while cantidadRo <= cantidadRopa:
            ropaPersona=random.choice(ropa)
            if ropaPersona not in usados:
                usados.append(ropaPersona)
                cantidadRo=cantidadRo+1
                v.set_ropa(ropaPersona)
        conjuntoVestuario.append(v)
    return conjuntoVestuario
# .........................................................
def CalcularGrupoEtario(año,mes,dia):
    """"Function that calculates the exact age of the person and assigns an age group depending on the age
       By means of a series of conditions and "if" comparisons
       :parameter "year,month,day" date of birth of the person
       :returns the object of the age group corresponding to the age"""
    fechaNacimiento= date(year=año,month=mes,day=dia)
    today=date.today()
    age = today.year - fechaNacimiento.year - ((today.month, today.day) < (fechaNacimiento.month, fechaNacimiento.day))
    grupoEtario = creaObjetoGrupoEtario()
    if age == 0 and age <=5:
        return grupoEtario[0]
    elif age >= 5 and age <= 11:
        return grupoEtario[1]
    elif age > 11 and age <= 17:
        return grupoEtario[2]
    elif age >= 18 and age <=64:
        return grupoEtario[3]
    else:
        return grupoEtario[4]

def CalcularProvincia(cedula):
    """"The function assign a province for person depending on the first number of the id.
        By means of a series of "if" conditions and comparisons.
       :parameter : "cedula"  the id number of a person who will be assigned a province
       :returns the province object that corresponds to the first number of the id
       :exception the id number must be converted to string type, in order to use the first position"""
    cedulaPersona = str(cedula)
    primerNum = cedulaPersona[0]
    provincias=creaObjetoProvincia()
    for provincia in provincias:
        if primerNum == "1":
            if "San José" == provincia.get_nombre():
                return provincia
        elif primerNum == "2":
            if "Alajuela" == provincia.get_nombre():
                return provincia
        elif primerNum == "3":
            if "Cartago" == provincia.get_nombre():
                return provincia
        elif primerNum == "4":
            if "Heredia" == provincia.get_nombre():
                return provincia
        elif primerNum == "5":
            if "Guanacaste" == provincia.get_nombre():
                return provincia
        elif primerNum == "6":
            if "Puntarenas" == provincia.get_nombre():
                return provincia
        elif primerNum == "7":
            if "Limón" == provincia.get_nombre():
                return provincia

def CrearObjetoPersona(cedulas):
    """This function performs the instantiation of the "Person" class to create all the people that will be used for development
        of the program, this is done by going through a list and in this way create a person with each element.
        :parameter: receives as a parameter a list of ID cards.
       :returns a list of people objects with all their attributes.
       :exception: has no exceptions"""
    Personas=[]
    for cedula in cedulas:
        p=Persona()
        p.set_cedula(cedula)
        años=random.randint(1965,2019)
        meses=random.randint(1,12)
        if meses == 2:
            dias=random.randint(1,28)
            p.set_edad(años,meses,dias)
        else:
            dias=random.randint(1,30)
            p.set_edad(años,meses,dias)
        grupo=CalcularGrupoEtario(años,meses,dias)
        p.set_grupoEtario(grupo)
        vestuarioPersona=random.choice(crearObjetoVesturio())
        p.set_vestuario(vestuarioPersona)
        ojosPersona=random.choice(creaObjetoOjos())
        p.set_ojos(ojosPersona)
        peloPersona=random.choice(creaObjetoCabello())
        p.set_cabello(peloPersona)
        colorPersona=random.choice(creaObjetoColorPiel())
        p.set_colorPiel(colorPersona)
        generoPersona=random.choice(creaObjetoGenero())
        p.set_genero(generoPersona)
        caraPersona=random.choice(creaObjetoFormaRostro())
        p.set_formaRostro(caraPersona)
        emocion=random.choice(creaObjetoEmocion())
        p.set_emocion(emocion)
        provincia=CalcularProvincia(cedula)
        p.set_provincia(provincia)
        Personas.append(p)
    return Personas
cedulas=CreaCedulas()
TotalPersonas=CrearObjetoPersona(cedulas)

def CrearPersonasAuto():
    """This function is in charge of receiving the new number of people who
    The administrator wants to create. These are created randomly so it makes
    the call of the previous function called "CrearObjetoPersona()".
    Since the identification numbers must be unique for each person, this function
    uses the function "CreaCedulas()" that returns a list with numbers
    randomly and is responsible for verifying that the new ids have not been
    used, to send the new list of numbers as a function parameter
    "CreaObjetoPersona()" and then add them to the list with the total number of people."""
    print(" ¡El programa ya cuenta con una cantidad de",len(TotalPersonas),"personas!","\n")
    cedulasNuevas= int(input("► Digite la cantidad de personas que desea crear automáticamente: "))
    listaCedulasUsadas=[]
    for persona in TotalPersonas:
        listaCedulasUsadas.append(persona.get_cedula())
    cantidadPersonas=0
    cantidadCedulas=CreaCedulas()
    cedulasPermitidas=[]
    while cantidadPersonas < cedulasNuevas:
        cedula=random.choice(cantidadCedulas)
        if cedula not in listaCedulasUsadas:
            listaCedulasUsadas.append(cedula)
            cedulasPermitidas.append(cedula)
            cantidadPersonas=cantidadPersonas+1
    nuevas=CrearObjetoPersona(cedulasPermitidas)
    for personaNueva in nuevas:
        TotalPersonas.append(personaNueva)
    print("\n"," ¡Se han creado ",len(nuevas)," personas de forma exitosa.")
    print(" ¡El programa cuenta con un nuevo total de:",len(TotalPersonas),"personas!")
    print("\033[1;36m" + "───────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def BuscarPersona(muestra,seleccion):
    """
    This function is responsible for searching within a list of five people who are
    used as a sample, the person the administrator chooses to modify.
    At the same time, it returns to the selected person, who has the form of
    object to make the desired changes.
    :parameter: Receives the list with the five sample people and the variable 
                that contains the number of the person that the administrator chose
    :returns only the item in the list that corresponds to the person that the 
             administrator echoed
    :exception: If the number that the administrator digits does not correspond to 
                any item in the sample list, the program is returned to the 
                function called "MenuModificarPersona()"
    """
    if seleccion == "1":
        personaModificar= muestra[0]
    elif seleccion == "2":
        personaModificar= muestra[1]
    elif seleccion == "3":
        personaModificar= muestra[2]
    elif seleccion == "4":
        personaModificar= muestra[3]
    elif seleccion == "5":
        personaModificar= muestra[4]
    else:
        print("¡El número de persona digitado no existe!")
        print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
        MenuModificarPersona()
    return personaModificar

def MenuModificarPersona():
    """
    This function is responsible for showing the administrator the sample of the five 
    people so that they can choose one to modify it. They call the "BuscarPersona()" function to
    know exactly which person to modify.
    In the same way it shows you the menu with the options that you can modify
    of the information of the chosen person.
    : parameter: has no parameter
    : returns: nothing return
    : exception: if the administrator does not select any of the menu options
                to modify, the program closes automatically.
    """
    muestra=[]
    cantidad=1
    while cantidad <= 5:
        personas=random.choice(TotalPersonas)
        muestra.append(personas)
        cantidad= cantidad +1
    print("                        ╓──────────────────────────────────╖\n"
          "                        ║       PERSONAS DE MUESTRA        ║\n"
          "                        ╟──────────────────────────────────╢\n"
          "                        ║      ► 1) Persona número 1       ║\n"
          "                        ║      ► 2) Persona número 2       ║\n"
          "                        ║      ► 3) Persona número 3       ║\n"
          "                        ║      ► 4) Persona número 4       ║\n"
          "                        ║      ► 5) Persona número 5       ║\n"
          "                        ╙──────────────────────────────────╜")
    seleccion=input("Digite el número correspondiente a la persona que desea modificar: ")
    persona=BuscarPersona(muestra,seleccion)
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    print("        ╓─────────────────────────────────────────────────────────────────────╖\n"
          "        ║                     OPCIONES PARA MODIFICAR                         ║\n"
          "        ╟─────────────────────────────────────────────────────────────────────╢\n"
          "        ║  ► 1) Lista de ropa: agregar ropa a lista de ropa.                  ║\n"
          "        ║  ► 2) Lista de accesorios: agregar accesorio a lista de accesorios. ║\n"
          "        ║  ► 3) Calzado: cambiar el existente por otra opción                 ║\n"
          "        ║  ► 4) Cancelar acción y volver a menu principal                     ║\n"
          "        ╙─────────────────────────────────────────────────────────────────────╜\n")
    try:
        opcionModificar = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))
        print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
        if opcionModificar == 1:
            ModificarListaRopa(persona)
        elif opcionModificar == 2:
            ModificarListaAccesorios(persona)
        elif opcionModificar == 3:
            ModificarCalzado(persona)
        elif opcionModificar ==4:
            login()
    except ValueError:
        print("El programa ha finalizado")
        exit
    return

def ModificarListaRopa(persona):
    """
    This function is responsible for modifying the clothing list by adding items to the list
    that the selected person has. This shows the administrator the list
    of the clothing the person owns and then shows you the list of clothing options that you can choose from and then add it to the person's clothing.
    : parameter: receives the person to modify
    : returns: nothing is returned
    : exceptions: has no exceptions
    """
    Ropa=creaObjetoRopa()
    print("\n","La persona tiene las siguientes prendas:")
    for vestuario in persona.get_vestuario():
        for ropa in vestuario.get_ropa():
            print("     ►",ropa.get_nombre())
    print("                    ╓──────────────────────────────────────────╖\n"
          "                    ║     OPCIONES DE PRENDAS PARA AGREGAR     ║\n"
          "                    ╟──────────────────────────────────────────╢\n"
          "                    ║    ► 1) Camisa       ► 6) Overol         ║\n"
          "                    ║    ► 2) Blusa        ► 7) Vestido        ║\n"
          "                    ║    ► 3) Pantalón     ► 8) Traje de baño  ║\n"
          "                    ║    ► 4) Short        ► 9) Camiseta       ║\n"
          "                    ║    ► 5) Falda        ► 10) Disfraz       ║\n"
          "                    ╙──────────────────────────────────────────╜\n")
    prendaNueva=int(input("Digite el número correspodiente a la prenda que desea agregar: "))
    for prenda in Ropa:
        if prendaNueva == prenda.identificador:
            elegida=prenda
    for vestuario in persona.get_vestuario():
        for ropa in vestuario.get_ropa():
            if elegida.get_identificador() == ropa.get_identificador():
                bandera=False
                break
            else:
                bandera=True
    if bandera == False:
        print("\n","La persona ya cuenta con la prenda elegida.")
        print("\n","Por favor, digite una prenda que no esté en la lista de la persona.")
        print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
        ModificarListaRopa(persona)
    else:
        vestuario.set_ropa(elegida)
        print("\n","Se ha elegido la prenda", elegida.get_nombre(),", ahora la persona tiene las siguientes prendas: ")
        for vestuario in persona.get_vestuario():
            for ropa in vestuario.get_ropa():
                print("     ►",ropa.get_nombre())
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')   
    MenuSalida()
    return

def ModificarListaAccesorios(persona):
    """
    This function is responsible for modifying the accessories list by adding items to the list
    that the selected person has. This shows the administrator the list
    of the accessories the person owns and then shows you the list of accessories options that you can 
    choose from and then add it to the person's accessories.
    : parameter: receives the person to modify
    : returns: nothing is returned
    : exceptions: has no exceptions
    """
    accesorios=creaObjetoAccesorio()
    print("\n","La persona tiene los siguientes accesorios:")
    for vestuario in persona.get_vestuario():
        for ACCESORIO in vestuario.get_accesorio():
            print("     ►",ACCESORIO.get_nombre())
    print("                    ╓──────────────────────────────────────────╖\n"
          "                    ║   OPCIONES DE ACCESORIOS PARA AGREGAR    ║\n"
          "                    ╟──────────────────────────────────────────╢\n"
          "                    ║    ► 1) Lentes         ► 6) Collar       ║\n"
          "                    ║    ► 2) Aretes         ► 7) Bufanda      ║\n"
          "                    ║    ► 3) Piercing       ► 8) Reloj        ║\n"
          "                    ║    ► 4) Sombrero       ► 9) Brazalete    ║\n"
          "                    ║    ► 5) Anillo         ► 10) Pulseras    ║\n"
          "                    ╙──────────────────────────────────────────╜\n")

    accesorioNuevo=int(input("Digite el número correspondiente al accesorio que desea agregar: "))
    for accesorio in accesorios:
        if accesorioNuevo == accesorio.get_identificador():
            elegido=accesorio
    for vestuario in persona.get_vestuario():
        for accesori in vestuario.get_accesorio():
            if elegido.get_identificador() == accesori.get_identificador():
                bandera=False
                break
            else:
                bandera=True
    if bandera == False:
        print("\n","La persona ya cuenta con el accesorios elegido.")
        print("\n","Por favor, digite un accesorio que no esté en la lista de la persona.")
        print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
        ModificarListaAccesorios(persona)
    else:
        vestuario.set_accesorio(elegido)
        print("\n","Se ha elegido el accesorio", elegido.get_nombre(),", ahora la persona tiene los siguientes accesorios: ")
        for vestuario in persona.get_vestuario():
            for ACCESORIO in vestuario.get_accesorio():
                print("     ►",ACCESORIO.get_nombre())
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def ModificarCalzado(persona):
    """
    This function is responsible for modifying the shoes list by adding items to the list that the selected person has. 
    This shows the administrator the list of the shoes the person owns and then shows you the shoe's list options that you can 
    choose from and then add it to the person's shoes.
    : parameter: receives the person to modify
    : returns: nothing is returned
    : exceptions: has no exceptions
    """    
    calzados = creaObjetoCalzado()
    for vestuario in persona.get_vestuario():
        print("\n","     ► La persona tiene el calzado:",vestuario.get_calzado().get_nombre(),"\n","\n")
    print("                    ╓──────────────────────────────────────────╖\n"
          "                    ║    OPCIONES DE CALZADO PARA CAMBIAR      ║\n"
          "                    ╟──────────────────────────────────────────╢\n"
          "                    ║    ► 1) Botas         ► 6) Náuticos      ║\n"
          "                    ║    ► 2) Tenis         ► 7) Pantunflas    ║\n"
          "                    ║    ► 3) Zapatilla     ► 8) Vaqueros      ║\n"
          "                    ║    ► 4) Sandalias     ► 9) Tacones       ║\n"
          "                    ║    ► 5) Mocasines     ► 10) Ballerinas   ║\n"
          "                    ╙──────────────────────────────────────────╜\n")

    calzadoNuevo = int(input("Digite el número correspondiente al calzado que desea modificar: "))
    for calzado in calzados:
        if calzadoNuevo == calzado.identificador:
            for vestuario in persona.get_vestuario():
                if calzado.identificador == vestuario.get_calzado().get_identificador():
                    print("\n","La persona ya cuenta con el calzado.")
                    print("\n","Digite uno diferente al que la persona posee.")
                    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
                    ModificarCalzado(persona)
                else:
                    vestuario.set_calzado(calzado)
                    print("\n","\n","     ► El nuevo calzado de la persona es:", calzado.get_nombre(),"\n","\n")
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def CalcularCantidades(lista):
    """
    This function receives a list of people and has counters with the names of each of the provinces, which you increase
    only when the person belongs to that group, and then add those counters to a list in a certain order.
    When finished, use those amounts to calculate the percentages that each of these amounts represents of the total number of people and
    it adds them to another list in the same order in which the number of people by province is ordered.
    Finally add both lists to another list to return it.
    : parameter: receive a list with people objects
    : returns: returns the list with quantities and percentages
    : exceptions: has no exceptions
    """
    sanJose=0
    alajuela=0
    cartago=0
    heredia=0
    guanacaste=0
    puntarena=0
    limon=0
    for persona in lista:
        if persona.get_provincia().get_identificador() == 1:
            sanJose= sanJose+1
        elif persona.get_provincia().get_identificador() == 2:
            alajuela= alajuela+1
        elif persona.get_provincia().get_identificador() == 3:
            cartago= cartago+1
        elif persona.get_provincia().get_identificador() == 4:
            heredia= heredia+1
        elif persona.get_provincia().get_identificador() == 5:
            guanacaste= guanacaste+1
        elif persona.get_provincia().get_identificador() == 6:
            puntarena= puntarena+1
        elif persona.get_provincia().get_identificador() == 7:
            limon= limon+1
    provincias=[sanJose,alajuela,cartago,heredia,guanacaste,puntarena,limon]
    porcentajes=[]
    for provincia in provincias:
        porcentaje = (provincia / len(lista)) * 100
        porcentajes.append(porcentaje)
    cantidades = [provincias, porcentajes]
    return cantidades

def InformeAccesorios():
    """
    This function shows the analyst a list of accessories to choose from. The function also displays a report on the number of people who use that accessory, according to their gender and province.
    the percentages representing these quantities, this is done through the function called "CalcularCantidades()" and at the end
    Shows the total number of people using the accessories chosen above, including men and women.
    : parameter: has no parameters
    : returns: nothing is returned
    : exceptions: has no exceptions
    """
    print("                     ╓──────────────────────────────────────────╖\n"
          "                     ║         ACCESORIOS A CONSULTAR           ║\n"
          "                     ╟──────────────────────────────────────────╢\n"
          "                     ║    ► 1) Lentes        ► 6) Collar        ║\n"
          "                     ║    ► 2) Aretes        ► 7) Bufanda       ║\n"
          "                     ║    ► 3) Piercing      ► 8) Reloj         ║\n"
          "                     ║    ► 4) Sombrero      ► 9) Brazalete     ║\n"
          "                     ║    ► 5) Anillo        ► 10) Pulseras     ║\n"
          "                     ╙──────────────────────────────────────────╜")
    opcionAccesorio = int(input("Ingrese el número correspondiente al accesorio que desea consultar: "))
    accesorios = creaObjetoAccesorio()
    for accesorio in accesorios:
        if opcionAccesorio == accesorio.get_identificador():
            accesorioCorrecto=accesorio.get_nombre()
            print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
            print("                                                  ",accesorioCorrecto)
    accesorioelegido = []
    for persona in TotalPersonas:
        for vestuario in persona.get_vestuario():
            for ACCESORIO in vestuario.get_accesorio():
                if ACCESORIO.get_identificador() == opcionAccesorio:
                    accesorioelegido.append(persona)
    masculino = []
    femenino = []
    for persona in accesorioelegido:
        if persona.get_genero().get_identificador() == 1:
            femenino.append(persona)
        else:
            masculino.append(persona)
    Pronvincias = listaProvincia()
    listaFemenino = CalcularCantidades(femenino)
    i = 0
    print("     Género: Femenino ")
    print("                       ┌──────────────────┬───────────────────────────┬──────────────┐")
    print("                       |", "{:^17}{:^1}{:^25}{:^5}{:^10}".format("Provincia","|","Cantidad de personas","|","Porcentaje  |"))
    print("                       ├──────────────────┼───────────────────────────┼──────────────┤")
    i = 0
    while i < len(Pronvincias):
        print("                       |", "{:^17}{:^1}{:^25}{:^5}{:^10}".format(Pronvincias[i],"|", listaFemenino[0][i],"|","{0:.3f}".format(listaFemenino[1][i])+" %    |"))
        i = i + 1
    print("                       ├──────────────────┼───────────────────────────┼──────────────┤")
    print("                       |","{:^17}{:^1}{:^25}{:^5}{:^10}".format("Total Femeninas","|", len(femenino), "|", "   100 %    |"))
    print("                       └──────────────────┴───────────────────────────┴──────────────┘")
    listaMasculino = CalcularCantidades(masculino)
    print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
    print("     Género: Masculino ")
    print("                       ┌──────────────────┬───────────────────────────┬──────────────┐")
    print("                       |", "{:^17}{:^1}{:^25}{:^5}{:^10}".format("Provincia","|","Cantidad de personas","|","Porcentaje  |"))
    print("                       ├──────────────────┼───────────────────────────┼──────────────┤")
    x = 0
    while x < len(Pronvincias):
        print("                       |", "{:^17}{:^1}{:^25}{:^5}{:^10}".format(Pronvincias[x],"|", listaMasculino[0][x],"|","{0:.3f}".format(listaMasculino[1][x])+" %    |"))
        x = x + 1
    print("                       ├──────────────────┼───────────────────────────┼──────────────┤")
    print("                       |","{:^17}{:^1}{:^25}{:^5}{:^10}".format("Total Masculinos","|", len(masculino), "|", "   100 %    |"))
    print("                       └──────────────────┴───────────────────────────┴──────────────┘")
    print("     Total de personas que usan ",accesorioCorrecto,":",len(accesorioelegido),"\n",)
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def ElegirCaracteristicas():
    """
    This function is responsible for showing the different options that the analyst must choose between different aspects,
    so you can choose one by one the characteristic you want a person to possess.
    These are saved in the variables and then, through comparisons, only those who meet all the requirements are added to the list.
    characteristics requested by the analyst.
    : parameter: has no parameters
    : returns: the list with people who meet all the characteristics
    : exceptions: has no exceptions
    """
    print("\n","¡Por favor elija los números correspodientes a cada una de las características que desea consultar!\n")
    try:
        print("                    ╓──────────────────────────────────────────╖\n"
              "                    ║                EMOCIONES                 ║\n"
              "                    ╟──────────────────────────────────────────╢\n"
              "                    ║    ► 1) Enfado         ► 5) Sorpresa     ║\n"
              "                    ║    ► 2) Desprecio      ► 6) Alegría      ║\n"
              "                    ║    ► 3) Disgusto       ► 7) Neutral      ║\n"
              "                    ║    ► 4) Miedo          ► 8) Tristeza     ║\n"
              "                    ╙──────────────────────────────────────────╜")
        opcionEmocion = int(input("     Ingrese el número correspondiente a la emoción : "))
        print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
        print("                    ╓──────────────────────────────────────────╖\n"
              "                    ║                PROVINCIAS                ║\n"
              "                    ╟──────────────────────────────────────────╢\n"
              "                    ║   ► 1) San José       ► 5) Guanacaste    ║\n"
              "                    ║   ► 2) Alajuela       ► 6) Puntarenas    ║\n"
              "                    ║   ► 3) Cartago        ► 7) Limón         ║\n"
              "                    ║   ► 4) Heredia                           ║\n"
              "                    ╙──────────────────────────────────────────╜")
        opcionProvincia = int(input("     Ingrese el número correspondiente a la provincia: "))
        print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
        print("                    ╓──────────────────────────────────────────╖\n"
              "                    ║                  GÉNERO                  ║\n"
              "                    ╟──────────────────────────────────────────╢\n"
              "                    ║    ► 1) Femenino      ► 2) Masculino     ║\n"
              "                    ╙──────────────────────────────────────────╜")
        opcionGenero = int(input("     Ingrese el número correspondiente al género: "))
        print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
        print("                    ╓──────────────────────────────────────────╖\n"
              "                    ║              COLOR DE PIEL               ║\n"
              "                    ╟──────────────────────────────────────────╢\n"
              "                    ║       ► 1) Negra         ► 4) Clara      ║\n"
              "                    ║       ► 2) Marrón        ► 5) Blanca     ║\n"
              "                    ║       ► 3) Morena                        ║\n"
              "                    ╙──────────────────────────────────────────╜")
        opcionColor = int(input("     Ingrese el número correspondiente al color de piel: "))
        print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
        print("                    ╓──────────────────────────────────────────╖\n"
              "                    ║             FORMA DE ROSTRO              ║\n"
              "                    ╟──────────────────────────────────────────╢\n"
              "                    ║    ► 1) Redondo      ► 4) Cuadrado       ║\n"
              "                    ║    ► 2) Alargado     ► 5) Ovalado        ║\n"
              "                    ║    ► 3) Corazón      ► 6) Rectangular    ║\n"
              "                    ╙──────────────────────────────────────────╜")
        opcionForma = int(input("     Ingrese el número correspondiente a la forma del rostro: "))
        print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
        print("                    ╓──────────────────────────────────────────╖\n"
              "                    ║               GRUPO ETARIO               ║\n"
              "                    ╟──────────────────────────────────────────╢\n"
              "                    ║   ► 1) Bebé          ► 4) Adulto         ║\n"
              "                    ║   ► 2) Niño          ► 5) Adulto Mayor   ║\n"
              "                    ║   ► 3) Adolescente                       ║\n"
              "                    ╙──────────────────────────────────────────╜")
        opcionGrupo = int(input("     Ingrese el número correspondiente al grupo etario: "))
        print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
    except ValueError:
        print("ERROR, no ingresó los números indicados")
        consultaPersona()
    listaPersonas = []
    for persona in TotalPersonas:
        if persona.get_emocion().get_identificador() == opcionEmocion:
            if persona.get_provincia().get_identificador() == opcionProvincia:
                if persona.get_genero().get_identificador() == opcionGenero:
                    if persona.get_colorPiel().get_identificador() == opcionColor:
                        if persona.get_formaRostro().get_identificador() == opcionForma:
                            if persona.get_grupoEtario().get_identificador() == opcionGrupo:
                                listaPersonas.append(persona)
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    return listaPersonas

def consultaPersona():
    """
    Function that is responsible for calling the "Choose characteristics ()" function to have a list of people who only meet the 
    characteristics desired by the analyst. If the list is empty, it indicates that there are no people who comply with everything requested
    and if the list has any element, the function goes through that list and of each person that is in that list it will only 
    show the attributes that are requested.
    : parameter: has no parameters
    : returns: nothing is returned
    : exceptions: has no exceptions
    """
    Personas = ElegirCaracteristicas()
    if len(Personas) == 0:
        print("\n  ¡No existen personas registradas en la base de datos que cumplan esas características!\n")
    else:
        for persona in Personas:
            listaRopa = []
            listaAccesorios = []
            for vestuario in persona.get_vestuario():
                calzado = vestuario.get_calzado()
                for ropa in vestuario.get_ropa():
                    listaRopa.append(ropa.get_nombre())
                for accesorio in vestuario.get_accesorio():
                    listaAccesorios.append(accesorio.get_nombre())
                    accesorio.get_nombre()
            print("\n","\033[1;35m" + "      ──────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
            print("                          Cédula: ", persona.get_cedula())
            print("\033[1;35m" + "       --------------------------------------------------------------------------------------" + '\033[0;m')
            print("          Vestuario:")
            print("                    Ropa:",  (" / ".join(listaRopa)))
            print("                    Accesorios:",  (" / ".join(listaAccesorios)))
            print("                    Calzado:",calzado.get_nombre())
            print("          Ojos:")
            print("                    Forma:", persona.get_ojos().get_forma().get_nombre())
            print("                    Color:", persona.get_ojos().get_color().get_nombre())
            print("         Cabello:")
            print("                    Color:", persona.get_cabello().get_color().get_nombre())
            print("                    Textura:", persona.get_cabello().get_textura().get_nombre())
            print("                    Densidad:", persona.get_cabello().get_densidad().get_nombre())
            print("\033[1;35m" + "      ──────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def FuncionesAdmi():
    """
    Function that is responsible for displaying the functions that can be performed by the 
    administrator, gives you the option to choose the action you want to perform and then invokes the different
    functions depends on what the user chooses.
    : parameters: does not receive any parameters.
    : renorta: nothing comes back
    : exceptions: if the administrator does not enter a number in the program, 
        it will return to the start of the function called "FuncionesAdmi()"
    """
    print("                ╔═══════════════════════════════════════════════════╗\n"
          "                ║                 MENÚ ADMINISTRADOR                ║\n"
          "                ╠═══════════════════════════════════════════════════╣\n"
          "                ║     Ingrese 1 para crear persona automáticamente  ║\n"
          "                ║     Ingrese 2 para modificar a una persona        ║\n"
          "                ║     Ingrese 3 para regresar a menú principal      ║\n"
          "                ╚═══════════════════════════════════════════════════╝")
    try:
        opcioParaAdmi = int(input("Ingrese el número correspondiente a la acción que desea realizar: "))
        if opcioParaAdmi == 1:
            print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
            CrearPersonasAuto()
        elif opcioParaAdmi ==2:
            print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
            MenuModificarPersona()
        elif opcioParaAdmi ==3:
            login()
    except ValueError:
        print("Por favor ingrese un dígito")
        FuncionesAdmi()
    return

def FuncionesAnalista():
    """
    Function that is responsible for displaying the functions that can be performed by the 
    analist, gives you the option to choose the action you want to perform and then invokes the different
    functions depends on what the analist chooses.
    : parameters: does not receive any parameters.
    : renorta: nothing comes back
    : exceptions: if the administrator does not enter a number in the program, 
    it will return to the start of the function called "FuncionesAnalista()"
    """
    print("         ╓────────────────────────────────────────────────────────────────────╖\n"
        "         ║                 Opciones de informes a consultar                   ║\n"
        "         ╟────────────────────────────────────────────────────────────────────╢\n"
        "         ║   ► 1) Cantidad y los porcentajes de las personas que usan un      ║\n"
        "         ║        determinado accesorio según el género y la provincia.       ║\n"
        "         ║                                                                    ║\n"
        "         ║   ► 2) Consultar la información de las personas que cumplan        ║\n"
        "         ║        con una serie de características elegidas por el analista.  ║\n"
        "         ║                                                                    ║\n"
        "         ║   ► 3) Cancelar acción y volver a menú principal.                  ║\n"
        "         ╙────────────────────────────────────────────────────────────────────╜")
    try:
        opcionModificar = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))
        print("\n")
        print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
        if opcionModificar == 1:
            InformeAccesorios()
        elif opcionModificar == 2:
            consultaPersona()
        elif opcionModificar == 3:
            login()
    except ValueError:
        print("El programa ha finalizado")
        exit
    return

def MenuSalida():
    """
    Function responsible for displaying an output menu which will be presented every time any of the analyst functions are performed
    or from the administrator and then invokes the different functions depends on what the user chooses.
    : parameter: has no parameters
    : returns: nothing is returned
    : exceptions: has no exceptions
    """
    print("          ╔═════════════════════════════════════════════════════════════════╗\n"
        "          ║                          MENÚ DE SALIDA                         ║\n"
        "          ╠═════════════════════════════════════════════════════════════════╣\n"
        "          ║    Ingrese 1 para ingresar a las funciones del ADMINISTRADOR    ║\n"
        "          ║    Ingrese 2 para ingresar a las funciones del ANALISTA         ║\n"
        "          ║    Ingrese 3 para volver a MENU PRINCIPAL                       ║\n"
        "          ║    Ingrese 4 para cerrar el programa                            ║\n"
        "          ╚═════════════════════════════════════════════════════════════════╝")
    try:
        opcion=int(input("Ingrese el número correspondiente a la acción que desea realizar: "))
        print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
        if opcion == 1:
            contrasena = input(" ► Por favor, ingrese la contraseña de Administrador: ")
            if contrasenaGlobal(contrasena) == True:
                FuncionesAdmi()
            else:
                print(" ¡CONTRASEÑA INCORRECTA!")
                login()
        elif opcion == 2:
            contrasena = input(" ► Por favor, ingrese la contraseña de Analista: ")
            if contrasenaGlobal(contrasena) == True:
                FuncionesAnalista()
            else:
                print(" ¡CONTRASEÑA INCORRECTA!")
                login()    
        elif opcion == 3:
                login()
        if opcion == 4:
            print("El programa ha finalizado")
            exit
    except ValueError:
        print("Por favor ingrese un dígito")
        login()
    return

def contrasenaGlobal(contra):
    """
    Function that is responsible for verifying if the password is correct or not.
    : parameter: has no parameters
    : returns: true if the password is correct and false if it is incorrect.
    : exceptions: has no exceptions   
    """
    if contra == "Etapa2":
        return True
    else:
        return False

def login():
    """
    This function is responsible for displaying the main menu, invokes the function to check the password and then invokes the different
    functions depends on what the user chooses.
    : parameter: has no parameters
    : returns: nothing is returned
    : exceptions: has no exceptions
    """
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    print("                       ╔════════════════════════════════════╗\n"
          "                       ║           MENÚ PRINCIPAL           ║\n"
          "                       ╠════════════════════════════════════╣\n"
          "                       ║    Ingrese 1 para Administrador    ║\n"
          "                       ║    Ingrese 2 para Analista         ║\n"
          "                       ║    Ingrese 3 para salir            ║\n"
          "                       ╚════════════════════════════════════╝")
    try:
        opcion=int(input("Ingrese el número correspondiente a la acción que desea realizar: "))
        if opcion == 1:
            print("\n","\033[1;35m" + "Nota: utilice ( Etapa2 ) como contraseña para administrador."+ '\033[0;m')
            contrasena = input(" ► Por favor, ingrese la contraseña de Administrador: ")
            if contrasenaGlobal(contrasena) == True:
                print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
                FuncionesAdmi()
            else:
                print("\n","\033[1;34m" +"¡CONTRASEÑA INCORRECTA!"+ '\033[0;m')
                login()
        if opcion == 2:
            print("\n","\033[1;35m" + "Nota: utilice ( Etapa2 ) como contraseña para analista."+ '\033[0;m')
            contrasena = input(" ► Por favor, ingrese la contraseña de Analista: ")
            if contrasenaGlobal(contrasena) == True:
                print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
                FuncionesAnalista()
            else:
                print("\n","\033[1;34m" +"¡CONTRASEÑA INCORRECTA!"+ '\033[0;m')
                login()
        if opcion == 3:
            print("\n","\033[1;31m" +"EL PROGRAMA HA FINALIZADO"+ '\033[0;m')
    except ValueError:
        print("Por favor ingrese un dígito")
        login()
login()