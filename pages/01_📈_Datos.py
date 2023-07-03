import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Datos Trabanca')
df = pd.read_csv('RegistroBanco.csv')
#Se muestra una caja de verificación para mostrar los valores del dataframe
if st.checkbox('Mostrar Registros'):
    st.dataframe(df)

#Se utiliza pa mostrar 2 botones, que le llevarán a ver las primeras o las últimas filas del dataframe
if st.checkbox('Mostrar Primeros o últimos registros'):
    if st.button('Mostrar Primeros'):
        st.write(df.head(3))
    if st.button('Mostrar últimos'):
        st.write(df.tail(3))

#Creará 2 circulos de verificación, que permita mostrar las dimensiones del dataframe
dim = st.radio('Dimensión:',('Filas', 'Columnas'), horizontal = True)
if dim == 'Filas':
    st.write('Cantidad de filas: ', df.shape[0])
else:
    st.write('Cantidad de columnas: ', df.shape[1])


depo_lim = st.slider('Máximo valor Depósito', 0, 2000000, 1000000)
fig1 = plt.figure(figsize=(20,7))
sns.scatterplot(x='Deposits', y = 'Balance', data=df[df['Deposits']<depo_lim])
st.pyplot(fig1)

retiro_lim = st.slider('Máximo valor de transacción', 0, 3000000, 1000000)
fig2 = plt.figure(figsize=(20,7))
sns.scatterplot(x='Withdrawls', y = 'Balance', data=df[df['Withdrawls']<retiro_lim] )
st.pyplot(fig2)
