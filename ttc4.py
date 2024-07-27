import tensorflow as tf
import numpy as np

class Corrente:
    def __init__(self):
        # Construção do modelo
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(1, input_shape=(1,), activation='linear')])
        
        # Compilação do modelo
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train(self, correnteAtual, correnteDesejada, epochs=2500):
        # Treinamento do modelo
        self.model.fit(correnteAtual, correnteDesejada, epochs=epochs, verbose=0)

    def ajusteCorrente(self, correnteAtual):
        # Predição do volume ajustado
        correnteAjustada = self.model.predict(correnteAtual)
        return correnteAjustada[0][0]

class Corrente2:
    def __init__(self):
        # Construção do modelo
        self.model2 = tf.keras.Sequential([
            tf.keras.layers.Dense(1, input_shape=(1,), activation='linear')])
        
        # Compilação do modelo
        self.model2.compile(optimizer='adam', loss='mean_squared_error')

    def train2(self, correnteAtual2, correnteDesejada2, epochs=2500):
        # Treinamento do modelo
        self.model2.fit(correnteAtual2, correnteDesejada2, epochs=epochs, verbose=0)

    def ajusteCorrente2(self, correnteAtual2):
        # Predição do volume ajustado
        correnteAjustada2 = self.model2.predict(correnteAtual2)
        return correnteAjustada2[0][0]


class Corrente3:
    def __init__(self):
        # Construção do modelo
        self.model3 = tf.keras.Sequential([
            tf.keras.layers.Dense(1, input_shape=(1,), activation='linear')])
        
        # Compilação do modelo
        self.model3.compile(optimizer='adam', loss='mean_squared_error')

    def train3(self, correnteAtual3, correnteDesejada3, epochs=2500):
        # Treinamento do modelo
        self.model3.fit(correnteAtual3, correnteDesejada3, epochs=epochs, verbose=0)

    def ajusteCorrente3(self, correnteAtual3):
        # Predição do volume ajustado
        correnteAjustada3 = self.model3.predict(correnteAtual3)
        return correnteAjustada3[0][0]
    

# Exemplo de uso
if __name__ == "__main__":
    # Dados de exemplo (volume atual e preferência de volume)
    correnteAtual = np.array([[0.2], [0.4], [0.6], [0.8], [0.3], [0.5], [0.7], [0.9]])
    correnteDesejada = np.array([[0.3], [0.5], [0.7], [0.9], [0.7], [0.6], [0.8], [1]])

if __name__ == "__main__":
    # Dados de exemplo (volume atual e preferência de volume)
    correnteAtual2 = np.array([[0.2], [0.4], [0.6], [0.8], [0.3], [0.5], [0.7], [0.9]])
    correnteDesejada2 = np.array([[0.1], [0.2], [0.5], [0.6], [0.2], [0.1], [0.3], [0.4]])
    
if __name__ == "__main__":
    # Dados de exemplo (volume atual e preferência de volume)
    correnteAtual3  = np.array([[0.2], [0.4], [0.6], [0.8], [0.3], [0.5], [0.7], [0.9]])
    correnteDesejada3 = np.array([[0.1], [0.2], [0.5], [0.6], [0.2], [0.1], [0.3], [0.4]])

    # Criando o modelo
    model = Corrente()

    # Treinando o modelo
    model.train(correnteAtual, correnteDesejada)

    # Criando o modelo
    model2 = Corrente2()

    # Treinando o modelo
    model2.train2(correnteAtual2, correnteDesejada2)
    
     # Criando o modelo
    model3 = Corrente3()

    # Treinando o modelo
    model3.train3(correnteAtual3, correnteDesejada3)

    def definirCorrenteAtual():
        corrente = float(input("Digite a corrente atual (entre 0 e 1): "))
        return np.array([[corrente]])

    def definirCorrenteAtual2():
        corrente2 = float(input("Digite a corrente2 atual (entre 0 e 1): "))
        return np.array([[corrente2]])

    def definirCorrenteAtual3():
        corrente3 = float(input("Digite a corrente3 atual (entre 0 e 1): "))
        return np.array([[corrente3]])

    for _ in range(8):
        corrente_Atual = definirCorrenteAtual()
        correnteAjustada = model.ajusteCorrente(corrente_Atual)
        print("corrente ajustada :", correnteAjustada, "A")
        
        corrente_Atual2 = definirCorrenteAtual2()
        correnteAjustada2 = model2.ajusteCorrente2(corrente_Atual2)
        print("corrente ajustada2 :", correnteAjustada2, "A")
        
        corrente_Atual3 = definirCorrenteAtual3()
        correnteAjustada3 = model3.ajusteCorrente3(corrente_Atual3)
        print("corrente ajustada3 :", correnteAjustada3, "A")
        