import streamlit as st
st.title("Você quer alugar um carro?")
st.sidebar.title("Escolha o seu moedlo")
st.sidebar.image('logo.png')

carros = ["bmw", "fusca","mustang"]

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')


