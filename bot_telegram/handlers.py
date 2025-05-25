from telebot import types
from bot_telegram.states import user_states
from controllers.usuario_controller import crear_usuario
from utils.id_generator import generar_id


print("handlers.py cargado")


def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("📝 Crear Usuario")
        bot.send_message(message.chat.id, "Bienvenido a Blockfactory Bot.\nElija una opción:", reply_markup=markup)

    @bot.message_handler(func=lambda m: m.text == "📝 Crear Usuario")
    def ask_nombre(message):
        bot.send_message(message.chat.id, "Ingrese su nombre o alias:")
        user_states[message.chat.id] = {"estado": "esperando_nombre"}

    @bot.message_handler(func=lambda m: m.chat.id in user_states)
    def proceso_creacion_usuario(message):
        estado = user_states[message.chat.id]

        if estado["estado"] == "esperando_nombre":
            estado["nombre"] = message.text
            estado["estado"] = "esperando_contacto"
            bot.send_message(message.chat.id, "Ingrese su número de contacto:")

        elif estado["estado"] == "esperando_contacto":
            estado["contacto"] = message.text
            estado["estado"] = "esperando_email"
            bot.send_message(message.chat.id, "Ingrese su correo electrónico:")

        elif estado["estado"] == "esperando_email":
            estado["email"] = message.text
            estado["estado"] = "esperando_tipo"

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup.add("👤 Emprendedor", "🛠️ Servidor")
            bot.send_message(message.chat.id, "Seleccione su perfil:", reply_markup=markup)

        elif estado["estado"] == "esperando_tipo":
            tipo = message.text.lower()
            if "emprendedor" in tipo:
                tipo_db = "emprendedor_id"
            elif "servidor" in tipo:
                tipo_db = "servidor_id"
            else:
                bot.send_message(message.chat.id, "Por favor seleccione una opción válida.")
                return

            estado["tipo"] = tipo_db
            estado["id_asignado"] = generar_id(tipo_db)
            estado["estado"] = "esperando_metamask"

            bot.send_message(message.chat.id, "Ingrese su ID de Metamask para completar el registro (o escriba 'omitir' para hacerlo más tarde):")

        elif estado["estado"] == "esperando_metamask":
            id_meta = message.text.strip()
            if id_meta.lower() == "omitir":
                id_meta = None

            estado["id_metamask"] = id_meta
            usuario_definido = id_meta is not None

            nuevo_usuario = crear_usuario(
                nombre=estado["nombre"],
                contacto=estado["contacto"],
                email=estado["email"],
                tipo="emprendedor" if "emprendedor" in estado["tipo"] else "servidor",
                id_metamask=id_meta
            )
            nuevo_usuario.tipo = estado["tipo"]
            nuevo_usuario.key_id = estado["id_asignado"]

            if usuario_definido:
                bot.send_message(message.chat.id, f"✅ Usuario guardado con ID: {nuevo_usuario.key_id}")
                # Aquí deberías guardar el usuario en la base
            else:
                bot.send_message(message.chat.id, f"📝 Usuario registrado parcialmente. Puedes completarlo luego con /registrar_wallet")

            user_states.pop(message.chat.id)


"""
            nuevo_usuario = crear_usuario(
                nombre=estado["nombre"],
                contacto=estado["contacto"],
                email=estado["email"]
            )

            # Aquí podrías guardar el usuario en la base de datos real
            bot.send_message(message.chat.id, f"✅ Usuario creado:\n{nuevo_usuario.to_dict()}")
            user_states.pop(message.chat.id)
"""