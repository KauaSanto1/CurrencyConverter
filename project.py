from flask import Flask, render_template, request  # Importa as classes necessárias do Flask
import requests  # Importa a biblioteca requests para fazer requisições HTTP

app = Flask(__name__)  # Cria uma instância da aplicação Flask

def obter_taxas():
    # Define a URL da API que retorna as taxas de câmbio
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Troque USD pela moeda de origem se necessário
    resposta = requests.get(url)  # Faz uma requisição GET para a URL

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if resposta.status_code == 200:
        return resposta.json()["rates"]  # Retorna as taxas de câmbio em formato JSON
    else:
        print("Erro ao obter taxas de câmbio.")  # Mensagem de erro se a requisição falhar
        return None  # Retorna None se houver erro

@app.route("/", methods=["GET", "POST"])  # Define a rota principal que aceita métodos GET e POST
def index():
    resultado = None  # Inicializa a variável resultado como None
    # Verifica se o método da requisição é POST (ou seja, o formulário foi enviado)
    if request.method == "POST":
        # Obtém os dados do formulário enviados pelo usuário
        valor = float(request.form["valor"])
        moeda_origem = request.form["moeda_origem"].upper()
        moeda_destino = request.form["moeda_destino"].upper()
        
        # Obtém as taxas de câmbio chamando a função obter_taxas
        taxas = obter_taxas()
        # Verifica se as taxas foram obtidas com sucesso
        if taxas and moeda_origem in taxas and moeda_destino in taxas:
            # Converte o valor da moeda de origem para USD
            valor_em_usd = valor / taxas[moeda_origem]
            # Converte o valor em USD para a moeda de destino
            resultado = valor_em_usd * taxas[moeda_destino]
    
    # Renderiza o template index.html e passa o resultado para o template
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)  # Executa a aplicação Flask em modo de depuração
