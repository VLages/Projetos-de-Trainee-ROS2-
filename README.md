# Projetos-de-Trainee-ROS2-

# Sistema de Comunicação Assíncrono (Publicador/Assinante)

Este documento descreve o funcionamento de um sistema de comunicação simples baseado no padrão **Publicador-Assinante** (Publisher-Subscriber ou Pub/Sub). Neste modelo, os nós de comunicação são desacoplados e não precisam se conhecer diretamente. A comunicação ocorre através de um canal intermediário chamado **tópico**.

## Conceitos Fundamentais

1.  **Publicador (Publisher / "Talker"):**

      * É o nó responsável por **produzir e enviar** informações.
      * Ele não envia a mensagem para um destinatário específico. Em vez disso, ele a "publica" em um tópico nomeado, sem se preocupar se alguém está ouvindo.
      * No nosso exemplo, o "talker" envia continuamente uma mensagem informando o tempo decorrido desde o início do programa.

2.  **Assinante (Subscriber / "Listener"):**

      * É o nó responsável por **receber e processar** informações.
      * Ele se "inscreve" em um ou mais tópicos de seu interesse para ser notificado sempre que uma nova mensagem for publicada nesses canais.
      * No nosso exemplo, o "listener" escuta o tópico e, ao receber uma mensagem, a exibe no console.

3.  **Tópico (Topic):**

      * É o **canal nomeado** que atua como um intermediário. Ele recebe as mensagens do publicador e as distribui para todos os assinantes que estão inscritos nele.
      * Funciona como um quadro de avisos: o publicador afixa uma nota (mensagem) e todos os interessados (assinantes) podem lê-la.

4.  **Comunicação Assíncrona:**

      * A principal característica deste modelo é que o publicador e o assinante operam de forma independente do tempo. O publicador envia a mensagem e continua seu trabalho sem esperar por uma confirmação ou resposta (conhecido como "fire-and-forget"). Da mesma forma, o assinante processa as mensagens à medida que chegam, sem bloquear o publicador.

## Fluxo de Funcionamento

O fluxo de comunicação no sistema de exemplo ocorre da seguinte maneira:

1.  **Inicialização:**

      * O nó **Assinante ("listener")** é iniciado. Ele declara seu interesse em um tópico específico e fica aguardando por dados.
      * O nó **Publicador ("talker")** é iniciado.

2.  **Publicação Contínua:**

      * Dentro de um loop contínuo (por exemplo, a cada segundo), o "talker" cria uma mensagem.
      * A mensagem é formatada com o tempo decorrido, como no exemplo:
        ```
        "Desde o início do programa se passaram: 15 segundos"
        ```
      * O "talker" envia (publica) essa string de texto para o tópico.

3.  **Distribuição e Recebimento:**

      * O mecanismo do tópico recebe a mensagem do "talker" e a retransmite imediatamente para todos os nós que estão inscritos nele.
      * O "listener", que estava aguardando, é notificado e recebe a mensagem.

4.  **Processamento:**

      * Ao receber os dados, o "listener" executa uma ação pré-definida (uma função de *callback*).
      * Neste caso, a ação é formatar e imprimir a mensagem recebida no console:
        ```
        "Mensagem enviada: Desde o início do programa se passaram: 15 segundos"
        ```

Este ciclo se repete continuamente enquanto os dois nós estiverem em execução, garantindo um fluxo de dados constante e desacoplado entre eles.