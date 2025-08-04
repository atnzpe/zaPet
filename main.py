# main.py (Versão Final e Definitiva)

import flet as ft
import logging

# --- 1. Configuração do Sistema de Logging Detalhado ---
# Nível DEBUG para capturar cada passo
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
    handlers=[
        logging.FileHandler("zapet_app.log"),
        logging.StreamHandler()
    ]
)

# --- Mapeamento de Cores e Fontes ---
COLOR_PRIMARY = "#5eb5fd"
COLOR_BACKGROUND = "#EEEEEE"
COLOR_TEXT = "#1e1e1e"
COLOR_HEADER_BG = "#FFFFFF"
FONT_FAMILY = "Poppins"

def main(page: ft.Page):
    """
    Função principal que constrói a interface da aplicação ZAPET com Flet.
    """
    logging.info("Aplicação ZAPET iniciada.")
    
    page.title = "Zapet"
    page.window_width = 1200
    page.window_height = 800
    page.fonts = {
        FONT_FAMILY: "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"
    }
    page.theme = ft.Theme(font_family=FONT_FAMILY)
    page.bgcolor = COLOR_BACKGROUND
    page.padding = 0

    def open_dialog(e):
        logging.info("Botão 'AGENDE JÁ!' clicado.")
        logging.debug("Abrindo diálogo de agendamento.")
        page.dialog = dialog
        dialog.open = True
        page.update()

    def close_dialog(e):
        if page.dialog:
            logging.debug("Fechando diálogo de agendamento.")
            page.dialog.open = False
            page.update()
    
    def submit_form(e):
        logging.info("Formulário de agendamento submetido.")
        close_dialog(e)
        page.snack_bar = ft.SnackBar(ft.Text("Agendamento recebido! Entraremos em contato!"), open=True)
        page.update()

    pet_name = ft.TextField(label="Nome do Pet", border_radius=4)
    tutor_cpf = ft.TextField(label="CPF do Tutor", border_radius=4)
    tutor_phone = ft.TextField(label="Telefone do Tutor", border_radius=4)
    service_dropdown = ft.Dropdown(
        label="Serviço",
        options=[
            ft.dropdown.Option("Banho e/ou tosa"), ft.dropdown.Option("Consulta"),
            ft.dropdown.Option("Hotelzinho"), ft.dropdown.Option("Day-care"),
            ft.dropdown.Option("Dog-walker"),
        ],
        border_radius=4
    )

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("AGENDE SEU SERVIÇO!", text_align=ft.TextAlign.CENTER, color=COLOR_TEXT),
        content=ft.Column(controls=[pet_name, tutor_cpf, tutor_phone, service_dropdown], tight=True),
        actions=[
            ft.ElevatedButton("Submeter", on_click=submit_form, style=ft.ButtonStyle(bgcolor=COLOR_PRIMARY, color="white")),
            ft.TextButton("Fechar", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def build_home_view():
        logging.info("Construindo a view 'Início'.")
        
        carousel_images_list = [
            "consultavet.jpg", "hotel.jpg", "Post_banho_e_tosa.jpg",
            "farmacia.png", "walker.jpeg", "recep.jpg"
        ]
        
        image_controls = [
            ft.Image(key=str(i), src=img, fit=ft.ImageFit.COVER, border_radius=10, width=380)
            for i, img in enumerate(carousel_images_list)
        ]

        image_carousel = ft.GridView(
            expand=False, height=400, runs_count=1, horizontal=True,
            padding=ft.padding.symmetric(horizontal=20), spacing=20,
            controls=image_controls
        )

        # Usamos um dicionário dentro da função para manter o estado do índice
        carousel_state = {"current_index": 0}

        def go_next(e):
            logging.debug(f"Botão 'próximo' clicado. Índice atual: {carousel_state['current_index']}")
            if carousel_state['current_index'] < len(carousel_images_list) - 1:
                carousel_state['current_index'] += 1
                image_carousel.scroll_to(key=str(carousel_state['current_index']), duration=500)
                logging.debug(f"Carrossel avançou para o índice: {carousel_state['current_index']}")
        
        def go_prev(e):
            logging.debug(f"Botão 'anterior' clicado. Índice atual: {carousel_state['current_index']}")
            if carousel_state['current_index'] > 0:
                carousel_state['current_index'] -= 1
                image_carousel.scroll_to(key=str(carousel_state['current_index']), duration=500)
                logging.debug(f"Carrossel voltou para o índice: {carousel_state['current_index']}")

        carousel_with_buttons = ft.Stack(
            [
                image_carousel,
                ft.Container(
                    # CORREÇÃO: Cor do ícone e função de clique
                    content=ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS_NEW, icon_color=COLOR_PRIMARY, on_click=go_prev),
                    alignment=ft.alignment.center_left,
                ),
                ft.Container(
                    # CORREÇÃO: Cor do ícone e função de clique
                    content=ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS, icon_color=COLOR_PRIMARY, on_click=go_next),
                    alignment=ft.alignment.center_right,
                )
            ]
        )
        
        return ft.Column(
            expand=True, scroll=ft.ScrollMode.AUTO, spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    bgcolor=COLOR_PRIMARY, padding=ft.padding.symmetric(horizontal=100, vertical=40),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=40,
                        controls=[
                            ft.Column(
                                expand=True, spacing=20,
                                controls=[
                                    ft.Text("ZAPET", size=55, weight=ft.FontWeight.W_700, color=COLOR_TEXT),
                                    ft.Text("Nós somos a Zapet! Sua mais nova clínica veterinária do Recife...", size=16, weight=ft.FontWeight.W_600, color=COLOR_TEXT),
                                    ft.ElevatedButton("Saber mais", icon=ft.Icons.ARROW_FORWARD, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), padding=15))
                                ]
                            ),
                            ft.Image(src="logo.png", width=350, height=350)
                        ]
                    )
                ),
                ft.Container(content=carousel_with_buttons, alignment=ft.alignment.center, margin=ft.margin.only(top=71)),
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=50, vertical=20),
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("O que nossos clientes dizem:", size=22, weight=ft.FontWeight.W_500, italic=True),
                                    ft.ElevatedButton("AGENDE JÁ!", on_click=open_dialog, style=ft.ButtonStyle(bgcolor=COLOR_PRIMARY, color=COLOR_TEXT, shape=ft.RoundedRectangleBorder(radius=8), padding=20))
                                ]
                            ),
                            ft.Row(
                                spacing=40, alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(bgcolor=COLOR_PRIMARY, padding=24, border_radius=25, width=400, content=ft.Column([ft.Text("Joaquina disse:", size=22, weight=ft.FontWeight.W_700), ft.Text("22, Janeiro, 2024", size=18), ft.Text("Eu amo a Zapet! Sempre levo meu cachorrinho e somos muito bem atendidos...", size=20)])),
                                    ft.Container(bgcolor=COLOR_PRIMARY, padding=24, border_radius=25, width=400, content=ft.Column([ft.Text("Alex disse:", size=22, weight=ft.FontWeight.W_700), ft.Text("26, Março 2024", size=18), ft.Text("O melhor preço de ração é aqui! Super recomendo a Zapet!", size=20)]))
                                ]
                            )
                        ]
                    )
                )
            ]
        )

    def build_contact_view():
        logging.info("Construindo a view 'Fale Conosco'.")
        def send_contact_form(e):
            logging.info("Formulário de contato enviado.")
            page.snack_bar = ft.SnackBar(ft.Text("Mensagem recebida! Obrigado pelo contato."), open=True)
            page.update()

        return ft.Column(
            expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=500, padding=40, border_radius=10, bgcolor="#d9d9d9", border=ft.border.all(2, COLOR_TEXT),
                    content=ft.Column([
                        ft.Text("Fale conosco", size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT),
                        ft.TextField(label="Nome", capitalization=ft.TextCapitalization.CHARACTERS),
                        ft.TextField(label="Email"),
                        ft.TextField(label="Mensagem", multiline=True, min_lines=4),
                        ft.ElevatedButton("Enviar", width=200, on_click=send_contact_form, style=ft.ButtonStyle(bgcolor=COLOR_PRIMARY, color="white"))
                    ])
                )
            ]
        )
    
    def navigate_to(e):
        route = e.control.data
        logging.info(f"Navegando para a rota: '{route}'")
        main_view.controls.clear()
        
        if route == "/":
            main_view.controls.append(build_home_view())
        elif route == "/contato":
            main_view.controls.append(build_contact_view())
        
        logging.debug("Atualizando a página após a navegação.")
        page.update()

    header = ft.Container(
        height=80, bgcolor=COLOR_HEADER_BG, padding=ft.padding.symmetric(horizontal=100),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("ZAPET", size=24, weight=ft.FontWeight.W_700, color=COLOR_PRIMARY),
                ft.Row(spacing=40, controls=[
                    ft.TextButton("Início", data="/", on_click=navigate_to, style=ft.ButtonStyle(color=COLOR_TEXT)),
                    ft.TextButton("Serviços", data="/", on_click=navigate_to, style=ft.ButtonStyle(color=COLOR_TEXT)),
                    ft.TextButton("Fale Conosco", data="/contato", on_click=navigate_to, style=ft.ButtonStyle(color=COLOR_TEXT)),
                ])
            ]
        )
    )

    footer = ft.Container(
        bgcolor=COLOR_TEXT, padding=20,
        content=ft.Text(
            "ZAPET: Empresa do ramo veterinário que atua como clínica e pet shop desde 2023. \n"
            "Desenvolvedores: Luciana Melo & Junior",
            color="#d9d9d990", text_align=ft.TextAlign.CENTER
        )
    )

    main_view = ft.Column(expand=True, controls=[build_home_view()])
    page.add(header, main_view, footer)
    logging.info("Layout principal da página adicionado.")

# --- Inicia a aplicação ---
ft.app(target=main, assets_dir="assets")