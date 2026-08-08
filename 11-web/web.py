#intalar o stremlit
#pip install streamlit

#importar a biblioteca
import streamlit as st

st.write("Olá, Mundo!")
st.write("Bem-vindo ao meu app Streamlit!")
st.write("meu nome é:Máuricio melo Araujo")
st.write("meu email é:malmeloaraujo@gmail.com")
st.write("meus hobies são: fAZER SPORTS, JOGAR VIDEO GAME, LER LIVROS, ESCUTAR MUSICA, ESTUDAR TECNOLOGIA E PROGRAMAR")
st.write("meu objetivo é: me tornar um programador full stack e trabalhar com desenvolvimento web e mobile")
st.write("meu objetivo é: me tornar O REI DOS PEDREIROS E FAZER MASSA EM MENOS DE 1 MINUTO")

if st.button("COLOQUE AQUI SEU NOME"):
    nome = st.text_input("Digite seu nome:") 
    st.write(f"Olá, {nome}!")