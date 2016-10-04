class publicacion:
	
	def __init__(self, titulo="", autor="Anonimo", precio=0):
		self._titulo = titulo
		self._autor = autor
		self._precio = precio

	def setTitulo(self,titulo):
		self._titulo = titulo

	def setAutor(self, autor):
		self._autor = autor

	def setPrecio(self, precio):
		self._precio = precio

	
