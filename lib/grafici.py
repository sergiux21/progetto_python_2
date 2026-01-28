import matplotlib.pyplot as plt
import seaborn as sns

#istogramma di una colonna
def plot_istogramma(df, colonna):
    plt.figure(figsize=(8,4))
    sns.histplot(data=df, x=colonna)
    plt.title(f"Frequenze dei valori di {colonna}")
    plt.tight_layout()
    plt.show()

#grafico della matrice di correlazione
def plot_heatmap(df):
    corr = df.corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Matrice di correlazione")
    plt.show()