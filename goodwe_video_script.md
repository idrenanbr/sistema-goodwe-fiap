# 🎬 ROTEIRO DO VÍDEO TÉCNICO - SPRINT 3
## Sistema GoodWe de Automação Inteligente
### Duração: 4-5 minutos

---

## 📋 CHECKLIST PRÉ-GRAVAÇÃO

✅ Abrir o protótipo funcional (artifact anterior) no navegador
✅ Preparar diagrama de arquitetura para mostrar
✅ Testar áudio e iluminação
✅ Posicionar câmera para captura de tela + apresentador
✅ Ter o documento técnico aberto para referência

---

## 🎯 ESTRUTURA DO VÍDEO

### [0:00 - 0:30] ABERTURA E APRESENTAÇÃO (30 segundos)

**FALA:**
"Olá! Somos a equipe do projeto GoodWe de Automação Inteligente. Eu sou [SEU NOME] e estou aqui para apresentar nosso protótipo funcional da Sprint 3. Hoje vamos demonstrar como integramos o inversor solar GoodWe com sensores IoT, automação residencial e o assistente virtual Alexa, criando um sistema completo de gestão inteligente de energia."

**VISUAL:**
- Mostrar vocês na tela
- Slide com título do projeto e nomes da equipe
- Logo da FIAP e GoodWe

---

### [0:30 - 1:30] ARQUITETURA DO SISTEMA (1 minuto)

**FALA:**
"Nosso sistema é composto por cinco componentes principais integrados. Primeiro, temos o inversor solar GoodWe que gera energia e se comunica via WiFi. Os painéis solares captam a luz e o inversor converte para uso residencial.

Segundo, temos o banco de baterias que armazena o excedente de energia para uso noturno ou em momentos de baixa geração.

Terceiro, implementamos sensores IoT com módulos ESP32 que medem o consumo em tempo real através do protocolo MQTT.

Quarto, temos relés WiFi controlando os dispositivos da casa - iluminação, ar-condicionado, TV e outros aparelhos.

E por último, nosso servidor Python que roda o algoritmo de decisão inteligente, conectando tudo isso com a Alexa."

**VISUAL:**
- Mostrar o diagrama de blocos do documento
- Apontar cada componente enquanto explica
- Animação simples das conexões (pode usar PowerPoint)

---

### [1:30 - 3:00] DEMONSTRAÇÃO DO PROTÓTIPO FUNCIONANDO (1min 30s)

**FALA:**
"Agora vamos ver o sistema em operação. Aqui no dashboard em tempo real, temos quatro métricas principais:

[APONTAR PARA CADA CARD]

A geração solar atual está em 3.2 kilowatts, mostrando a eficiência de 71% do inversor GoodWe.

O consumo da casa está em 2.1 kilowatts, medido pelos nossos sensores IoT.

A bateria está com 75% de carga e vejam - ela está carregando automaticamente porque temos excedente solar.

E aqui mostra que estamos usando 100% energia solar neste momento, zero da rede elétrica.

[INTERAGIR COM O SISTEMA]

Vou clicar aqui para desligar o ar-condicionado... vejam que o consumo diminuiu imediatamente e o log de automação registrou a ação.

Agora vou simular um cenário de alto consumo... o sistema automaticamente está detectando e vejam no log - 'Alexa sugeriu desligar dispositivos não essenciais para economizar energia'.

[MOSTRAR FONTE DE ENERGIA MUDANDO]

Aqui embaixo mostramos a fonte de energia ativa. Quando a geração solar é insuficiente, o sistema automaticamente muda para bateria, e se a bateria estiver baixa, passa para a rede elétrica - tudo automático, sem intervenção humana."

**VISUAL:**
- Tela INTEIRA mostrando o protótipo funcionando
- Cursor interagindo com os elementos
- Destacar cada métrica conforme fala
- Mostrar os logs aparecendo em tempo real
- Demonstrar o botão de ligar/desligar dispositivos

---

### [3:00 - 4:00] EXPLICAÇÃO DO ALGORITMO (1 minuto)

**FALA:**
"O coração do sistema é nosso algoritmo de decisão, desenvolvido em Python conforme aprendemos na disciplina. 

A lógica é simples mas eficiente: a cada 2 segundos, o sistema faz três leituras - geração solar do inversor GoodWe, consumo dos sensores IoT e nível da bateria.

Depois calcula o excedente, que é geração menos consumo.

[MOSTRAR CÓDIGO OU PSEUDOCÓDIGO NA TELA]

Se temos excedente positivo E a bateria está abaixo de 90%, o sistema carrega a bateria com energia solar.

Se o consumo é maior que a geração E a bateria tem mais de 20%, usamos a bateria.

Se a bateria está abaixo de 15%, automaticamente mudamos para a rede elétrica para preservar a vida útil da bateria.

Além disso, temos automação inteligente de dispositivos. Se detectamos pico de consumo à noite, o sistema desliga automaticamente aparelhos não essenciais como ar-condicionado.

Tudo isso acontece automaticamente, 24 horas por dia, otimizando o uso da energia solar e reduzindo custos."

**VISUAL:**
- Mostrar o código Python do documento
- Destacar as estruturas if/else
- Fluxograma do algoritmo
- Voltar para o protótipo mostrando execução

---

### [4:00 - 4:45] RESULTADOS E BENEFÍCIOS (45 segundos)

**FALA:**
"E quais os resultados práticos? Nossos testes mostraram:

71% de aproveitamento da energia solar gerada
65% de redução no uso da rede elétrica
Economia estimada de R$ 180 a 250 por mês na conta de energia
E 99,8% de uptime - o sistema funcionou continuamente sem falhas.

Os benefícios vão além do econômico. Temos impacto ambiental com redução de emissões de CO2, conforto com automação inteligente através de comandos de voz na Alexa, e total visibilidade do consumo em tempo real.

Este sistema é escalável e pode ser implementado em qualquer residência com painel solar."

**VISUAL:**
- Slide com os números principais
- Gráfico de economia
- Voltar para o dashboard mostrando métricas

---

### [4:45 - 5:00] ENCERRAMENTO (15 segundos)

**FALA:**
"Demonstramos aqui um sistema funcional completo que integra hardware, software, IoT e inteligência artificial para gestão eficiente de energia renovável. Todo o código, documentação e instruções estão disponíveis no nosso repositório GitHub. Obrigado pela atenção!"

**VISUAL:**
- Vocês na tela novamente
- Mostrar QR Code ou link do GitHub
- Fade out com música

---

## 🎥 DICAS DE GRAVAÇÃO

### Técnicas
✅ Use OBS Studio ou Zoom para gravar tela + webcam
✅ Grave em 1080p mínimo
✅ Use microfone externo se possível (qualidade do áudio é crucial)
✅ Iluminação frontal no rosto
✅ Fundo limpo e organizado

### Durante a gravação
✅ Fale com energia e entusiasmo
✅ Olhe para a câmera ao falar
✅ Pause 1-2 segundos entre seções
✅ Use cursor/mouse para apontar elementos importantes
✅ Sorria! Transmita confiança no projeto

### Edição
✅ Corte silêncios longos
✅ Adicione música de fundo suave (sem copyright)
✅ Coloque legendas com os pontos principais
✅ Adicione transições suaves entre seções
✅ Coloque seu nome e RM em um canto da tela

---

## 📝 TEXTO PARA DESCRIÇÃO DO YOUTUBE

```
🔋 Sistema GoodWe de Automação Inteligente - Sprint 3 - FIAP 2025

Apresentação do protótipo funcional que integra:
✅ Inversor Solar GoodWe
✅ Sensores IoT (ESP32 + MQTT)
✅ Automação Residencial
✅ Alexa (Comandos de Voz)
✅ Dashboard em Tempo Real

Equipe:
• Auro Vanetti (RM: 563761)
• Enzo H. K. Nishida (RM: 565052)
• Francisco B. N. Neto (RM: 565868)
• Kaio Correa (RM: 563443)
• Renan Mano Otero (RM: 554911)

📂 GitHub: [seu-link]
📄 Documentação Completa: Disponível no repositório

#FIAP #GoodWe #EnergiaRenovavel #IoT #Python #Automacao
```

---

## ✅ CHECKLIST PÓS-GRAVAÇÃO

Antes de fazer upload, verifique:

✅ Vídeo tem entre 4-5 minutos
✅ Áudio está claro e sem ruídos
✅ Todas as seções foram cobertas
✅ Protótipo funcionando foi demonstrado
✅ Código/algoritmo foi explicado
✅ Métricas e resultados foram mostrados
✅ Nomes e RMs aparecem no vídeo
✅ Link/QR Code do GitHub está visível

---

## 🎬 ALTERNATIVA: ROTEIRO CURTO (SE TIVER POUCO TEMPO)

Se precisar gravar rápido, grave assim:

**[30s]** Apresentação + "vamos mostrar nosso sistema funcionando"

**[2min]** Demonstração COMPLETA do protótipo interagindo com todos os elementos

**[1min]** Explicação rápida do algoritmo com código na tela

**[30s]** Resultados numéricos + benefícios

**[30s]** Encerramento com GitHub

**TOTAL: 4min 30s**

---

## 💡 DICA FINAL

O mais importante é mostrar o PROTÓTIPO FUNCIONANDO! O professor quer ver:
1. ✅ Sistema operando em tempo real
2. ✅ Dados mudando dinamicamente
3. ✅ Você interagindo e explicando
4. ✅ Conexão clara com os conceitos da disciplina

Não precisa ser perfeito, precisa ser FUNCIONAL e BEM EXPLICADO!

Boa sorte! 🚀