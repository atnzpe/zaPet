# main.py (Versão Final e Completa)

import flet as ft
import time

# --- Mapeamento de Cores e Fontes do CSS ---
# Extraído de styles.css e contato.css
COLOR_PRIMARY = "#5eb5fd"
COLOR_BACKGROUND = "#EEEEEE"
COLOR_TEXT = "#1e1e1e"
COLOR_HEADER_BG = "#FFFFFF"
FONT_FAMILY = "Poppins"


def main(page: ft.Page):
    """
    Função principal que constrói a interface da aplicação ZAPET com Flet.
    """
    # --- Configurações Iniciais da Página ---
    page.title = "Zapet"
    page.window_width = 1200
    page.window_height = 800
    page.fonts = {
        FONT_FAMILY: "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
    }
    page.theme = ft.Theme(font_family=FONT_FAMILY)
    page.bgcolor = COLOR_BACKGROUND
    page.padding = 0

    # --- Diálogo/Modal de Agendamento ---
    # Tradução do formulário popup (myForm) de index.html e main.js
    def close_dialog(e):
        dialog.open = False
        page.update()

    def submit_form(e):
        # Lógica de submissão do formulário
        # Aqui você poderia, por exemplo, salvar os dados em um arquivo ou banco de dados
        print("Formulário enviado:")
        print(f"  Nome do Pet: {pet_name.value}")
        print(f"  CPF do Tutor: {tutor_cpf.value}")
        print(f"  Telefone: {tutor_phone.value}")
        print(f"  Serviço: {service_dropdown.value}")

        close_dialog(e)
        # Exibe uma notificação de sucesso
        page.snack_bar = ft.SnackBar(ft.Text("Ok! Entraremos em contato!"), open=True)
        page.update()

    pet_name = ft.TextField(label="Nome do Pet", border_radius=4)
    tutor_cpf = ft.TextField(label="CPF do Tutor", border_radius=4)
    tutor_phone = ft.TextField(label="Telefone do Tutor", border_radius=4)
    service_dropdown = ft.Dropdown(
        label="Serviço",
        options=[
            ft.dropdown.Option("Banho e/ou tosa"),
            ft.dropdown.Option("Consulta"),
            ft.dropdown.Option("Hotelzinho"),
            ft.dropdown.Option("Day-care"),
            ft.dropdown.Option("Dog-walker"),
        ],
        border_radius=4,
    )

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(
            "AGENDE SEU SERVIÇO!", text_align=ft.TextAlign.CENTER, color=COLOR_TEXT
        ),
        content=ft.Column(
            width=500,
            controls=[pet_name, tutor_cpf, tutor_phone, service_dropdown],
            tight=True,
        ),
        actions=[
            ft.ElevatedButton(
                "Submeter",
                on_click=submit_form,
                style=ft.ButtonStyle(bgcolor=COLOR_PRIMARY, color="white"),
            ),
            ft.TextButton("Fechar", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_dialog(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    # --- FUNÇÕES DE CONSTRUÇÃO DE VIEWS (PÁGINAS) ---

    def build_home_view():
        # --- Seção Banner ---
        banner = ft.Container(
            bgcolor=COLOR_PRIMARY,
            padding=ft.padding.symmetric(horizontal=100, vertical=40),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=40,
                controls=[
                    ft.Column(
                        expand=True,
                        controls=[
                            ft.Text("ZAPET", size=55, weight=ft.FontWeight.W_700),
                            ft.Text(
                                "Nós somos a Zapet! Sua mais nova clínica veterinária do Recife. "
                                "Temos uma excelente equipe de veterinários das mais diversas áreas "
                                "prontos para cuidar do seu animalzinho. Dispomos também de uma "
                                "loja com uma ampla rede de medicamentos e acessórios de altíssima "
                                "qualidade! Ofertamos os serviços de banho, tosa, dog-walker, "
                                "day-care, hotelzinho 24h e muito mais!",
                                size=16,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.ElevatedButton(
                                "Saber mais",
                                icon=ft.icons.ARROW_FORWARD,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    padding=ft.padding.symmetric(
                                        horizontal=40, vertical=15
                                    ),
                                ),
                            ),
                        ],
                    ),
                    ft.Image(src="logo.png", width=350, height=350),
                ],
            ),
        )

        # --- Seção Carrossel ---
        carousel_images = [
            "consultavet.jpg",
            "hotel.jpg",
            "Post_banho_e_tosa.jpg",
            "farmacia.png",
            "walker.jpeg",
            "recep.jpg",
        ]
        carousel = ft.Carousel(
            width=1000,
            height=400,
            page_snapping=True,
            controls=[
                ft.Image(
                    src=img,
                    fit=ft.ImageFit.COVER,
                    border_radius=ft.border_radius.all(10),
                )
                for img in carousel_images
            ],
        )

        # --- Seção Depoimentos ---
        testimonials = ft.Container(
            padding=ft.padding.all(50),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "O que nossos clientes dizem:",
                                size=22,
                                weight=ft.FontWeight.W_500,
                                italic=True,
                            ),
                            ft.ElevatedButton(
                                "AGENDE JÁ!",
                                on_click=open_dialog,
                                style=ft.ButtonStyle(
                                    bgcolor=COLOR_PRIMARY,
                                    color=COLOR_TEXT,
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    padding=ft.padding.all(20),
                                ),
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=40,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                bgcolor=COLOR_PRIMARY,
                                padding=24,
                                border_radius=25,
                                width=400,
                                content=ft.Column(
                                    [
                                        ft.Text(
                                            "Joaquina disse:",
                                            size=22,
                                            weight=ft.FontWeight.W_700,
                                        ),
                                        ft.Text("22, Janeiro, 2024", size=18),
                                        ft.Text(
                                            "Eu amo a Zapet! Sempre levo meu cachorrinho e somos muito bem atendidos. Especialmente por Dra. Maria, que é uma veterinária super competente e paciente.",
                                            size=20,
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(
                                bgcolor=COLOR_PRIMARY,
                                padding=24,
                                border_radius=25,
                                width=400,
                                content=ft.Column(
                                    [
                                        ft.Text(
                                            "Alex disse:",
                                            size=22,
                                            weight=ft.FontWeight.W_700,
                                        ),
                                        ft.Text("26, Março 2024", size=18),
                                        ft.Text(
                                            'O melhor preço de ração é aqui! Sempre encontro tudo que preciso na lojinha. Sem contar do hotelzinho, quando preciso viajar deixo meus "filhinhos" sem preocupações! A estrutura é excelente e o atendimento dos funcionários é maravilhoso! Super recomendo a Zapet!',
                                            size=20,
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

        return ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=0,
            controls=[
                banner,
                ft.Container(
                    content=carousel,
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=30),
                ),
                testimonials,
            ],
        )

    def build_contact_view():
        # Tradução da página contato.html
        return ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=500,
                    padding=40,
                    border_radius=10,
                    bgcolor="#d9d9d9",
                    border=ft.border.all(2, COLOR_TEXT),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Fale conosco",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=COLOR_TEXT,
                            ),
                            ft.TextField(label="Nome", text_transform="uppercase"),
                            ft.TextField(label="Email"),
                            ft.TextField(
                                label="Mensagem",
                                multiline=True,
                                min_lines=4,
                                max_lines=4,
                            ),
                            ft.ElevatedButton(
                                "Enviar",
                                width=200,
                                style=ft.ButtonStyle(
                                    bgcolor=COLOR_PRIMARY, color="white"
                                ),
                            ),
                        ]
                    ),
                )
            ],
        )

    # --- LÓGICA DE NAVEGAÇÃO ---

    # Dicionário mapeando rotas para funções de construção
    views = {"/": build_home_view(), "/contato": build_contact_view()}

    # Conteúdo principal da página que será trocado
    main_content = ft.Container(expand=True, content=views["/"])

    def navigate_to(e):
        # Obtém a rota do 'data' do TextButton clicado
        route = e.control.data
        main_content.content = views[route]
        main_content.update()

    # --- Header (com navegação) ---
    header = ft.Container(
        height=80,
        bgcolor=COLOR_HEADER_BG,
        padding=ft.padding.symmetric(horizontal=100),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    "ZAPET", size=24, weight=ft.FontWeight.W_700, color=COLOR_PRIMARY
                ),
                ft.Row(
                    spacing=40,
                    controls=[
                        ft.TextButton(
                            "Início",
                            data="/",
                            on_click=navigate_to,
                            style=ft.ButtonStyle(color=COLOR_TEXT),
                        ),
                        ft.TextButton(
                            "Serviços",
                            data="/",
                            on_click=navigate_to,
                            style=ft.ButtonStyle(color=COLOR_TEXT),
                        ),  # Levando para a home por enquanto
                        ft.TextButton(
                            "Fale Conosco",
                            data="/contato",
                            on_click=navigate_to,
                            style=ft.ButtonStyle(color=COLOR_TEXT),
                        ),
                    ],
                ),
            ],
        ),
    )

    # --- Rodapé ---
    footer = ft.Container(
        bgcolor=COLOR_TEXT,
        padding=20,
        content=ft.Text(
            "ZAPET: Empresa do ramo veterinário que atua como clínica e pet shop desde 2023. \n"
            "Desenvolvedores: Luciana Melo & Junior",
            color="#d9d9d990",
            text_align=ft.TextAlign.CENTER,
        ),
    )

    # --- Layout Principal ---
    page.add(header, main_content, footer)
    page.update()


# --- Inicia a aplicação ---
ft.app(target=main, assets_dir="PROJETO ZAPET")
