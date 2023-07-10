import pandas as pd
from binance.client import Client

# Inicialize o cliente da API com suas chaves de API
client = Client("ygLyQROn7y7SdNvMoJepOdhZJV4OJUPeq1hhYe2929CopY2ZqGREhnWnVy1FQMEs", "aACSH2BCvZKNwp7bbQR5vtMOJAGMvJ8SUB2Cdfw5sBF1g8sRjhRevQfu6EYpssKC")

try:
    # Obtenha informações de trades agregados para o par BTCUSDT
    info = client.get_aggregate_trades(symbol='BTCUSDT')

    # Converta os dados em um dataframe do pandas
    df = pd.DataFrame(info)

    # Exiba as informações
    print(df)
except Exception as e:
    # Exiba qualquer erro que ocorrer
    print(e)