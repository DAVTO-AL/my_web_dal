import reflex as rx
import datetime as dat
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="DD.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de MoureDev. Una \"eme\" entre llaves.",
            style={
                "@media (max-width: 480px)": {  # Para pantallas pequeñas
                    "height": "70px",  # Tamaño reducido
                    "width": "70px",
                }
            },
        ),
        rx.box(
            rx.box(
                rx.text(
                    "davidaraozlopinta@gmail.com",
                    align="center",
                    margin_bottom="5px",
                    style={
                        "@media (max-width: 480px)": {  # Para pantallas pequeñas
                            "font_size": "12px",  # Reduce el tamaño de la fuente
                            "text_align": "center",
                        }
                    },
                ),
                f"© 2005-{dat.date.today().year} años vivo en este ",
                rx.text(
                    "planeta",
                    as_="span",
                    color=Color.PRIMARY.value,
                ),
                spacing=Spacing.BIG.value,
                padding_top=Size.DEFAULT.value,
                style={
                    "@media (max-width: 480px)": {  # Para pantallas pequeñas
                        "font_size": "12px",  # Reduce el tamaño de la fuente
                        "text_align": "center",  # Alinea el texto al centro
                    }
                },
            ),
            font_size=Size.MEDIUM.value,
        ),
        rx.box(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub",
                    style={
                        "margin_top": "-10px",  # Ajusta la posición hacia arriba
                        "@media (max-width: 480px)": {  # Para pantallas pequeñas
                            "height": "25px",  # Reduce el tamaño del icono
                            "width": "25px",
                            "margin_top": "-5px",  # Menos margen hacia arriba en móviles
                        },
                    },
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    style={
                        "@media (max-width: 480px)": {  # Para pantallas pequeñas
                            "font_size": "10px",  # Reduce el tamaño del texto
                            "text_align": "center",  # Centra el texto
                        }
                    },
                ),
            ),
            is_external=True,
            spacing=Spacing.SMALL.value,
            style={
                "@media (max-width: 480px)": {  # Para pantallas pequeñas
                    "flex_direction": "column",  # Cambia a disposición vertical
                    "align_items": "center",  # Centra el contenido
                }
            },
        ),
        rx.box(
            height="2px",  # Grosor de la línea
            width="100%",  # Ancho inicial completo
            max_width="490px",  # Ancho máximo de la línea
            background_color=Color.SECONDARY.value,  # Color de la línea
            margin_top=Spacing.DEFAULT.value,  # Espaciado antes de la línea
            align_self="center",  # Asegura que esté centrada
            style={
                "@media (max-width: 480px)": {  # Para pantallas pequeñas
                    "max_width": "80%",  # Reduce el ancho máximo
                }
            },
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        align="center",
        color=TextColor.FOOTER.value,
        style={
            "@media (max-width: 480px)": {  # Para pantallas pequeñas
                "padding_bottom": "10px",  # Reduce el relleno inferior
                "margin_bottom": "10px",  # Reduce el margen inferior
            }
        },
    )
