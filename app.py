import streamlit as st
import pandas as pd 

df_amostra = pd.read_csv('df_amostra.csv')
df_amostra.drop(axis=1, inplace=True, columns=['Unnamed: 0'])

st.set_page_config(page_title="My App",layout='wide')

st.markdown("<h1 style='text-align: center; color: black;'>Régua Ótima de Atração</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Métricas Relacionadas a interações com SMS de Atração</h2>", unsafe_allow_html=True)

#st.dataframe(df_amostra.head(n=5))

idades_analise_df = pd.read_csv('idades_analise_df.csv')
idades_analise_df.index = idades_analise_df['Unnamed: 0']
idades_analise_df.drop(axis=1, inplace=True, columns=['Unnamed: 0'])
idades_analise_df.index.name = 'Idade'




st.sidebar.header('Filtros')

idade_minima = 18
idade_maxima = 100
idade_minima = st.sidebar.number_input('Digite a idade mínima:', min_value=18, max_value=idade_maxima, value=idade_minima)
idade_maxima = st.sidebar.number_input('Digite a idade máxima:', min_value=idade_minima, max_value=100, value=idade_maxima)

#plotagem = (idades_analise_df[(idades_analise_df['Percentual'] >= menor_porcentagem)  &  (idades_analise_df['Ocorrências'] >= menor_qtd_ocorrencias)].sort_values(by='Percentual', ascending=False)['Percentual'])

st.header('Idade')

col1, col2 = st.columns(2)

plotagem = idades_analise_df.sort_values(by='Ocorrências', ascending=True)
plotagem = plotagem[(plotagem.index >= idade_minima) & (plotagem.index <= idade_maxima)]
plotagem = plotagem['Ocorrências']


plotagem2 = idades_analise_df.sort_values(by='Percentual', ascending=False)
plotagem2 = plotagem2[(plotagem2.index >= idade_minima) & (plotagem2.index <= idade_maxima)]
plotagem2 = plotagem2['Percentual']



with col1:
    st.subheader('Ordenação pelo número de ocorrências na amostra:')
    df1 = idades_analise_df.sort_values(by='Ocorrências', ascending=False)
    df1 = df1[(df1.index >= idade_minima) & (df1.index <= idade_maxima)].head(n=15)
    st.dataframe(df1)
    st.bar_chart(data = plotagem)

with col2:
    st.subheader('Ordenação pelo percentual de acordos:')
    df2 = idades_analise_df.sort_values(by='Percentual', ascending=False)
    df2 = df2[(df2.index >= idade_minima) & (df2.index <= idade_maxima)].head(n=15)
    st.dataframe(df2)
    st.bar_chart(data = plotagem2)


st.header('Unidade Federativa')

UFs_analise_df = pd.read_csv('UFs_analise_df.csv')

UFs_analise_df.index = UFs_analise_df['Unnamed: 0']
UFs_analise_df.drop(axis=1, inplace=True, columns=['Unnamed: 0'])
UFs_analise_df.index.name = 'UF'

UFs_selecionados = st.sidebar.multiselect(
    'Selecione as Unidades Federativas:',
    options = list(set(UFs_analise_df.index)),
    default = list(set(UFs_analise_df.index))

)

col3, col4 = st.columns(2)

plotagem3 = UFs_analise_df.sort_values(by='Ocorrências', ascending=True)
plotagem3 = plotagem3[plotagem3.index.isin(UFs_selecionados)]
plotagem3 = plotagem3['Ocorrências']


plotagem4 = UFs_analise_df.sort_values(by='Percentual', ascending=False)
plotagem4 = plotagem4[plotagem4.index.isin(UFs_selecionados)]
plotagem4 = plotagem4['Percentual']

with col3:
    st.subheader('Ordenação pelo número de ocorrências na amostra:')
    df3 = UFs_analise_df.sort_values(by='Ocorrências', ascending=False)
    df3 = df3[df3.index.isin(UFs_selecionados)].head(n=15)
    df3 = df3.head(n=15)
    st.dataframe(df3)
    st.bar_chart(data = plotagem3)

with col4:
    st.subheader('Ordenação pelo percentual de acordos:')
    df4 = UFs_analise_df.sort_values(by='Percentual', ascending=False)
    df4 = df4[df4.index.isin(UFs_selecionados)].head(n=15)
    df4 = df4.head(n=15)
    st.dataframe(df4)
    st.bar_chart(data = plotagem4)

st.header('Sexo')

generos_analise_df = pd.read_csv('generos_analise_df.csv')

generos_analise_df.index = generos_analise_df['Unnamed: 0']
generos_analise_df.drop(axis=1, inplace=True, columns=['Unnamed: 0'])
generos_analise_df.index.name = 'Sexo'


col5, col6 = st.columns(2)

plotagem5 = generos_analise_df.sort_values(by='Ocorrências', ascending=True)
plotagem5 = plotagem5['Ocorrências']


plotagem6 = generos_analise_df.sort_values(by='Percentual', ascending=False)
plotagem6 = plotagem6['Percentual']

with col5:
    st.subheader('Ordenação pelo número de ocorrências na amostra:')
    df5 = generos_analise_df.sort_values(by='Ocorrências', ascending=False)
    df5 = df5.head(n=15)
    st.dataframe(df5)
    
    st.image('grafico_pizza.png')

    #labels = plotagem5.index
    #sizes = plotagem5

    #fig1, ax1 = plt.subplots()
    #ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.pyplot(fig1)

with col6:
    st.subheader('Ordenação pelo percentual de acordos:')
    df6 = generos_analise_df.sort_values(by='Percentual', ascending=False)
    df6 = df6.head(n=15)
    st.dataframe(df6)
    st.bar_chart(data = plotagem6)

st.header('Análise do Par UF & Idade')

UF_idade_analise_df = pd.read_csv('UF_idade_analise_df.csv') 

UF_idade_analise_df.index = UF_idade_analise_df['Unnamed: 0']
UF_idade_analise_df.drop(axis=1, inplace=True, columns=['Unnamed: 0'])
UF_idade_analise_df.index.name = 'UF,Idade'

filtro = [str(UF) + ',' + str(idade) for UF in UFs_selecionados for idade in list(range(idade_minima, idade_maxima + 1))]
filtro = list(set(filtro))
UF_idade_analise_df = UF_idade_analise_df[UF_idade_analise_df.index.isin(filtro)]

col7, col8 = st.columns(2)

plotagem7 = UF_idade_analise_df.sort_values(by='Ocorrências', ascending=True)
plotagem7 = plotagem7['Ocorrências']

plotagem8 = UF_idade_analise_df.sort_values(by='Porcentagem', ascending=True)
plotagem8 = plotagem8['Porcentagem']

with col7:
    st.subheader('Ordenação pelo número de ocorrências na amostra:')
    df7 = UF_idade_analise_df.sort_values(by='Ocorrências', ascending=False)
    df7 = df7.head(n=15)
    st.dataframe(df7)
    st.bar_chart(data = plotagem7)
    

with col8:
    st.subheader('Ordenação pelo percentual de acordos:')
    df8 = UF_idade_analise_df.sort_values(by=['Porcentagem'], ascending=False)[UF_idade_analise_df.sort_values(by=['Porcentagem'] , ascending=False)['Acordos'] >= 50]
    df8 = df8.head(n=15)
    st.dataframe(df8)
    st.bar_chart(data = plotagem8)

st.header('Análise da Dívida')

divida_analise_df = pd.read_csv('divida_analise_df.csv')
divida_analise_df.index = divida_analise_df['Unnamed: 0']
divida_analise_df.drop(axis=1, inplace=True, columns=['Unnamed: 0'])
divida_analise_df.index.name = 'Idade da Dívida'

col9, col10 = st.columns(2)

plotagem9 = divida_analise_df['Ocorrências'].sort_values(ascending=True)

plotagem10 = divida_analise_df['Percentual'].sort_values(ascending=True)


with col9:
    st.subheader('Ordenação pelo número de ocorrências na amostra:')
    df9 = divida_analise_df.sort_values(by='Ocorrências', ascending=False)
    df9 = df9.head(n=7)
    st.dataframe(df9)
    st.bar_chart(data = plotagem9)
    
with col10:
    st.subheader('Ordenação pelo percentual de acordos:')
    df10 = divida_analise_df.sort_values(by='Percentual' , ascending=False)
    df10 = df10.head(n=7)
    st.dataframe(df10)
    st.bar_chart(data = plotagem10)
