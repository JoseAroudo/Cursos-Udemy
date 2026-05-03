from pathlib import Path
import os

#base = Path(r"C:\Users\jajap\OneDrive\Desktop\Programacion\CursoUdemy\pythonProject\Dia 6\Recetas")


leer_archivo= lambda archivo: print(open(archivo).read())


Ver_categorias = lambda: os.listdir(Path(__file__).resolve().parent / "Recetas")

Elegir_carpeta = lambda carpeta: Path(Path(__file__).resolve().parent, carpeta)

def Ver_recetas(ruta):
    # Buscar archivos .txt recursivamente en todos los subdirectorios dentro de la carpeta
    archivos_txt = list(ruta.rglob("*.txt"))
    num = 0
    archivos_txt = [archivo.name for archivo in ruta.rglob("*.txt")]
    for archivo in archivos_txt: # Imprimir los archivos encontrados
        num += 1  # Cuenta las recetas
        print(archivo)  # Muestra las recetas
    return num


def MenuPrincipal():
    base= Path(__file__).resolve().parent
    print('''############ MENU PRINCIPAL ############ 
    
[1] leer receta
[2] crear receta
[3] crear categoria
[4] eliminar receta
[5] eliminar receta
[6] finalizar programa''')
    match input("Elige una opción: "):
        case "1":
            opcion1(base)
        case "2":
            print("Opción 2 seleccionada")
        case "3":
            print("Opción 3 seleccionada")
        case "4":
            print("Opción 4 seleccionada")
        case "5":
            print("Opción 5 seleccionada")
        case "6":
            print("Programa finalizado")
            return 0
        case _:
            print("Opción no válida, por favor elige una opción del 1 al 6")

#TODO    Mostrar Recetas
#TODO    Elegir receta
#TODO    Leer receta
    


def opcion1(base):
    print("\nPor favor, elige una categoría entre las siguientes opciones:\n")
    print(Ver_categorias())
    categoria=input().strip()

    ruta= Path(base,"Recetas", categoria)

    archivos_txt = [archivo.name for archivo in ruta.rglob("*.txt")]
    print(f"\nLas recetas disponibles en esta categoría son:\n {archivos_txt}\n\n")
    
    Ver_recetas(Path(base,"Recetas", categoria))
    receta=input("\n\nElije una receta: ")
    ruta_receta= Path(base,"Recetas", categoria, receta+".txt")
    leer_archivo(ruta_receta)


MenuPrincipal()
#base= os.getcwd() 
#opcion1(Path(__file__).resolve().parent)
