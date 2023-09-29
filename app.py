# aplicação para aprender matemática:
import streamlit as st
import pyttsx3
from PIL import Image

st.title('Cooperativa de Crédito das Crianças da Interativa')
col5, col6 = st.columns(2)
with col5:
    st.image(Image.open(r"D:\Projetos_Analytics\09.alice\alice.png"), use_column_width = True)
with col6:
    st.header('Olá,')

# Inicialize o mecanismo de síntese de voz fora do Streamlit
engine = pyttsx3.init()
engine.setProperty("rate", 180)  # Velocidade da voz (ajuste conforme necessário)

# Caixa de texto para inserir o texto que o usuário deseja que seja lido em voz alta
texto = st.text_input("Diga o seu nome:")
if st.button("iniciar"):
    if texto:
        # Reproduza o texto em voz alta
        engine.say("Olá, " + texto + ' bem-vindo ao aplicativo da cooperativa de crédito das crianças da interativa. O que você deseja fazer? Aqui você pode fazer um depósito ou uma transferência')
        engine.runAndWait()

with st.expander('FAZER UM DEPÓSITO:'):
    col1, col2 = st.columns(2)
    with col1:
        valor = st.text_input('Valor:')
    with col2:
        conta = st.radio('Conta:', options=['123', '321'])
    if st.button('Depositar'):
        if texto:
            # Reproduza o texto em voz alta
            engine.say('Muito bem, ' + texto + ' você depositou ' + valor + ' reais na conta ' + conta)
            engine.runAndWait()

with st.expander('FAZER UM EMPRÉSTIMO:'):
    col3, col4 = st.columns(2)
    with col3:
        valor2 = st.text_input('Valor do empréstimo:')
    with col4:
        conta2 = st.radio('Conta do empréstimo:', options=['123', '321'])
        prazo = st.slider('Quantidade de parcelas:', 1, 10, 5)
        prazo = str(prazo)
    if st.button('Contratar'):
        if texto:
            # Reproduza o texto em voz alta
            engine.say('Muito bem, ' + texto + ' você contratou um empréstimo no valor de ' + valor2 + ' com ' + prazo + ' parcelas e será depositado na conta ' + conta2)
            engine.runAndWait()
st.image(Image.open(r"D:\Projetos_Analytics\09.alice\alice3.jpg"), use_column_width = True)
st.text(    'Feito por Fabio Varriano Alves')