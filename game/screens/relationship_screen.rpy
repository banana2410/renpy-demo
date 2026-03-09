screen relationship_screen():
    if show_relationships:
        frame:
            xalign 1.0
            yalign 0.0
            xpadding 20
            ypadding 15
            xmargin 10
            ymargin 10
            background "#00000099"

            vbox:
                spacing 8

                text "— Personality —" size 18 color "#ffffff" bold True
                hbox:
                    spacing 10
                    text "Warmth:" size 16 color "#cccccc" min_width 120
                    text "[personality_warmth]" size 16 color "#e8a735"
                hbox:
                    spacing 10
                    text "Curiosity:" size 16 color "#cccccc" min_width 120
                    text "[personality_curiosity]" size 16 color "#7bc77b"

                null height 5

                text "— Relationships —" size 18 color "#ffffff" bold True
                hbox:
                    spacing 10
                    text "Sam:" size 16 color "#cccccc" min_width 120
                    text "[sam_affection]" size 16 color "#e8a735"
                hbox:
                    spacing 10
                    text "Riley:" size 16 color "#cccccc" min_width 120
                    text "[riley_affection]" size 16 color "#7ba1c7"

                null height 5

                text "{size=14}{color=#888888}Press 'R' to hide{/color}{/size}"

    if not main_menu and not renpy.get_screen("game_menu"):
        key "r" action ToggleVariable("show_relationships")

init python:
    config.overlay_screens.append("relationship_screen")
