import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def links() -> rx.Component:
    return rx.vstack(
        title("Más redes",),
        link_button("Twitch", 
                    "Siempre en vivo",
                    "https://www.twitch.tv/dall_as_",
                    "/icons/twitch.svg"),
        link_button("YouTube", 
                    "Amande de las musicas",
                    "https://www.youtube.com/@d-v-k-t-o",
                    "/icons/youtube.svg"),
        
        link_button("Discord", 
                    "Una forma mas para estar en contacto",
                    "https://discord.com/channels/@me/856544537660751883",
                    "/icons/discord.svg"),
         link_button(
            "linkedin",
            "Aún en trabajo",
            "https://www.linkedin.com/in/david-araoz-lopinta-2a5115301/",
            "/icons/linkedin.svg"
        
        ),
        title("Mis proyectos",),
        link_button("Git", 
                    "En trabajo",
                    " ",
                    "/icons/git.svg"
                    ),
        link_button("Git hub", 
                    "En trabajo",
                    "https://github.com/DAVTO-AL",
                    "/icons/github.svg"
                    ),
        title("Canales recomendados"),
        
        link_button("Libros", 
                    "los libros simpre estaran ahí",
                    " ",
                    "/icons/corazon.svg"
                    ),
        
        link_button("Peliculas", 
                    "Cuando quieras :3",
                    " ",
                    "/icons/corazon.svg"),
        
        
        link_button("Musicas", 
                    "Una forma mas para estar en contacto",
                    " ",
                    "/icons/corazon.svg"),
        

        width="100%",
        spacing=Size.SMALL.value,
        align="center"
    )