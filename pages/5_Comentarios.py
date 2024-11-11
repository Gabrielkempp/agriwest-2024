import pandas as pd
from pathlib import Path
import streamlit as st
import plotly_express as px
import Informações_Gerais as IG

# Definições iniciais da pagina
st.set_page_config('Observações', '🪙', 'wide')

# Carregando arquivo
cur_dir = Path(__file__).parent.parent
data = pd.ExcelFile(cur_dir / 'dados.xlsx')

# Chamando a função para garantir que os dados estejam carregados
IG.carregar_dados_se_nao_existem()

# Carregando os dados para a sessão
df_custo_22_23 = st.session_state['df_custo_22_23']
df_custo_23_24 = st.session_state['df_custo_23_24']
df_custo_24_25 = st.session_state['df_custo_24_25']

# Header
st.markdown('# Observações e Feedbacks 💭🌱')
st.markdown('')

st.markdown('### Em breve...')