# ZAPET - Site Institucional de Clínica Veterinária

Este repositório contém o código-fonte do site institucional da ZAPET, uma clínica veterinária e pet shop. O projeto foi desenvolvido para criar uma presença online para a empresa, apresentando seus serviços e facilitando o contato e agendamento por parte dos clientes.

## 🚀 Sobre o Projeto

ZAPET é uma landing page desenvolvida em HTML, CSS e JavaScript. O objetivo é ser uma vitrine digital para a clínica, oferecendo informações claras sobre os serviços disponíveis, o espaço físico e a qualidade do atendimento, além de capturar o interesse de novos clientes através de um formulário de agendamento prático.

## ✨ Funcionalidades Atuais

* **Navegação Principal:** Um menu de navegação fixo no topo com links para as seções da página e para a página de contato.
* **Banner de Apresentação:** Seção principal que introduz a clínica ZAPET e seus serviços.
* **Carrossel de Imagens:** Um carrossel interativo que exibe fotos dos serviços e da estrutura da clínica, como consultas, hotel, farmácia e recepção.
* **Formulário de Agendamento (Pop-up):** Um formulário que permite ao usuário agendar serviços como consulta, banho/tosa, hotel, entre outros. O formulário aparece ao clicar no botão "AGENDE JÁ!".
* **Seção de Depoimentos:** Exibe comentários de clientes satisfeitos para gerar credibilidade.
* **Página de Contato:** Uma página separada com um formulário para envio de mensagens diretas para a clínica.
* **Design Responsivo:** O layout foi pensado para se adaptar a diferentes dispositivos, embora melhorias possam ser implementadas.

## 🗺️ Roadmap de Desenvolvimento

Este é um roadmap sugerido para as próximas etapas do projeto, visando adicionar novas funcionalidades, melhorar a experiência do usuário e a qualidade do código.

### Fase 1: Melhorias na Interface e Experiência do Usuário (UI/UX)

-   [ ] **Refinar a Responsividade:** Realizar testes em mais dispositivos (tablets, celulares de diferentes tamanhos) e ajustar o CSS para garantir uma experiência consistente em todas as plataformas.
-   [ ] **Animações e Transições:** Adicionar micro-interações (hover effects nos botões, transições suaves ao rolar a página) para tornar a navegação mais fluida e agradável.
-   [ ] **Acessibilidade (a11y):** Implementar melhorias de acessibilidade, como atributos `alt` mais descritivos para as imagens, uso de tags semânticas e garantir o contraste de cores adequado.
-   [ ] **Validação de Formulário em Tempo Real:** Adicionar validação nos campos do formulário (ex: verificar se o CPF é válido, se o telefone está no formato correto) antes do envio, fornecendo feedback instantâneo ao usuário.

### Fase 2: Funcionalidades Adicionais

-   [ ] **Página de Serviços Detalhada:** Criar uma página dedicada para cada serviço (Banho e Tosa, Hotelzinho, etc.) com mais informações, fotos e preços.
-   [ ] **Integração com Calendário:** Conectar o formulário de agendamento a uma ferramenta de calendário (como Google Calendar) para verificar a disponibilidade de horários em tempo real.
-   [ ] **Blog ou Seção de Dicas:** Criar uma área no site para postar artigos e dicas sobre cuidados com animais, o que pode ajudar a atrair e engajar o público.
-   [ ] **Galeria de Fotos:** Uma página com uma galeria de fotos dos "clientinhos", com a devida autorização dos tutores.

### Fase 3: Melhorias Técnicas e de Manutenção

-   [ ] **Refatoração do Código:**
    -   **JavaScript:** Modularizar o código do `main.js`, separando as responsabilidades (lógica do carrossel, lógica do formulário) em diferentes arquivos ou funções.
    -   **CSS:** Organizar o CSS utilizando uma metodologia como BEM (Block, Element, Modifier) ou dividir os estilos em componentes (header, footer, cards) para facilitar a manutenção.
-   [ ] **Otimização de Performance:**
    -   **Otimizar Imagens:** Comprimir as imagens (`.jpg`, `.png`) para reduzir o tempo de carregamento da página.
    -   **Minificação de Arquivos:** Minificar os arquivos CSS e JavaScript para produção.
-   [ ] **Backend para Formulários:** Desenvolver um backend simples (usando Node.js, por exemplo) ou integrar com um serviço de terceiros (como Netlify Forms ou Formspree) para receber e gerenciar os envios dos formulários de contato e agendamento de forma segura.