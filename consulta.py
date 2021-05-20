import streamlit as st
import pandas as pd
import numpy as np

st.title("""Sistema de Gestão de Dados de Pós-Graduação""")
st.subheader("Consulta")

# Leitura dos dados
cursos = pd.read_excel('bd.xlsx')
col = cursos.columns
col = list(col[0:16])+['STATUS']
cursos = cursos.loc[:, col]


# Seleção de campos que podem ser consultados
col = cursos.columns
col = ['CURSO',  'DIRETORIA',  'UNIDADE REGIONAL',  'CARGO DE CONFIANÇA',
        'INSTITUIÇÃO DE ENSINO',  'ANO DE OBTENÇÃO DO TÍTULO',  'DEMANDA', 'STATUS']
opt = st.selectbox('Escolha', col)

# Filtro para consulta
filtros = ['TODOS'] + col

f = st.selectbox('Filtro', filtros)
if f != 'TODOS':
    selecionado = cursos[f].unique()
    sel = st.multiselect('Quais',selecionado)

    indopt = np.array([False]*cursos.shape[0])
    for s in sel:
        cond = cursos.loc[:,f] == s
        indopt = np.logical_or(indopt,cond)

    cursos = cursos.loc[indopt,:]


# Busca por assunto
assunto = st.text_input('Busca assunto', '')
titulos = list(cursos['TÍTULO'])
if len(assunto) > 3:
    assunto = assunto.split()
    ind = []
    for a in assunto:
        for i, t in enumerate(titulos):
            if a.lower() in str(t).lower():
                ind += [i]

    titulos = np.array(titulos)
    titulos = titulos[ind]

    cursos = cursos.iloc[ind, :]


# Resultados
d = cursos[opt].value_counts()
st.bar_chart(d)