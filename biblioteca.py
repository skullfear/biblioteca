class Biblioteca:
    def __init__(self, archivo):
        self.archivo = archivo
        self.libros = []

    def cargar_libros(self):
        try:
            with open(self.archivo, 'r') as archivo_txt:
                for linea in archivo_txt:
                    partes = linea.strip().split(', ')
                    if len(partes) == 3:
                        titulo, autor, ano = partes
                        self.libros.append({'Título': titulo, 'Autor': autor, 'Año de Publicación': ano})
        except FileNotFoundError:
            print(f'El archivo "{self.archivo}" no se encontró.')

    def mostrar_libros(self):
        if self.libros:
            for i, libro in enumerate(self.libros, start=1):
                print(f'Libro {i}:')
                for campo, valor in libro.items():
                    print(f'{campo}: {valor}')
                print('-' * 20)
        else:
            print('No se han cargado libros.')

    def solicitar_libro(self, numero_libro):
        if 1 <= numero_libro <= len(self.libros):
            libro_solicitado = self.libros[numero_libro - 1]
            print(f'Has solicitado el libro número {numero_libro}:')
            for campo, valor in libro_solicitado.items():
                print(f'{campo}: {valor}')
        else:
            print('Número de libro no válido. Por favor, elige un número de libro válido.')

if __name__ == "__main__":
    biblioteca = Biblioteca("libros.txt")
    biblioteca.cargar_libros()
    biblioteca.mostrar_libros()

    try:
        numero_solicitud = int(input('Ingrese el número del libro que desea solicitar: '))
        biblioteca.solicitar_libro(numero_solicitud)
    except ValueError:
        print('Entrada no válida. Debes ingresar un número válido.')
