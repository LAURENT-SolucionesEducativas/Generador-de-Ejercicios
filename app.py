import streamlit as st
import random

ejercicios = [
    "Resuelve 2x + 3 = 7",
    "Resuelve x/2 = 4",
    "Resuelve 3x - 5 = 10",
    "Resuelve 5x + 1 = 16",
    "Resuelve 4x = 20",
    "Resuelve x - 7 = 2"
]

st.title("Generador de ejercicios de ecuaciones lineales")

if st.button("Generar 5 ejercicios"):
    seleccion = random.sample(ejercicios, 5)
    for i, ejercicio in enumerate(seleccion, 1):
        st.write(f"{i}. {ejercicio}")
