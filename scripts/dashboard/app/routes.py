import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
	# Lendo o arquivo CSV com os dados
	data = pd.read_csv('Video Game.csv')

	# Convertendo a coluna de data de string para datetime
	data['Carimbo de data/hora'] = pd.to_datetime(data['Carimbo de data/hora'])

	# Gráfico de pizza para os videogames mais usados
	videogames = data['Qual(is) desses videogames você já usou'].str.get_dummies(sep=', ')
	videogames_counts = videogames.sum().sort_values(ascending=False).head(5)
	plt.figure(figsize=(4,4))
	plt.pie(videogames_counts, labels=videogames_counts.index, autopct='%1.1f%%')
	plt.title('Videogames mais usados')
	plt.savefig('static/figures/grafico1.png', bbox_inches='tight')
	plt.close()

	# Gráfico de pizza para o gênero favorito
	generos = data['Qual é o seu gênero favorito de jogos de vídeo game? '].value_counts().head(5)
	plt.figure(figsize=(4,4))
	plt.pie(generos, labels=generos.index, autopct='%1.1f%%')
	plt.title('Gêneros favoritos')
	plt.savefig('static/figures/grafico2.png', bbox_inches='tight')
	plt.close()

	# Gráfico de barras para a frequência de jogos
	frequencia = data['Com que frequência você joga vídeo game?'].value_counts()
	plt.figure(figsize=(4,2))
	plt.bar(frequencia.index, frequencia.values)
	plt.title('Frequência de jogos')
	plt.xlabel('Frequência')
	plt.ylabel('Número de respostas')
	plt.savefig('static/figures/grafico3.png', bbox_inches='tight')
	plt.close()

	# Gráfico de linha para idade dos jogadores
	idades = pd.to_datetime(data['Qual é sua data de nascimento?']).apply(lambda x: (pd.datetime.now().year - x.year))
	idades_counts = idades.value_counts().sort_index()
	plt.plot(idades_counts.index, idades_counts.values)
	plt.title('Idade dos jogadores')
	plt.xlabel('Idade')
	plt.ylabel('Número de respostas')
	plt.savefig('static/figures/grafico4.png', bbox_inches='tight')
	plt.close()

	# Gráfico de barras para jogos favoritos
	jogos_favoritos = data['Qual é o seu jogo de vídeo game favorito? '].value_counts().head(5)
	plt.figure(figsize=(8,4))
	plt.bar(jogos_favoritos.index, jogos_favoritos.values)
	plt.title('Jogos favoritos')
	plt.xlabel('Jogo')
	plt.ylabel('Número de respostas')
	plt.xticks(rotation=45, ha='right')
	plt.savefig('static/figures/grafico5.png', bbox_inches='tight')
	plt.close()
	
	jogos_favoritos_freq = data.loc[data['Qual é o seu jogo de vídeo game favorito? '].isin(jogos_favoritos.index)]
	jogos_favoritos_freq_counts = jogos_favoritos_freq['Com que frequência você joga vídeo game?'].value_counts()
	plt.figure(figsize=(6,6))
	plt.pie(jogos_favoritos_freq_counts, labels=jogos_favoritos_freq_counts.index, autopct='%1.1f%%')
	plt.title('Frequência dos jogos favoritos')
	plt.savefig('static/figures/grafico6.png')
	# renderizar template HTML com os gráficos
	return render_template('dashboard.html')

if __name__ == "__main__":
	app.run(debug=False)
