import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, Spacing


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,  # Ajustar máximo en PC
                width="100%",               # Asegura que ocupe todo el ancho en móvil
                margin_y=Size.DEFAULT.value,
                padding=Spacing.LARGE.value,  # Más espacio alrededor del contenido
                align="center",
                style={
                    "@media (max-width: 768px)": {  # Media query para pantallas móviles
                        "padding": "1rem",         # Espacio adicional en los márgenes laterales
                        "margin_x": "1rem",        # Añade margen horizontal
                    }
                },
            )
        ),
        footer(),
        style={
            "width": "100%",                # Elimina cualquier margen negro
            "min_height": "100vh",          # Ocupa toda la altura de la ventana
            "overflow_x": "hidden",         # Evita desbordamiento horizontal
            "margin": "0",                  # Quita márgenes adicionales
            "padding": "0",                 # Quita relleno extra
            "box_sizing": "border-box",     # Ajuste para que todo esté dentro del ancho
        }
    )



# Crear y compilar la app
app = rx.App(
    style=styles.BASE_STYLE,
)

app.add_page(index)
app._compile
