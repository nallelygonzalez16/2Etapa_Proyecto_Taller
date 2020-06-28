import random
import datetime
from datetime import date

def CreaCedulas():
    numeroCed = random.sample(range(100000000,800000000),5000)
    return numeroCed
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
    lista = ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
    return lista
def listaFormaOjos():
    lista = ["Almendrados","Separados", "Redondos", "Caídos", "Saltones","Juntos", "Profundos", "Asiáticos"]
    return lista
def listaColorOjos():
    lista = ["Negro","Castaño","Ámbar","Avellana","Verde", "Azul","Gris"]
    return lista
def listaRopa():
    lista = ["Camisa", "Blusa", "Pantalón","Short","Falda", "Overol", "Vestido","Traje de baño","Camiseta","Disfraz"]
    return lista
def listaCalzado():
    lista = ["botas", "tenis", "zapatilla", "sandalias", "mocasines", "náuticos","pantunflas","vaqueros","tacones","ballerinas"]
    return lista
def listaGrupoEtario():
    lista = ["Bebé","Niño","Adolescente","Adulto","Adulto Mayor"]
    return lista
# .........................................................
class grupoEtario():
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
#Revisar Clase persona
class Persona():
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
    lista = []
    grupos = listaGrupoEtario()
    contador=1
    for grupo in grupos:
        g = grupoEtario()
        g.set_nombre(grupo)
        g.set_identificador(contador)
        lista.append(g)
        contador=contador+1
    return lista

def creaObjetoFormaRostro():
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
    contador=1
    for textura in Texturas:
        t = TexturaCabello()
        t.set_nombre(textura)
        t.set_identificador(contador)
        contador=contador+1
        lista.append(t)
    return lista
def creaObjetoColorCabello():
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
    contador=1
    for accesorio in accesorios:
        a = Accesorio()
        a.set_nombre(accesorio)
        a.set_identificador(contador)
        lista.append(a)
        contador=contador+1
    return lista
def creaObjetoRopa():
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
    print("El programa ya cuenta con una cantidad de",len(TotalPersonas)," personas","\n")
    cedulasNuevas= int(input("Digite la cantidad de personas que desea crear automáticamente: "))
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
    print("\n","Se han creado ",len(nuevas)," personas de forma exitosa.")
    print("El programa cuenta con un nuevo total de: ",len(TotalPersonas)," personas.")
    print("\033[1;36m" + "───────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def BuscarPersona(muestra,seleccion):
    try:
        if seleccion == "1":
            personaModificar= muestra[0]
        elif seleccion == "2":
            personaModificar= muestra[1]
        elif seleccion == "3":
            personaModificar= muestra[2]
        elif seleccion == "4":
            personaModificar= muestra[3]
        else:
            personaModificar= muestra[4]
    except ValueError:
        print("El numero de persona digitado no existe")
        MenuModificarPersona()
    return personaModificar

def ModificarListaRopa(persona):
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
    prendaNueva=int(input("Digite el numero de la prenda que desea agregar: "))
    for prenda in Ropa:
        if prendaNueva == prenda.identificador:
            print("\n","Se ha elegido la prenda", prenda.get_nombre(),", ahora la persona tiene las siguientes prendas: ")
            for vestuario in persona.get_vestuario():
                vestuario.set_ropa(prenda)
    for vestuario in persona.get_vestuario():
        for ropa in vestuario.get_ropa():
            print("     ►",ropa.get_nombre())
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def ModificarListaAccesorios(persona):
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

    accesorioNuevo=int(input("Digite el numero correspondiente al accesorio que desea agregar: "))
    for accesorio in accesorios:
        if accesorioNuevo == accesorio.get_identificador():
            print("\n","Se ha elegido el accesorio", accesorio.get_nombre(),", ahora la persona tiene los siguientes accesorios: ")
            for vestuario in persona.get_vestuario():
                vestuario.set_accesorio(accesorio)
    for vestuario in persona.get_vestuario():
        for ACCESORIO in vestuario.get_accesorio():
            print("     ►",ACCESORIO.get_nombre())
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def ModificarCalzado(persona):
    calzados = creaObjetoCalzado()
    for vestuario in persona.get_vestuario():
        print("\n","     ► La persona tiene el calzado:",vestuario.get_calzado().get_nombre(),"\n","\n")
    print("                    ╓──────────────────────────────────────────╖\n"
          "                    ║    OPCIONES DE CALZADO PARA AGREGAR      ║\n"
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
            print("\n","\n","     ► El nuevo calzado de la persona es:", calzado.get_nombre(),"\n","\n")
            vestuario.set_calzado(calzado)
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def CalcularCantidades(lista):
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
    print("                    ╓──────────────────────────────────────────╖\n"
          "                    ║         ACCESORIOS A CONSULTAR           ║\n"
          "                    ╟──────────────────────────────────────────╢\n"
          "                    ║    ► 1) Lentes        ► 6) Collar        ║\n"
          "                    ║    ► 2) Aretes        ► 7) Bufanda       ║\n"
          "                    ║    ► 3) Piercing      ► 8) Reloj         ║\n"
          "                    ║    ► 4) Sombrero      ► 9) Brazalete     ║\n"
          "                    ║    ► 5) Anillo        ► 10) Pulseras     ║\n"
          "                    ╙──────────────────────────────────────────╜")
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
    print("                       ├──────────────────┴───────────────────────────┴──────────────┤")
    i = 0
    while i < len(Pronvincias):
        print("                       |", "{:^17}{:^1}{:^25}{:^5}{:^10}".format(Pronvincias[i],"|", listaFemenino[0][i],"|","{0:.3f}".format(listaFemenino[1][i])+" %    |"))
        i = i + 1
    print("                       |","{:^17}{:^1}{:^25}{:^5}{:^10}".format("Total Femeninas","|", len(femenino), "|", "   100 %    |"))
    print("                       └─────────────────────────────────────────────────────────────┘")
    listaMasculino = CalcularCantidades(masculino)
    print("\033[1;36m" + "     -------------------------------------------------------------------------------------    " + '\033[0;m')
    print("     Género: Masculino ")
    print("                       ┌──────────────────┬───────────────────────────┬──────────────┐")
    print("                       |", "{:^17}{:^1}{:^25}{:^5}{:^10}".format("Provincia","|","Cantidad de personas","|","Porcentaje  |"))
    print("                       ├──────────────────┴───────────────────────────┴──────────────┤")
    x = 0
    while x < len(Pronvincias):
        print("                       |", "{:^17}{:^1}{:^25}{:^5}{:^10}".format(Pronvincias[x],"|", listaMasculino[0][x],"|","{0:.3f}".format(listaMasculino[1][x])+" %    |"))
        x = x + 1
    print("                       |","{:^17}{:^1}{:^25}{:^5}{:^10}".format("Total Masculinos","|", len(masculino), "|", "   100 %    |"))
    print("                       └─────────────────────────────────────────────────────────────┘")
    print("     Total de personas que usan ",accesorioCorrecto,": ",len(accesorioelegido),"\n",)
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def ElegirCaracteristicas():
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
    return listaPersonas

def consultaPersona():
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
            print("                    extura:", persona.get_cabello().get_textura().get_nombre())
            print("                    Densidad:", persona.get_cabello().get_densidad().get_nombre())
            print("\033[1;35m" + "      ──────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    MenuSalida()
    return

def MenuModificarPersona():
    muestra=[]
    cantidad=1
    while cantidad <= 5:
        personas=random.choice(TotalPersonas)
        muestra.append(personas)
        cantidad= cantidad +1
    print("                    ╓──────────────────────────────────╖\n"
          "                    ║       PERSONAS DE MUESTRA        ║\n"
          "                    ╟──────────────────────────────────╢\n"
          "                    ║      ► 1) Persona número 1       ║\n"
          "                    ║      ► 2) Persona número 2       ║\n"
          "                    ║      ► 3) Persona número 3       ║\n"
          "                    ║      ► 4) Persona número 4       ║\n"
          "                    ║      ► 5) Persona número 5       ║\n"
          "                    ╙──────────────────────────────────╜")
    try:
        seleccion=input("Digite el numero correspondiente a la persona que desea modificar: ")
        print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
        persona=BuscarPersona(muestra,seleccion)
    except ValueError:
        print("El número de persona dígitado no existe")
    print("                    ╓─────────────────────────────────────────────────────────────────────╖\n"
          "                    ║                     OPCIONES PARA MODIFICAR                         ║\n"
          "                    ╟─────────────────────────────────────────────────────────────────────╢\n"
          "                    ║  ► 1) Lista de ropa: agregar ropa a lista de ropa.                  ║\n"
          "                    ║  ► 2) Lista de accesorios: agregar accesorio a lista de accesorios. ║\n"
          "                    ║  ► 3) Calzado: cambiar el existente por otra opción                 ║\n"
          "                    ║  ► 4) Cancelar acción y volver a menu principal                     ║\n"
          "                    ╙─────────────────────────────────────────────────────────────────────╜\n")
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

def FuncionesAdmi():
    print("              ╔═══════════════════════════════════════════════════╗\n"
        "              ║                 MENÚ ADMINISTRADOR                ║\n"
        "              ╠═══════════════════════════════════════════════════╣\n"
        "              ║     Ingrese 1 para crear persona automáticamente  ║\n"
        "              ║     Ingrese 2 para modificar a una persona        ║\n"
        "              ║     Ingrese 3 para regresar a menú principal      ║\n"
        "              ╚═══════════════════════════════════════════════════╝")
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
    print("\033[1;37m"+"          ╓────────────────────────────────────────────────────────────────────╖\n"
        "          ║                 Opciones de informes a consultar                   ║\n"
        "          ╟────────────────────────────────────────────────────────────────────╢\n"
        "          ║   ► 1) Cantidad y los porcentajes de las personas que usan un      ║\n"
        "          ║        determinado accesorio según el género y la provincia.       ║\n"
        "          ║                                                                    ║\n"
        "          ║   ► 2) Consultar la información de las personas que cumplan        ║\n"
        "          ║        con una serie de características elegidas por el analista.  ║\n"
        "          ║                                                                    ║\n"
        "          ║   ► 3) Cancelar acción y volver a menú principal.                  ║\n"
        "          ╙────────────────────────────────────────────────────────────────────╜")
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
    print("           ╔═════════════════════════════════════════════════════════════════╗\n"
        "           ║                          MENÚ DE SALIDA                         ║\n"
        "           ╠═════════════════════════════════════════════════════════════════╣\n"
        "           ║    Ingrese 1 para ingresar a las funciones del ADMINISTRADOR    ║\n"
        "           ║    Ingrese 2 para ingresar a las funciones del ANALISTA         ║\n"
        "           ║    Ingrese 3 para volver a MENU PRINCIPAL                       ║\n"
        "           ║    Ingrese 4 para cerrar el programa                            ║\n"
        "           ╚═════════════════════════════════════════════════════════════════╝")
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
    if contra == "Etapa2":
        return True
    else:
        return False

def login():
    print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
    print("                     ╔════════════════════════════════════╗\n"
          "                     ║           MENÚ PRINCIPAL           ║\n"
          "                     ╠════════════════════════════════════╣\n"
          "                     ║    Ingrese 1 para Administrador    ║\n"
          "                     ║    Ingrese 2 para Analista         ║\n"
          "                     ║    Ingrese 3 para salir            ║\n"
          "                     ╚════════════════════════════════════╝")
    try:
        opcion=int(input("Ingrese el número correspondiente a la acción que desea realizar: "))
        if opcion == 1:
            contrasena = input(" ► Por favor, ingrese la contraseña de Administrador: ")
            if contrasenaGlobal(contrasena) == True:
                print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
                FuncionesAdmi()
            else:
                print(" ¡CONTRASEÑA INCORRECTA!")
                login()
        if opcion == 2:
            contrasena = input(" ► Por favor, ingrese la contraseña de Analista: ")
            if contrasenaGlobal(contrasena) == True:
                print("\033[1;36m" + "──────────────────────────────────────────────────────────────────────────────────────────────────" + '\033[0;m')
                FuncionesAnalista()
            else:
                print(" ¡CONTRASEÑA INCORRECTA!")
                login()
        if opcion == 3:
            print("El programa ha finalizado")
    except ValueError:
        print("Por favor ingrese un dígito")
        login()
login()