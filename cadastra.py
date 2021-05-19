import streamlit as st
import pandas as pd


st.title("""Sistema de Gestão de Dados de Pós-Graduação""")
st.subheader("Cadastra")

# Ler dados
cursos = pd.read_excel('bd.xlsx')
campos = list(cursos.columns)[1:]

valor = dict.fromkeys(campos)
for c in campos:
    valor[c] = st.text_input(c, '')

b = st.button('Salvar')
if b:
    cursos.append(valor, ignore_index = True)
    cursos.to_excel('bd.xlsx')

