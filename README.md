# Sistemas Distribuidos

## Comunicação MQTT - Python - Arduino

Esse projeto está sendo criado usando como sistema operacional o windows. O projeto possui 3 diretórios: um possuindo o código arduino, um possuindo o servidor MQTT Local (windows) e um com o código Python.

### Arduino

O módulo do arduino tem a função de rebecer as mensagens vinda da porta serial. Assim só fica responsavel em verificar se essa mensagem é para acender o led.

### Python 

Os módulos em python servem um para escrever a mesnagem no servidor MQTT e outro para escutar essa mensagem e então enviar a mensagem correta para o arduino.

### MQTT 

É a pasta que possui o servior MQTT rodando local. Para rodar foi criado um arquivo .bat dentro de Python.
  