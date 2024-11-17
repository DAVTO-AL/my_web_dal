import reflex as rx
from link_bio.styles.colors import TextColor as Textcolor
from link_bio.styles.colors import Color as color
from link_bio.styles.styles import Size as Size

def info_text(title:str, body: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
            title, font_weight="bold",
            color=color.PRIMARY.value
            
        ),
        f"{body}",font_size=Size.MEDIUM.value),
        color=Textcolor.BODY.value
    )