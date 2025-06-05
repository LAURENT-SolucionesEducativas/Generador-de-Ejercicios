import streamlit as st
import random

# Configurar la página con título e ícono
st.set_page_config(page_title="Generador de Ecuaciones", page_icon="🧮")

# Fondo con estilo CSS
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .stApp {
            background: linear-gradient(to bottom, #e0f7fa, #ffffff);
            padding: 20px;
        }
        .title {
            text-align: center;
            color: #1565C0;
            font-size: 40px;
            font-weight: bold;
        }
        .subtext {
            text-align: center;
            font-size: 18px;
            color: #333333;
        }
        .ejercicio-box {
            background-color: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888888;
            margin-top: 40px;
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
st.markdown("<div class='title'>📘 Generador de Ejercicios de Ecuaciones Lineales</div>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Haz clic para generar <strong>5 ejercicios aleatorios</strong> y ¡pon a prueba tu mente! 🧠</p>", unsafe_allow_html=True)

# Botón
if st.button("🎲 Generar 5 ejercicios"):
    seleccion = random.sample(ejercicios, 5)
    st.markdown("### 📝 Tus ejercicios son:")
    for i, ejercicio in enumerate(seleccion, 1):
        st.markdown(f"<div class='ejercicio-box'><strong>{i}. </strong>{ejercicio}</div>", unsafe_allow_html=True)
    st.success("¡Listo! Resuélvelos en tu cuaderno 📓")
else:
    st.info("Haz clic en el botón para empezar 🎯")

# Pie de página
st.markdown("<div class='footer'>Hecho con ❤️ por tu profe</div>", unsafe_allow_html=True)

