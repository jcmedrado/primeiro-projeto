import streamlit as st 
import webbrowser as wbb
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"]>= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.title(":green[FIFA 23] OFFICIAL DATASET!!") 
st.sidebar.markdown("Desenvolvido por João Medrado")

btn = st.button("Acesse os dados do Keggle")
if btn:
    wbb.open_new_tab("https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset")

st.markdown("""
O FIFA 23 Complete Player Dataset é uma rica fonte de informações que oferece uma visão abrangente do desempenho,
habilidades e características de todos os jogadores presentes no jogo. Com dados detalhados sobre atributos como
velocidade, habilidade de drible, finalização e muito mais, este banco de dados se torna uma ferramenta valiosa
para fãs, analistas e desenvolvedores de jogos. Ele permite a realização de análises profundas sobre o desempenho
dos jogadores, identificando tendências e padrões que podem influenciar táticas e estratégias. 
            
Além disso, facilita a comparação entre jogadores de diferentes clubes e ligas, ajudando tanto os fãs quanto os profissionais a entenderem
melhor as habilidades relativas. Para os desenvolvedores, é útil na criação de experiências de jogo personalizadas
ou modos de jogo baseados em dados reais. O dataset também oferece a possibilidade de criar visualizações impactantes
e relatórios que podem auxiliar na tomada de decisões, seja em ligas de fantasia ou em análises de desempenho. Com
o FIFA 23 Complete Player Dataset, você terá acesso a um mundo de dados que transforma a forma como interage com o
jogo, proporcionando insights valiosos e uma experiência aprimorada para todos os entusiastas do FIFA. **O banco de dados conta com mais de 77.000 joogadores**
"""
)