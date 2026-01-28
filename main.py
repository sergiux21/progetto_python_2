from lib.loader import load_csv
from lib.statistiche import stat_describe
from lib.grafici import plot_istogramma, plot_heatmap

def main():
    path = "dati\heart_cleveland_upload.csv"

    #chiamiamo il metodo che importa un csv
    df = load_csv(path)

    #facciamo l'analisi statistica
    stat_describe(df)

    #facciamo l'istogramma di una colonna
    plot_istogramma(df, 'chol')

    #visualizziamo la matrice di correlazione
    plot_heatmap(df)

if __name__ == '__main__':
    main()
