import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Allenamento Atleti", layout="wide")

st.title("🏋️‍♂️ PROGRAMMA ALLENAMENTO")

file = "DATABASE_APP.xlsx"
df = pd.read_excel(file)

# login atleta
email = st.sidebar.selectbox(
    "Seleziona il tuo account",
    df["EMAIL_ATLETA"].unique()
)

df_atleta = df[df["EMAIL_ATLETA"] == email]

menu = st.sidebar.radio(
    "MENU",
    ["Allenamento di oggi","Le mie schede","I miei progressi"]
)

# -----------------------
# ALLENAMENTO DI OGGI
# -----------------------

if menu == "Allenamento di oggi":

    st.header("🔥 Allenamento")

    ultima_data = df_atleta["DATA"].max()

    scheda = df_atleta[df_atleta["DATA"] == ultima_data]

    giorno = scheda["GIORNO"].iloc[0]

    st.subheader(giorno)

    for i,row in scheda.iterrows():

        st.markdown(f"### {row['ESERCIZIO']}")

        col1,col2,col3 = st.columns(3)

        col1.metric("Serie",row["SERIE"])
        col2.metric("Rip",row["RIPETIZIONI"])
        col3.metric("Carico",f"{row['CARICO']} kg")

        done = st.checkbox("Eseguito", key=i)

        st.divider()

# -----------------------
# SCHEDE
# -----------------------

elif menu == "Le mie schede":

    st.header("📅 Programma")

    giorni = df_atleta["GIORNO"].unique()

    giorno = st.selectbox("Seleziona giorno",giorni)

    scheda = df_atleta[df_atleta["GIORNO"]==giorno]

    st.dataframe(scheda[["ESERCIZIO","SERIE","RIPETIZIONI","CARICO"]])

# -----------------------
# PROGRESSI
# -----------------------

elif menu == "I miei progressi":

    st.header("📈 Progressi")

    esercizi = df_atleta["ESERCIZIO"].unique()

    esercizio = st.selectbox("Esercizio",esercizi)

    dati = df_atleta[df_atleta["ESERCIZIO"]==esercizio]

    fig = px.line(
        dati,
        x="DATA",
        y="CARICO",
        markers=True,
        title=f"Progressione {esercizio}"
    )

    st.plotly_chart(fig)