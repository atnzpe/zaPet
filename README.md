# ZAPET - Aplicação Desktop de Clínica Veterinária com Flet

Este repositório contém o código-fonte da aplicação desktop da ZAPET, uma clínica veterinária e pet shop. O projeto, originalmente uma página web, foi migrado com sucesso para Python utilizando o framework Flet para criar uma experiência de usuário nativa e multiplataforma.

## 🚀 Sobre o Projeto

ZAPET é uma aplicação desktop desenvolvida em Python e Flet. O objetivo é fornecer uma vitrine digital para a clínica, oferecendo informações claras sobre os serviços, e permitir que clientes agendem atendimentos e entrem em contato diretamente pela aplicação. A migração para Flet resultou em uma solução robusta, de fácil manutenção e com potencial para integração com funcionalidades nativas do sistema operacional.

## ✨ Funcionalidades Atuais

* **Interface Gráfica Nativa:** Construída com Flet, oferecendo uma experiência de usuário rápida e com layout fiel ao design original da web.
* **Navegação entre Páginas:** Navegação fluida entre as seções "Início" e "Fale Conosco" sem a necessidade de um navegador.
* **Carrossel de Imagens Interativo:** Um carrossel de imagens (`ft.GridView` horizontal) com botões de navegação funcionais para avançar e retroceder.
* **Formulário de Agendamento (Modal):** Um diálogo modal (`ft.AlertDialog`) permite ao usuário agendar serviços. Após o envio, uma notificação de confirmação (`ft.SnackBar`) é exibida.
* [cite_start]**Sistema de Logging:** Registra os principais eventos da aplicação (inicialização, navegação, cliques e submissão de formulários) em um arquivo `zapet_app.log` [cite: 2] e no console, facilitando a depuração e o monitoramento.
* **Interatividade Completa:** Todos os botões, incluindo "Saber mais" e os de envio de formulário, estão funcionais e fornecem feedback ao usuário.

## 🗺️ Roadmap de Desenvolvimento

Com a migração da interface concluída e estável, estes são os próximos passos sugeridos para a evolução do projeto:

### Fase 1: Persistência de Dados e Melhorias Gerais

* [ ] **Salvar Agendamentos:** Implementar a lógica para salvar os dados dos formulários de agendamento e contato em um arquivo local (CSV, JSON) ou em um banco de dados simples (SQLite).
* [ ] **Tema Claro/Escuro:** Adicionar uma opção para o usuário alternar entre um tema claro e escuro na aplicação.
* [ ] **Validação de Formulários:** Adicionar validação em tempo real aos campos de texto (ex: verificar formato do e-mail, preenchimento obrigatório).

### Fase 2: Funcionalidades Adicionais

* [ ] **Sistema de Notificações:** Enviar notificações nativas do sistema operacional para lembrar os usuários de seus agendamentos.
* [ ] **Página de Serviços Detalhada:** Criar uma view dedicada para cada serviço com mais informações, fotos e preços.
* [ ] **Geração de Relatórios:** Criar uma funcionalidade para gerar relatórios simples a partir dos dados de agendamento salvos.

### Fase 3: Empacotamento e Distribuição

* [ ] **Criar um Instalador:** Usar ferramentas como `PyInstaller` ou `flet pack` para empacotar a aplicação em um executável (`.exe` para Windows, `.app` para macOS).
* [ ] **Ícone da Aplicação:** Definir um ícone personalizado para a aplicação e o executável.
* [ ] **Publicação:** Disponibilizar os instaladores na seção "Releases" do GitHub.