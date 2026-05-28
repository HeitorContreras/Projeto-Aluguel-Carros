import streamlit as st

st.sidebar.title("Locadora de veículos")
st.sidebar.image("logo.png")
st.sidebar.selectbox("Selecione o carro que deseja alugar:",
                     ["Duster","Civic","Corolla", "Creta","Amarok","G63"])
st.image(f"{carro}.png", width=750)
