# Sistemas Distribuidos

## Comunica��o MQTT - Python - Arduino

Esse projeto est� sendo criado usando como sistema operacional o windows. O projeto possui 3 diret�rios: um possuindo o c�digo arduino, um possuindo o servidor MQTT Local (windows) e um com o c�digo Python.

### Arduino

O m�dulo do arduino tem a fun��o de rebecer as mensagens vinda da porta serial. Assim s� fica responsavel em verificar se essa mensagem � para acender o led.

### Python 

Os m�dulos em python servem um para escrever a mesnagem no servidor MQTT e outro para escutar essa mensagem e ent�o enviar a mensagem correta para o arduino.

### MQTT 

� a pasta que possui o servior MQTT rodando local. Para rodar foi criado um arquivo .bat dentro de Python.
  