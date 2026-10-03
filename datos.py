from tkinter import messagebox
import sqlite3
from bs4 import BeautifulSoup
import urllib
import urljoin

def cargar():
	respuesta = messagebox.askyesno(
		title="Confirmar",
		message="¿Está seguro que quiere recargar los datos?\n"
	)
	if respuesta:
		almacenardb()


def almacenardb():
	conn = sqlite3.connect('recetas.db')
	conn.text_factory = str
	conn.execute('DROP TABLE IF EXISTS RECETAS')
	conn.execute('''CREATE TABLE RECETAS
	(titulo TEXT NOT NULL,
	dificultad TEXT NOT NULL CHECK(DIFICULTAD IN ('Muy baja', 'Baja', 'Media', 'Alta')),
	num_comensales INTEGER,
	tiempo_preparacion TEXT,
	autor TEXT,
	fecha TEXT NOT NULL);''')

	lista_recetas = extraer_recetas()
	for receta in lista_recetas:
		url = receta.find("a")["href"]
		f = urllib.request.urlopen(url)
		s = BeautifulSoup(f, "html.parser")
		titulo = s.find("h1", class_="titulo titulo--articulo")
		dificultad = s.find("span", class_="property dificultad")
		num_comensales = s.find("span", class_="property comensales")
		tiempo_preparacion = s.find("span", class_="property duracion")
		autor = s.find("div", class_="nombre autor").find("a").get_text(strip=True)
		fecha = s.find("span", class_="date_publish")

		conn.execute(
			"""INSERT INTO RECETAS
			(titulo, dificultad, num_comensales, tiempo_preparacion, autor, fecha)
			VALUES (?,?,?,?,?,?)""",
			(titulo, dificultad, num_comensales, tiempo_preparacion, autor, fecha),
		)

	conn.commit()

	cursor = conn.execute("SELECT COUNT(*) FROM RECETAS")
	cursor1 = conn.execute("SELECT COUNT(DISTINCT autor) FROM RECETAS;")
	messagebox.showinfo(
		"Base Datos",
		"Base de datos creada correctamente\nHay "
		+ str(cursor.fetchone()[0]) + " recetas y "
		+ str(cursor1.fetchone()[0]) + " autores",
	)
	conn.close()


def extraer_recetas():
	import locale
	locale.setlocale(locale.LC_TIME, 'es_ES')

	url = "https://recetas.elperiodico.com/Recetas-de-Aperitivos-tapas-listado_receta-1_1.html"
	f = urllib.request.urlopen(url)
	s = BeautifulSoup(f, "html.parser")
	listado_recetas = s.find("div", class_="clear padding-left-1")
	listar_recetas = listado_recetas.find_all("div", class_="resultado link")
	return listar_recetas