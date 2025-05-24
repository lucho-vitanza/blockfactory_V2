class Usuario:
    def __init__(self, nombre: str, contacto: str, email: str, id_metamask: str = None):
        self.nombre = nombre
        self.contacto = contacto
        self.email = email
        self.id_metamask = id_metamask
        self.tipo = tipo  # Se definirá luego como 'emprendedor' o 'servidor'

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "contacto": self.contacto,
            "email": self.email,
            "id_metamask": self.id_metamask,
            "tipo": self.tipo
        }

