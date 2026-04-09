# Ponderada Estação Meteorológica

Sistema real IOT de visualização e armazenamento de dados enviados por meio de comunicação serial.

![arduino](src/static/assets/arduino.png)

## Principais Ferramentas Utilizadas
- Arduino UNO + Sensor DHT11
- Python + Flask + PySerial + SQLite
- HTML + JavaScript

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