class Usuario:
    def __init__(self, nombre: str, contacto: str, email: str, id_metamask: str = None, tipo: str = None, key_id: str = None):
        self.nombre = nombre
        self.contacto = contacto
        self.email = email
        self.id_metamask = id_metamask
        self.tipo = tipo  # Se definirá luego como 'emprendedor' o 'servidor'
        self.key_id = key_id  # ID único para el usuario, se generará al crear el usuario
        self.usuario_definido = bool(id_metamask)


    def to_dict(self):
        return {
            "nombre": self.nombre,
            "contacto": self.contacto,
            "email": self.email,
            "id_metamask": self.id_metamask,
            "tipo": self.tipo,
            "key_id": self.key_id,
            
        }

