style journal_frame:
    background "#1a1410ee"
    xsize 780
    ysize 580
    xalign 0.5
    yalign 0.5
    padding (40, 35, 40, 35)

style journal_title:
    color "#e8c09a"
    size 32
    bold True
    xalign 0.5

style journal_subtitle:
    color "#d4845a"
    size 20
    bold True

style journal_body:
    color "#c8b8a0"
    size 17

style journal_muted:
    color "#7a6e62"
    size 15

style journal_entry_title:
    color "#e8b87a"
    size 18
    bold True

style journal_entry_text:
    color "#b8a890"
    size 16

style journal_icon:
    color "#d4845a"
    size 22

style journal_bar_label:
    color "#c8b8a0"
    size 16
    min_width 80

style journal_bar_value:
    color "#e8b87a"
    size 15


transform journal_fadein:
    alpha 0.0
    ease 0.3 alpha 1.0

transform journal_fadeout:
    alpha 1.0
    ease 0.2 alpha 0.0


screen journal():
    modal True
    zorder 100

    add Solid("#00000088")

    frame:
        style "journal_frame"
        at journal_fadein

        vbox:
            spacing 5

            hbox:
                xfill True
                text "Journal" style "journal_title" xalign 0.0
                textbutton "{size=24}\u2715{/size}":
                    xalign 1.0
                    yalign 0.0
                    text_color "#7a6e62"
                    text_hover_color "#e8c09a"
                    action Hide("journal", transition=dissolve)

            add Solid("#d4845a44"):
                xsize 700
                ysize 2
                xalign 0.5

            null height 5

            viewport:
                mousewheel True
                scrollbars "vertical"
                xfill True
                ysize 480

                vbox:
                    spacing 18

                    ## Personality
                    text "Who You Are" style "journal_subtitle"

                    null height 2

                    hbox:
                        spacing 12
                        yalign 0.5
                        text "Warmth" style "journal_bar_label"

                        bar:
                            value AnimatedValue(
                                max(0.0, min(1.0, (personality_warmth + 3) / 8.0)),
                                1.0, 0.5
                            )
                            xsize 320
                            ysize 14
                            left_bar Solid("#e8a735")
                            right_bar Solid("#3a3228")
                            thumb None

                        $ _warmth_label = get_personality_label("warmth", personality_warmth)
                        text "[_warmth_label]" style "journal_bar_value"

                    hbox:
                        spacing 12
                        yalign 0.5
                        text "Curiosity" style "journal_bar_label"

                        bar:
                            value AnimatedValue(
                                max(0.0, min(1.0, (personality_curiosity + 3) / 8.0)),
                                1.0, 0.5
                            )
                            xsize 320
                            ysize 14
                            left_bar Solid("#7bc77b")
                            right_bar Solid("#3a3228")
                            thumb None

                        $ _curiosity_label = get_personality_label("curiosity", personality_curiosity)
                        text "[_curiosity_label]" style "journal_bar_value"

                    null height 5
                    add Solid("#d4845a22"):
                        xsize 660
                        ysize 1
                        xalign 0.5

                    ## Relationships
                    text "Relationships" style "journal_subtitle"

                    null height 2

                    hbox:
                        spacing 12
                        yalign 0.5
                        text "{color=#e8a735}Sam{/color}" style "journal_bar_label"

                        bar:
                            value AnimatedValue(
                                max(0.0, min(1.0, sam_affection / 8.0)),
                                1.0, 0.5
                            )
                            xsize 320
                            ysize 14
                            left_bar Solid("#e8a735")
                            right_bar Solid("#3a3228")
                            thumb None

                        $ _sam_label = get_relationship_label(sam_affection)
                        text "[_sam_label]" style "journal_bar_value"

                    hbox:
                        spacing 12
                        yalign 0.5
                        text "{color=#7ba1c7}Riley{/color}" style "journal_bar_label"

                        bar:
                            value AnimatedValue(
                                max(0.0, min(1.0, riley_affection / 8.0)),
                                1.0, 0.5
                            )
                            xsize 320
                            ysize 14
                            left_bar Solid("#7ba1c7")
                            right_bar Solid("#3a3228")
                            thumb None

                        $ _riley_label = get_relationship_label(riley_affection)
                        text "[_riley_label]" style "journal_bar_value"

                    null height 5
                    add Solid("#d4845a22"):
                        xsize 660
                        ysize 1
                        xalign 0.5

                    ## Memories — grows as the player does things
                    $ _entries = get_journal_entries()

                    if _entries:
                        text "Memories" style "journal_subtitle"

                        null height 2

                        for _entry in _entries:
                            hbox:
                                spacing 14
                                yalign 0.0

                                text _entry["icon"] style "journal_icon" yalign 0.0 yoffset 2

                                vbox:
                                    spacing 3
                                    text _entry["title"] style "journal_entry_title"
                                    text _entry["text"] style "journal_entry_text"

                            null height 4

                    else:
                        null height 10
                        text "No memories yet. Your story is just beginning." style "journal_muted" xalign 0.5

                    null height 15
                    text "Press {color=#e8b87a}J{/color} or {color=#e8b87a}Esc{/color} to close" style "journal_muted" xalign 0.5

    key "j" action Hide("journal", transition=dissolve)
    key "K_ESCAPE" action Hide("journal", transition=dissolve)
    key "game_menu" action Hide("journal", transition=dissolve)


screen journal_keybind():
    if not renpy.get_screen("journal") and not main_menu and not renpy.get_screen("game_menu"):
        key "j" action Show("journal", transition=dissolve)

init python:
    config.overlay_screens.append("journal_keybind")
