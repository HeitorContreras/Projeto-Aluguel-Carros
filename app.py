import streamlit as st
from datetime import datetime

st.sidebar.title("Locadora de veículos")
st.sidebar.image("logo.png")
carro=st.sidebar.selectbox("Selecione o carro que deseja alugar:",
                     ["Duster","Civic","Corolla", "Creta","Amarok","G63"])
valores_diarias = {"Duster":250, "Civic": 300, "Creta": 300, "Amarok": 300, "G63": 800, "Corolla": 250}

st.image(f"{carro}.png")
st.subheader(f"Valor da diária: R$ {valores_diarias[carro]}")
data_retirada = st.date_input("Selecione a data de retirada: ", datetime.now())
data_devolucao = st.input("Selecione a data de entrega:", datetime.now())
