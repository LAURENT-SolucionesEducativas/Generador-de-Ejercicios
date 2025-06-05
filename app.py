import streamlit as st
import random

# Configurar la página
st.set_page_config(page_title="Generador de Ecuaciones", page_icon="🧮")

# Lista de ejercicios
ejercicios = [
    "Resuelve 2x + 3 = 7",
    "Resuelve x/2 = 4",
    "Resuelve 3x - 5 = 10",
    "Resuelve 5x + 1 = 16",
    "Resuelve 4x = 20",
    "Resuelve x - 7 = 2",
    "Resuelve 6x + 2 = 20",
    "Resuelve x/3 + 2 = 5",
    "Resuelve 2(x - 1) = 6",
    "Resuelve 7x - 4 = 24"
]

# Fondo más claro y tipografía personalizada
st.markdown("""
    <style>
        .titulo {
            text-align: center;
            color: #2c3e50;
            font-size: 38px;
            font-weight: bold;
        }
        .subtexto {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 30px;
        }
        .ejercicio-box {
            background-color: #ffffff;
            border-left: 5px solid #3498db;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 8px;
            font-size: 18px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #999;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Imagen motivadora
st.image("https://i.imgur.com/Nu9dhdK.png", width=150, use_column_width=False)

# Título y subtítulo
st.markdown("<div class='titulo'>📘 Generador de Ejercicios de Ecuaciones Lineales</div>", unsafe_allow_html=True)
st.markdown("<div class='subtexto'>Haz clic para generar <strong>5 ejercicios aleatorios</strong> y ¡pon a prueba tu mente! 🧠</div>", unsafe_allow_html=True)

# Botón
if st.button("🎲 Generar 5 ejercicios"):
    seleccion = random.sample(ejercicios, 5)
    st.markdown("### 📝 Tus ejercicios son:")
    for i, ejercicio in enumerate(seleccion, 1):
        st.markdown(f"<div class='ejercicio-box'><strong>{i}.</strong> {ejercicio}</div>", unsafe_allow_html=True)
    st.success("¡Listo! Resuélvelos en tu cuaderno 📓")
else:
    st.info("Haz clic en el botón para empezar 🎯")

# Pie de página
st.markdown("<div class='footer'>Hecho con ❤️ por tu profe</div>", unsafe_allow_html=True)
