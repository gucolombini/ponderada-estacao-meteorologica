# Ponderada Estação Meteorológica

Sistema real IOT de visualização e armazenamento de dados enviados por meio de comunicação serial.

![arduino](src/static/assets/arduino.png)

## Principais Ferramentas Utilizadas
- Arduino UNO + Sensor DHT11
- Python + Flask + PySerial + SQLite
- HTML + JavaScript + Chart.js

(não tive tempo de fazer front bonito dessa vez... contemple os HTML puros com desenhos do Paint)

## Execução
### 1. Etapa física
Conecte um Arduino UNO com um componente DHT11 da seguinte maneira:
- DHT11 VCC → 5V do Arduino
- DHT11 GND → GND do Arduino
- DHT11 DATA → Pino Analógico 0 do Arduino

Depois, utilizando [ArduinoIDE](https://www.arduino.cc/en/software/), instale a biblioteca [DHT-sensor-library](https://github.com/adafruit/DHT-sensor-library) e envie o código em ***src/arduino/estacao/estacao.ino*** para a placa.

Caso não tenha um componente DHT11 para usar, é possível fazer o envio de dados simulados usando o código em ***src/arduino/estacao_random/estacao_random.ino***.

### 2. Back-end
Na raiz da pasta, crie e ative um venv, e instale as dependências em *requirements.txt*:
```bash
python -m venv venv

/.venv/Scripts/Activate.ps1 # (Windows)
source .venv/Scripts/activate # (Linux)

pip install -r requirements.txt
```

Dentro do ambiente virtual, entre na pasta /src e execute a aplicação Flask.

```bash
cd src
python app.py
```
A aplicação irá iniciar na porta local 5000.

Abra então outro terminal na raiz do projeto e inicie novamente o ambiente virtual.

```bash
/.venv/Scripts/Activate.ps1 # (Windows)
source .venv/Scripts/activate # (Linux)
```

Agora, com o Arduino UNO conectado ao computador, execute o leitor serial.
```bash
cd src
python serial_reader.py
```

### 3. Front-end

Uma vez que o front é entregue pela mesma aplicação Flask, basta acessar *http://localhost:5000/home*.

## Rotas da API

| Método | Rota               | Função         | Descrição                                      |
|--------|--------------------|----------------|------------------------------------------------|
| GET    | /                  | index()        | Painel principal - últimas 10 leituras         |
| GET    | /leituras          | listar()       | Histórico completo com paginação               |
| POST   | /leituras          | criar()        | Recebe JSON do Arduino / simulador             |
| GET    | /leituras/<id>     | detalhe()      | Exibe uma leitura específica                   |
| PUT    | /leituras/<id>     | atualizar()    | Atualiza campos de uma leitura                 |
| DELETE | /leituras/<id>     | deletar()      | Remove uma leitura do banco                    |
| GET    | /api/estatisticas  | estatisticas() | Média, mín e máx do período                    |

## Páginas disponíveis
### 1. Home (/home)
<img width="1919" height="1079" alt="Captura de tela 2026-04-09 052445" src="https://github.com/user-attachments/assets/c512ab00-ee85-4e13-b071-1c7368cef62b" />

Exibe últimas 10 leituras, atualiza em tempo real, e exibe gráfico de variação temporal usando Chart.js.

### 2. Histórico (/historico)
<img width="664" height="844" alt="Captura de tela 2026-04-09 052505" src="https://github.com/user-attachments/assets/0a7f7961-64d7-4146-8633-272c794ae885" />

Exibe todas as leituras até o momento, com opção para deletar ou editar qualquer uma das leituras.

### 3. Editar (/editar)
<img width="810" height="811" alt="Captura de tela 2026-04-09 052512" src="https://github.com/user-attachments/assets/8f6956fe-00a6-49b1-82c6-9ac28233f7ec" />

Tela de edição após selecionar uma das leituras no histórico.
