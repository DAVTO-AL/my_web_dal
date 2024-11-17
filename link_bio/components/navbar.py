import reflex as rx
from link_bio.styles import styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
 
def navbar() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.flex(
                rx.text("DAV",
                    color=Color.PRIMARY.value),
                rx.text("ID",
                    color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            )
        ),
        position="sticky", 
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )
    