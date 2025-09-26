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

-----------


# Sistema de Comunicação Síncrono (Cliente/Servidor via Serviços)

Este documento descreve o funcionamento de um sistema de comunicação baseado no padrão **Cliente-Servidor**. Este modelo utiliza **serviços** para uma comunicação **síncrona**, ou seja, de requisição e resposta.

Diferente do modelo Publicador/Assinante, aqui a comunicação é direta e o cliente que faz um pedido aguarda ativamente por uma resposta do servidor antes de continuar sua execução. É o modelo ideal para tarefas que exigem uma confirmação ou um resultado direto, funcionando de forma análoga a uma chamada de função remota.

## Conceitos Fundamentais

1.  **Servidor (Server):**

      * É o nó que **oferece uma capacidade ou funcionalidade** específica. Ele define um serviço, aguarda por requisições nesse serviço e as processa.
      * Para cada requisição recebida, ele executa uma lógica e **envia uma resposta de volta** para o cliente que a solicitou.
      * No nosso exemplo, o servidor oferece um serviço de soma: ele recebe dois números e retorna o resultado.

2.  **Cliente (Client):**

      * É o nó que **consome a funcionalidade** oferecida pelo servidor.
      * Quando precisa realizar uma tarefa, ele envia uma requisição para o servidor com os dados necessários.
      * O ponto crucial é que, após enviar a requisição, o cliente **pausa sua execução e aguarda** (fica bloqueado) até que a resposta do servidor chegue.

3.  **Serviço (Service):**

      * É a interface de comunicação que conecta o cliente e o servidor. É definido por um nome e uma estrutura de dados clara, contendo:
          * **Requisição (Request):** Os dados que o cliente envia para o servidor (ex: dois inteiros `A` e `B`).
          * **Resposta (Response):** Os dados que o servidor envia de volta para o cliente (ex: um inteiro com a `soma`).

4.  **Comunicação Síncrona:**

      * O cliente envia uma requisição e **bloqueia** sua operação.
      * O servidor recebe, processa a requisição e envia uma resposta.
      * O cliente recebe a resposta, **desbloqueia** sua operação e continua a execução com o resultado em mãos.

## Fluxo de Funcionamento

O fluxo de comunicação no exemplo de um serviço de soma ocorre da seguinte maneira:

1.  **Inicialização:**

      * O nó **Servidor** é iniciado. Ele anuncia que está oferecendo um serviço e fica aguardando por chamadas.

2.  **Requisição do Cliente:**

      * O nó **Cliente**, em algum ponto de sua execução, precisa somar dois números (ex: `A = 5` e `B = 10`).
      * Ele monta uma mensagem de requisição contendo esses dois números.
      * O cliente "chama" o serviço e envia a requisição. **Neste momento, a execução do cliente é pausada.**

3.  **Processamento no Servidor:**

      * O Servidor recebe a requisição com os dados `A = 5` e `B = 10`.
      * Ele pode registrar a chegada dos dados, por exemplo, imprimindo no seu próprio console:
        ```
        "Números encaminhados: (A = 5 B = 10)"
        ```
      * O servidor executa a lógica principal do serviço: `resultado = 5 + 10`.

4.  **Resposta do Servidor:**

      * Com o cálculo finalizado, o Servidor monta uma mensagem de resposta contendo o resultado (`15`).
      * Ele envia essa resposta de volta para o cliente específico que fez a requisição.

5.  **Finalização no Cliente:**

      * O Cliente recebe a resposta (`15`) do servidor. **Sua execução é desbloqueada.**
      * Agora, com o resultado em mãos, ele pode continuar seu trabalho. Por exemplo, formatando e imprimindo a mensagem final:
        ```
        "O resultado da soma 5 + 10 é 15"
        ```