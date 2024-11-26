import pandas as pd
from pathlib import Path
import streamlit as st
import plotly_express as px
import Informações_Gerais as IG

# Definições iniciais da pagina
st.set_page_config('Análise Financeira', '🪙', 'wide')

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
st.markdown('# Análise Financeira 🪙🌱')
st.markdown('')

# Definindo variaveis
custo_hectare_22_23 = df_custo_22_23['R$/ha '].sum()
custo_hectare_23_24 = df_custo_23_24['R$/ha '].sum()
custo_hectare_24_25 = df_custo_24_25['R$/ha '].sum()

# Função para formatar valores em reais
def formatar_reais(valor): 
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Cabeçalho
# Comparação de dados
porcentagem = ((custo_hectare_24_25 - custo_hectare_23_24) / custo_hectare_23_24) * 100
porcentagem = -porcentagem
if porcentagem >= 0:
    mensuracao = 'Menor'
else:
    mensuracao = 'Maior'

col1, col2, col3, col4 = st.columns(4)

# Custo por hectare
col1.metric(label='Custo por Hectare', value=formatar_reais(custo_hectare_24_25), delta=f'{porcentagem:.2f}% {mensuracao} comparado a última safra')
col2.metric(label='Custo por Hectare na última Safra', value=formatar_reais(custo_hectare_23_24))

# Custo total
col3.metric(label='Previsão de custo total', value=formatar_reais(custo_hectare_24_25 * 100))
col3.write(f'Custo total da última Safra: {formatar_reais(custo_hectare_23_24 *100)}')

# Média de custo
media_custo = ((custo_hectare_22_23 + custo_hectare_23_24) / 2)
col4.metric(label='Média de custo das últimas Safras', value=formatar_reais(media_custo))
col4.write('Média feita com base nas safras 22/23 e 23/24')
st.divider()

# Gráficos divisão de custo
# Header
st.markdown('## Divisão de custos por categoria')
col5, col6, col7 = st.columns(3)

# Gráfico 1
col5.markdown("<h4 style='color: #4CAF50;'>24/25 - Atual</h4>", unsafe_allow_html=True)
fig = px.pie(df_custo_24_25 , names=df_custo_24_25['Categorias'],values=df_custo_24_25['Partc. Custo'])
col5.plotly_chart(fig)

# Gráfico 2
col6.markdown('### 23/24')
fig = px.pie(df_custo_23_24 , names=df_custo_23_24['Categorias'],values=df_custo_23_24['Partc. Custo'])
col6.plotly_chart(fig)

# Gráfico 3
col7.markdown('### 22/23')
fig = px.pie(df_custo_22_23 , names=df_custo_22_23['Categorias'],values=df_custo_22_23['Partc. Custo'])
col7.plotly_chart(fig)

# Criar gráfico de barras
fig = px.bar(
    df_lucro, 
    x='Safra', 
    y=['Lucro Liquido Venda Fisica', 'Lucro Liquido Venda Fisica + B3'],
    labels={'value': 'Lucro (R$)', 'variable': 'Tipo de Lucro'},
    title='',
    barmode='group'
)

# Personalizar a legenda para ficar na parte de baixo
fig.update_layout(
    legend_title_text='Tipos de Lucro',
    legend=dict(
        orientation='v',  # Orientação horizontal
        yanchor='bottom',  # Alinhamento vertical
        y=-0.5,  # Posição vertical (negativo para ficar abaixo do gráfico)
        xanchor='center',  # Alinhamento horizontal
        x=0.5  # Posição horizontal
    )
)

st.markdown('## Comparativo Lucro Líquido (R$)')
# Exibir gráfico no Streamlit
st.plotly_chart(fig)
