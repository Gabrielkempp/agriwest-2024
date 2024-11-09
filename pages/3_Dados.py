import pandas as pd
from pathlib import Path
import streamlit as st
import plotly_express as px
import Informações_Gerais as IG

# Definições iniciais da pagina
st.set_page_config('Visualização dos dados', '📈', 'wide')

# Carregando arquivo
cur_dir = Path(__file__).parent.parent
data = pd.ExcelFile(cur_dir / 'dados.xlsx')

# Chamando a função para garantir que os dados estejam carregados
IG.carregar_dados_se_nao_existem()

# Carregando os dados para a sessão
df_custo_22_23 = st.session_state['df_custo_22_23']
df_custo_23_24 = st.session_state['df_custo_23_24']
df_custo_24_25 = st.session_state['df_custo_24_25']
df_lucro = st.session_state['df_lucro']


# Header
st.markdown('# Propriedade Agriwest')
st.markdown('## Visualização dos dados 📈🌱')
st.markdown('')
st.divider()

# Dados do periodo 2022-2023
st.markdown('### Dados do periodo 2022-2023')
st.dataframe(df_custo_22_23, width=800, hide_index=True)
st.divider()

# Dados do periodo 2023-2024
st.markdown('### Dados do periodo 2023-2024')
st.dataframe(df_custo_23_24, width=800, hide_index=True)
st.divider()

# Dados do periodo 2024-2025
st.markdown('### Dados do periodo 2024-2025')
st.dataframe(df_custo_24_25, width=800, hide_index=True)
st.divider()    

# Dados de todo o periodo
st.markdown('### Dados de todo o periodo')
st.dataframe(df_lucro, width=800, hide_index=True)
st.divider()    