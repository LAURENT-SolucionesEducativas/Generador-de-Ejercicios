import streamlit as st
import random

# Configurar la página
st.set_page_config(page_title="Generador de Ecuaciones", page_icon="🧮")

# Estilos CSS para fondo y elementos visuales
st.markdown("""
    <style>
        /* Fondo general en azul degradado */
        .stApp {
            background: linear-gradient(135deg, #d0e9ff, #ffffff);
            padding: 2rem;
        }

        /* Título principal */
        .title {
            text-align: center;
            color: #0d47a1;
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Subtítulo */
        .subtext {
            text-align: center;
            font-size: 18px;
            color: #333333;
            margin-bottom: 30px;
        }

        /* Caja de ejercicios */
        .ejercicio-box {
            background-color: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            font-size: 16px;
        }

        /* Pie de página */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888888;
            margin-top: 40px;
        }

        /* Botón personalizado */
        div.stButton > button {
            background-color: #1e88e5;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 8px;
            border: none;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #1565c0;
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

# Título y subtítulo
st.markdown("<div class='title'>📘 Ejercicios de Ecuaciones Lineales</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Haz clic para generar <strong>5 ejercicios aleatorios</strong> y ¡pon a prueba tu mente! 🧠</div>", unsafe_allow_html=True)

# Botón centrado con columnas
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎲 Generar 5 ejercicios"):
        seleccion = random.sample(ejercicios, 5)
        st.markdown("### 📝 Tus ejercicios son:")
        for i, ejercicio in enumerate(seleccion, 1):
            st.markdown(f"<div class='ejercicio-box'><strong>{i}.</strong> {ejercicio}</div>", unsafe_allow_html=True)
        st.success("¡Listo! Resuélvelos en tu cuaderno 📓")
    else:
        st.info("Empieza ya!! 🎯")

# Pie de página
st.markdown("<div class='footer'>Hecho con ❤️ por tu profe | LAURENT - Soluciones Tecnológicas Educativas</div>", unsafe_allow_html=True)
