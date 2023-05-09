import matplotlib.pyplot as plt
import numpy as np
from shiny import ui, render, App
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")


dados = pd.read_csv('Space_Corrected.csv')
dados.head()

# Um gráfico de barras pode ser obtido utilizando a função bar() do módulo plot
# A coluna Datum possui informações sobre a data de lançamento
# Para transformar a data de texto para datetime e poder obter o ano, vamos utilizar a função to_datetime
# Assim vamos obter o ano de cada lançamento e salvar em uma nova coluna
dados['Ano'] = [i.year for i in pd.to_datetime(dados['Datum'],format='mixed')]
# Obtenha quantos lançamentos foram realizados por ano e qual ano teve mais lançamentos
por_ano = dados.groupby('Ano').count().sort_values('Ano',ascending=False)
por_ano[['Datum']][0:10].plot.bar()
# Vamos agora obter como gráfico de barras

# fig = plt.figure(figsize=(6,6))
# ax = sns.countplot(y="Status Mission", data=dados, order=dados["Status Mission"].value_counts().index, palette="Set2")
# ax.set_xscale("log")
# ax.axes.set_title("Mission Status vs. Count",fontsize=18)
# ax.set_xlabel("Count",fontsize=16)
# ax.set_ylabel("Mission Status",fontsize=16)
# ax.tick_params(labelsize=12)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(6,6))
# ax = sns.countplot(x="Status Rocket", data=dados, order=dados["Status Rocket"].value_counts().index, palette="pastel")
# ax.axes.set_title("Rocket Status vs. Count",fontsize=18)
# ax.set_xlabel("Count",fontsize=16)
# ax.set_ylabel("Rocket Status",fontsize=16)
# ax.tick_params(labelsize=12)
# plt.tight_layout()
# plt.show()

dados["Country"] = dados["Location"].apply(lambda location: location.split(", ")[-1])
dados.head()


# plt.figure(figsize=(8,8))
# ax = sns.countplot(y="Country", data=dados, order=dados["Country"].value_counts().index)
# ax.set_xscale("log")
# ax.axes.set_title("Country vs. # Launches (Log Scale)",fontsize=18)
# ax.set_xlabel("Number of Launches (Log Scale)",fontsize=16)
# ax.set_ylabel("Country",fontsize=16)
# ax.tick_params(labelsize=12)
# plt.tight_layout()
# plt.show()


app_ui = ui.page_fixed(
    ui.h2("Lançamentos Espaciais"),
    ui.markdown("""
        Vamos analisar os dados dos lançamentos espaciais desde o primeiro lançamento em 1957 até 2020.
    """),
        ui.panel_main(
            ui.output_table("text_data"),
            ui.output_plot("plot")
        )
    )
def server(input, output, session):
    @output
    @render.plot
    def plot():
        fig = plt.figure(figsize=(6,6))
        ax = sns.countplot(y="Status Mission", data=dados, order=dados["Status Mission"].value_counts().index, palette="Set2")
        ax.set_xscale("log")
        ax.axes.set_title("Mission Status vs. Count",fontsize=18)
        ax.set_xlabel("Count",fontsize=16)
        ax.set_ylabel("Mission Status",fontsize=16)
        ax.tick_params(labelsize=12)

        return fig
    @output
    @render.table
    def text_data():
        return dados.head()


app = App(app_ui, server)
