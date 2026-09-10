from pathlib import Path


BASE = Path(__file__).resolve().parent


def leer_archivo(archivo):
    archivo = Path(archivo)
    if not archivo.is_file():
        print("La receta no existe.")
        return
    print(archivo.read_text(encoding="utf-8"))


def Ver_categorias(base=BASE):
    recetas = Path(base) / "Recetas"
    return sorted(categoria.name for categoria in recetas.iterdir() if categoria.is_dir())


def Elegir_carpeta(carpeta, base=BASE):
    return Path(base) / "Recetas" / carpeta


def Ver_recetas(ruta):
    recetas = sorted(Path(ruta).glob("*.txt"))
    for receta in recetas:
        print(receta.stem)
    return len(recetas)


def Mostrar_recetas(categoria, base=BASE):
    ruta = Elegir_carpeta(categoria, base)
    if not ruta.is_dir():
        print("La categoría no existe.")
        return []
    recetas = sorted(ruta.glob("*.txt"))
    if not recetas:
        print("La categoría no contiene recetas.")
    else:
        Ver_recetas(ruta)
    return recetas


def Elegir_receta(categoria, base=BASE):
    recetas = Mostrar_recetas(categoria, base)
    if not recetas:
        return None
    nombre = input("Elige una receta: ").strip()
    receta = Elegir_carpeta(categoria, base) / nombre
    if receta.suffix.lower() != ".txt":
        receta = receta.with_suffix(".txt")
    if receta not in recetas:
        print("La receta no existe.")
        return None
    return receta


def Leer_receta(base=BASE):
    categorias = Ver_categorias(base)
    print("Categorías:", ", ".join(categorias))
    categoria = input("Elige una categoría: ").strip()
    receta = Elegir_receta(categoria, base)
    if receta:
        leer_archivo(receta)


def Crear_receta(base=BASE):
    categorias = Ver_categorias(base)
    print("Categorías:", ", ".join(categorias))
    categoria = input("Categoría: ").strip()
    ruta = Elegir_carpeta(categoria, base)
    if not ruta.is_dir():
        print("La categoría no existe.")
        return
    nombre = input("Nombre de la receta: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    ruta_receta = ruta / nombre
    if ruta_receta.suffix.lower() != ".txt":
        ruta_receta = ruta_receta.with_suffix(".txt")
    if ruta_receta.exists():
        print("La receta ya existe.")
        return
    contenido = input("Escribe la receta: ")
    ruta_receta.write_text(contenido, encoding="utf-8")
    print("Receta creada.")


def Crear_categoria(base=BASE):
    nombre = input("Nombre de la categoría: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    categoria = Path(base) / "Recetas" / nombre
    if categoria.exists():
        print("La categoría ya existe.")
        return
    categoria.mkdir(parents=True)
    print("Categoría creada.")


def Eliminar_receta(base=BASE):
    categorias = Ver_categorias(base)
    print("Categorías:", ", ".join(categorias))
    categoria = input("Categoría: ").strip()
    receta = Elegir_receta(categoria, base)
    if receta and input("¿Eliminar esta receta? (s/n): ").strip().lower() == "s":
        receta.unlink()
        print("Receta eliminada.")


def Eliminar_categoria(base=BASE):
    categorias = Ver_categorias(base)
    print("Categorías:", ", ".join(categorias))
    nombre = input("Categoría: ").strip()
    categoria = Elegir_carpeta(nombre, base)
    if not categoria.is_dir():
        print("La categoría no existe.")
        return
    if any(categoria.iterdir()):
        print("La categoría no está vacía.")
        return
    categoria.rmdir()
    print("Categoría eliminada.")


def MenuPrincipal(base=BASE):
    while True:
        print("""
############ MENU PRINCIPAL ############
[1] Leer receta
[2] Crear receta
[3] Crear categoría
[4] Eliminar receta
[5] Eliminar categoría
[6] Finalizar programa""")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            Leer_receta(base)
        elif opcion == "2":
            Crear_receta(base)
        elif opcion == "3":
            Crear_categoria(base)
        elif opcion == "4":
            Eliminar_receta(base)
        elif opcion == "5":
            Eliminar_categoria(base)
        elif opcion == "6":
            print("Programa finalizado")
            return 0
        else:
            print("Opción no válida, por favor elige una opción del 1 al 6")


if __name__ == "__main__":
    MenuPrincipal()
