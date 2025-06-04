import streamlit as st
import random

# Configuración de la página
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

# Título con estilo
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📘 Generador de Ejercicios de Ecuaciones Lineales</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Haz clic para generar <strong>5 ejercicios aleatorios</strong> y ¡pon a prueba tu mente! 🧠</p>", unsafe_allow_html=True)

# Botón
if st.button("🎲 Generar 5 ejercicios"):
    seleccion = random.sample(ejercicios, 5)
    st.markdown("### 📝 Tus ejercicios son:")
    for i, ejercicio in enumerate(seleccion, 1):
        st.write(f"**{i}.** {ejercicio}")
    st.success("¡Listo! Resuélvelos en tu cuaderno 📓")
else:
    st.info("Haz clic en el botón para empezar 🎯")

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Hecho con ❤️ por tu profe/p>", unsafe_allow_html=True)

