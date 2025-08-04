# ZAPET - Aplicação Desktop de Clínica Veterinária com Flet

Este repositório contém o código-fonte da aplicação desktop da ZAPET, uma clínica veterinária e pet shop. O projeto, originalmente uma página web, foi migrado para Python com o framework Flet para criar uma experiência de usuário nativa e multiplataforma.

## 🚀 Sobre o Projeto

ZAPET é uma aplicação desktop desenvolvida em Python e Flet. O objetivo é fornecer uma vitrine digital para a clínica, oferecendo informações claras sobre os serviços, e permitir que clientes agendem atendimentos e entrem em contato diretamente pela aplicação. A migração para Flet visa criar uma solução robusta, de fácil manutenção e com potencial para integração com funcionalidades nativas do sistema operacional.

## ✨ Funcionalidades Atuais

* **Interface Gráfica Nativa:** Construída com Flet, oferecendo uma experiência de usuário rápida e responsiva.
* **Navegação entre Páginas:** Navegação entre as seções "Início" e "Fale Conosco" sem a necessidade de um navegador.
* **Banner de Apresentação:** Seção principal que introduz a clínica ZAPET e seus serviços.
* **Carrossel de Imagens:** Um carrossel interativo (`ft.Carousel`) que exibe fotos dos serviços e da estrutura da clínica.
* **Formulário de Agendamento (Modal):** Um diálogo modal (`ft.AlertDialog`) permite ao usuário agendar serviços. Após o envio, uma notificação de confirmação (`ft.SnackBar`) é exibida.
* **Seção de Depoimentos:** Exibe comentários de clientes satisfeitos para gerar credibilidade.
* **Página de Contato:** Uma view dedicada com um formulário para envio de mensagens diretas para a clínica.

## 🗺️ Roadmap de Desenvolvimento (Pós-migração para Flet)

Este é um roadmap sugerido para as próximas etapas do projeto, focando em funcionalidades de uma aplicação desktop.

### Fase 1: Melhorias na Aplicação e Persistência de Dados

-   [ ] **Salvar Agendamentos:** Implementar a lógica para salvar os dados dos formulários de agendamento e contato em um arquivo local (CSV, JSON) ou em um banco de dados simples (SQLite).
-   [ ] **Tema Claro/Escuro:** Adicionar uma opção para o usuário alternar entre um tema claro e escuro na aplicação.
-   [ ] **Melhorar Responsividade:** Testar e ajustar o layout da janela para diferentes tamanhos e resoluções de tela.
-   [ ] **Validação de Formulários:** Adicionar validação em tempo real aos campos de texto (ex: verificar formato do e-mail, preenchimento obrigatório).

### Fase 2: Funcionalidades Adicionais

-   [ ] **Sistema de Notificações:** Enviar notificações nativas do sistema operacional para lembrar os usuários de seus agendamentos.
-   [ ] **Página de Serviços Detalhada:** Criar uma view dedicada para cada serviço com mais informações, fotos e preços.
-   [ ] **Geração de Relatórios:** Criar uma funcionalidade para gerar relatórios simples a partir dos dados de agendamento salvos.
-   [ ] **Integração com API de Calendário:** (Funcionalidade avançada) Conectar com APIs do Google Calendar ou Outlook para criar eventos a partir dos agendamentos.

### Fase 3: Empacotamento e Distribuição

-   [ ] **Criar um Instalador:** Usar ferramentas como `PyInstaller` ou `flet pack` para empacotar a aplicação em um executável (.exe para Windows, .app para macOS) e criar um instalador.
-   [ ] **Ícone da Aplicação:** Definir um ícone personalizado (`patas.png`) para a aplicação e o executável.
-   [ ] **Publicação:** Disponibilizar os instaladores na seção "Releases" do GitHub.