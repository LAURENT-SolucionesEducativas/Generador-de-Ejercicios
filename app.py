import streamlit as st
import random

# Configurar la página
st.set_page_config(page_title="Generador de Ecuaciones", page_icon="🧮")

# Estilos personalizados con CSS
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom, #2193b0, #6dd5ed); /* azul degradado */
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        .titulo {
            text-align: center;
            color: white;
            font-size: 38px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitulo {
            text-align: center;
            color: #f0f0f0;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .ejercicio-box {
            background-color: #ffffffdd;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            font-size: 18px;
        }
        .footer {
            text-align: center;
            color: white;
            font-size: 14px;
            margin-top: 50px;
        }
        .stButton > button {
            background-color: #ff9800;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

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

# Mostrar título
st.markdown("<div class='titulo'>📘 Generador de Ejercicios de Ecuaciones Lineales</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Haz clic para generar <strong>5 ejercicios aleatorios</strong> y ¡pon a prueba tu mente! 🧠</div>", unsafe_allow_html=True)

# Botón para generar ejercicios
if st.button("🎲 Generar 5 ejercicios"):
    seleccion = random.sample(ejercicios, 5)
    st.markdown("### 📝 Tus ejercicios son:")
    for i, ejercicio in enumerate(seleccion, 1):
        st.markdown(f"<div class='ejercicio-box'><strong>{i}.</strong> {ejercicio}</div>", unsafe_allow_html=True)
    st.success("¡Listo! Resuélvelos en tu cuaderno 📓")
else:
    st.info("Haz clic en el botón para empezar 🎯")

# Pie de página
st.markdown("<div class='footer'>Hecho con ❤️ por tu profe | LAURENT - Soluciones Tecnológicas Educativas</div>", unsafe_allow_html=True)
