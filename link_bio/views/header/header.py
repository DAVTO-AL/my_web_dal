import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor
from link_bio.styles.colors import Color
from link_bio.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack(
        # Contenedor para el avatar y el título
        rx.hstack(
            # Avatar con tamaño adaptable
            rx.avatar(
                name="Araoz Lupinta",
                size="8",  # Tamaño base
                margin_y="5px",
                fallback=":)",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                src="https://i.blogs.es/0ca9a6/aa/1366_2000.jpeg",
                border="4px",
                padding="2px",
            ),
            # Título e íconos en un vstack
            rx.vstack(
                rx.heading(
                    rx.text(
                        "D_V_K_O",
                        size="lg",
                        margin_top="1px",
                        text_align="center",
                    ),
                    width="100%",
                ),
                rx.box(
                    rx.text(
                        "pagina en mantenimineto*",
                        margin_top="-3px",
                        color=Color.PRIMARY.value,
                        text_align="center",
                    ),
                    width="100%",
                ),
                # Íconos más grandes con espaciado ajustable y centrados
                rx.hstack(
                    link_icon(
                        "/icons/facebook.svg",
                        "https://www.facebook.com/david.araozlopinta.9",
                        "facebook",
                    ),
                    rx.text("/"),
                    link_icon(
                        "/icons/pinterest.svg",
                        "https://pin.it/45kViYwsA",
                        "pinterest",
                    ),
                    rx.text("/"),
                    link_icon(
                        "/icons/instagram.svg",
                        "https://www.instagram.com/davidaraozlopinta/",
                        "Instagram",
                    ),
                    rx.text("/"),
                    link_icon(
                        "/icons/tiktok.svg",
                        "https://www.tiktok.com/@davidlopinta1",
                        "TikTok",
                    ),
                    rx.text("/"),
                    link_icon(
                        "/icons/spotify.svg",
                        "https://open.spotify.com/playlist/7m8zhrvgXFwIeiphzoZnBW?si=I8ACfVsCQK2eD1Y4v77Z2A&pi=NcDlXDi1QUO32",
                        "Spotify",
                    ),
                    width="100%",
                    justify="center",
                    align_items="center",
                    style={
                        "font_size": "1.5rem",
                        "gap": "1rem",
                        "@media (max-width: 537px)": {
                            "font_size": "1.2rem",
                            "gap": "0.8rem",
                            "flex_direction": "row",
                        },
                    },
                ),
                width="100%",
            ),
            justify="center",
            align_items="center",
            width="100%",
            style={
                "@media (max-width: 537px)": {
                    "flex_direction": "column",
                }
            },
        ),
        # Contenedor para los textos debajo del avatar (comienzos, universitario, proyectos)
        rx.flex(
            info_text("2021", "Mis comienzos"),
            rx.spacer(),
            info_text("2024", "Universitario"),
            rx.spacer(),
            info_text("(+)", "Proyectos"),
            width="100%",
            justify="space-between",
            style={
                "@media (max-width: 537px)": {
                    "flex_direction": "column",  # Cambia a disposición vertical
                    "align_items": "center",  # Centra el contenido
                    "gap": "0.3rem",  # Reduce aún más el espacio entre los elementos
                    "text_align": "center",  # Alinea el texto al centro
                },
            },
        ),
        # Texto principal con márgenes adaptables
        rx.box(
            rx.text(
                "Hola, me gusta que llamen Da-vid. Soy un estudiante de Ingeniería Informática y de Sistemas en busca de conocimiento y de seguir formando mi camino como freelance. Esta página de presentación es parte de una serie de proyectos que tengo planeados. ¡Así que espero que me conozcas más! ¡Bienvenid@!",
                color=TextColor.BODY.value,
                text_align="justify",
            ),
            width="100%",
            padding_x="0.3rem",
            padding_y="0.5rem",
        ),
        spacing=Size.DEFAULT.value,
        align_items="center",
    )
