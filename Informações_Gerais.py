import pandas as pd
from pathlib import Path
import streamlit as st
import plotly_express as px
from datetime import datetime
import webbrowser

# Definições iniciais da pagina
st.set_page_config('Informações Gerais', '🌱', 'wide')

# Carregando arquivo
cur_dir = Path(__file__).parent
data = pd.ExcelFile(cur_dir / 'dados.xlsx')
lucro = pd.ExcelFile(cur_dir / 'lucro.xlsx')

# Função para verificar e carregar os dados
def carregar_dados_se_nao_existem():

    # Chaves que você deseja verificar no session_state
    keys = ['df_custo_22_23', 'df_custo_23_24', 'df_custo_24_25', 'df_lucro']

    if any(key not in st.session_state for key in keys):
        df_custo_22_23 = data.parse(sheet_name='2022-23').fillna(0)
        df_custo_23_24 = data.parse(sheet_name='2023-24').fillna(0)
        df_custo_24_25 = data.parse(sheet_name='2024-25').fillna(0)
        df_lucro = lucro.parse(sheet_name='Plan1').fillna(0)

        # Carregando os dados para a sessão
        st.session_state['df_custo_22_23'] = df_custo_22_23
        st.session_state['df_custo_23_24'] = df_custo_23_24
        st.session_state['df_custo_24_25'] = df_custo_24_25
        st.session_state['df_lucro'] = df_lucro

# Chamando a função para garantir que os dados estejam carregados
carregar_dados_se_nao_existem()

# Carregando os dados para a sessão
df_custo_22_23 = st.session_state['df_custo_22_23']
df_custo_23_24 = st.session_state['df_custo_23_24']
df_custo_24_25 = st.session_state['df_custo_24_25']
df_lucro = st.session_state['df_lucro']

# Header
st.markdown('# Informações Gerais 📈🌱')
st.markdown('')
st.divider()

# Dados sobre a propriedade
col1, col2 = st.columns(2)
col1.metric(label='Nome da Propriedade', value= 'Propriedade Agriwest')
col2.metric(label='Localização', value='Oeste Paranaense')
col3, col4 = st.columns(2)
col3.metric(label='Área Total', value= '100 Hectares')
col4.metric(label='Safras monitoradas', value='22/23 | 23/24 |  24/25')
st.divider()

# Dados sobre a safra
st.markdown('### Cultura Principal:    SOJA')
st.markdown('### Data de Início do Projeto:    Setembro de 2024')
st.markdown('### Status Atual da Safra:    Acompanhamento')
st.divider()


# Resumo das Safras Anteriores
st.markdown('### Resumo das Safras Anteriores')

# Função para formatar valores em reais
def formatar_reais(valor): 
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# safra 2022 - 2023 ----------------------------------------------
st.markdown("<h4 style='color: #4CAF50;'>2022 - 2023</h4>", unsafe_allow_html=True)
col8, col9, col10 = st.columns(3)
col8.metric('Produção Total', df_lucro.loc[df_lucro['Safra'] == '2022/2023', 'Produtividade (sacas/hectare)'])

custo_hec = df_lucro.loc[df_lucro['Safra'] == '2022/2023', 'Custo por Hectare (R$)'].values[0]
col9.metric('Custo Total por Hectare', formatar_reais(custo_hec))    

lucro_f = df_lucro.loc[df_lucro['Safra'] == '2022/2023', 'Lucro Liquido Venda Fisica'].values[0]
col10.metric('Lucro Fisico', formatar_reais(lucro_f))    
st.write(' ')
st.write(' ')

# safra 2023 - 2024 ----------------------------------------------
st.markdown("<h4 style='color: #4CAF50;'>2023 - 2024</h4>", unsafe_allow_html=True)
col8, col9, col10 = st.columns(3)
col8.metric('Produção Total', df_lucro.loc[df_lucro['Safra'] == '2023/2024', 'Produtividade (sacas/hectare)'])

custo_hec = df_lucro.loc[df_lucro['Safra'] == '2023/2024', 'Custo por Hectare (R$)'].values[0]
col9.metric('Custo Total por Hectare', formatar_reais(custo_hec))  

lucro_f = df_lucro.loc[df_lucro['Safra'] == '2023/2024', 'Lucro Liquido Venda Fisica + B3'].values[0]
col10.metric('Lucro Fisico + B3', formatar_reais(lucro_f))    
st.write(' ')
st.write(' ')

# safra 2024 - 2025 - Atual ----------------------------------------------
st.markdown("<h4 style='color: #4CAF50;'>2024 - 2025 - Atual</h4>", unsafe_allow_html=True)
col8, col9, col10 = st.columns(3)
col8.metric('Previsão de produção', df_lucro.loc[df_lucro['Safra'] == '2023/2024', 'Produtividade (sacas/hectare)'])
custo_hec = df_lucro.loc[df_lucro['Safra'] == '2024/2025', 'Custo por Hectare (R$)'].values[0]
col9.metric('Previsão de Custo por Hectare', formatar_reais(custo_hec))    
lucro_f = df_lucro.loc[df_lucro['Safra'] == '2024/2025', 'Lucro Liquido Venda Fisica + B3'].values[0]
col10.metric('Previsão de Lucro - Físico + B3', formatar_reais(lucro_f))    
st.divider()

# Número Mensal de Visitas
st.markdown("### Número Mensal de Visitas:  15")

# Histórico de Visitas
st.markdown("#### 📅 **Histórico de Visitas**")

# Ano 2022/2023
st.markdown("""
<div style="
    border: 2px solid #D3D3D3;
    padding: 10px;
    border-radius: 12px;
    background-color: #ffffff00;
    margin-bottom: 10px;">
    <strong>Ano 2022/2023</strong><br>
    Número total: 32
</div>
""", unsafe_allow_html=True)

# Ano 2023/2024
st.markdown("""
<div style="
    border: 2px solid #D3D3D3;
    padding: 10px;
    border-radius: 12px;
    background-color: #ffffff00;
    margin-bottom: 10px;">
    <strong>Ano 2023/2024</strong><br>
    Número total: 38
</div>
""", unsafe_allow_html=True)

# Ano 2024/2025
st.markdown("""
<div style="
    border: 2px solid #D3D3D3;
    padding: 10px;
    border-radius: 12px;
    background-color: #ffffff00;
    margin-bottom: 10px;">
    <strong>Ano 2024/2025</strong><br>
    Quantidade até o momento: 15
</div>
""", unsafe_allow_html=True)




#st.sidebar.write('Informacoes sobre datas de visitas.')
#botao_pdf = st.sidebar.button("Baixar")    
#if botao_pdf:
#    webbrowser.open_new_tab("https://www.google.com")

#st.sidebar.divider()

#st.sidebar.write('Fotos e videos da sua propriedade')
#botao_fotos = st.sidebar.button("Visualizar")    
#if botao_fotos:
#    webbrowser.open_new_tab("https://drive.google.com/drive/folders/1LetX9FOQ1ZSQJUd-tle4jpotKqDxwH_v?usp=sharingm")


# Função para criar links clicáveis em HTML
def abrir_link(url):
    js = f"window.open('{url}')"  # Comando JavaScript para abrir uma nova aba
    st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)

st.sidebar.write('Informações sobre datas de visitas.')
botao_pdf = st.sidebar.button("Baixar")
if botao_pdf:
    abrir_link("https://www.google.com")

st.sidebar.divider()

st.sidebar.write('Fotos e vídeos da sua propriedade')
botao_fotos = st.sidebar.button("Visualizar")
if botao_fotos:
    abrir_link("https://drive.google.com/drive/folders/1LetX9Fgm")
