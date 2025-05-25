from models.usuario import Usuario
from utils.id_generator import generar_id

# from database import save_user_to_db  # ← si estás usando una función externa para guardar

def crear_usuario(nombre, contacto, email, tipo= None, id_metamask=None):
    
    key_id = generar_id(tipo)
        
    nuevo_usuario = Usuario(nombre, contacto, email, id_metamask=id_metamask, tipo=tipo, key_id=key_id)
    # Aquí puedes guardar en la base de datos o retornar el dict para que lo use otra función
    # save_user_to_db(nuevo_usuario.to_dict())

    if usuario.usuario_definido:
        guardar_en_base_de_datos(usuario.to_dict(), tipo)
    return nuevo_usuario

