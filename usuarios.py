import streamlit as st
import pandas as pd
import numpy as np

st.title("""Sistema de Gestão de Dados de Pós-Graduação""")
st.subheader("Cadastra usuários")

# Leitura dos dados
usuarios = pd.read_excel('usuarios.xlsx')
nomes = usuarios['nomes']
senhas = usuarios['senha']

nome = st.text_input('Nome', '')
senha = st.text_input('Senha', '')

usuario = {'nomes': nome, 'senha': senha}