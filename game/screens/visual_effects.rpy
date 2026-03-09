image leaf_particle:
    Text("{size=24}{color=#b8763a}\U0001f342{/color}{/size}")

image leaf_particle_2:
    Text("{size=20}{color=#c4883f}\U0001f341{/color}{/size}")

image leaf_particle_3:
    Text("{size=18}{color=#8b5e34}\U0001f343{/color}{/size}")

transform leaf_fall(start_x, duration, sway):
    xpos start_x
    ypos -30
    alpha 0.0
    rotate 0

    parallel:
        ease 1.0 alpha 0.7
        ease (duration - 2.0) alpha 0.7
        ease 1.0 alpha 0.0
    parallel:
        linear duration ypos 750
    parallel:
        ease (duration * 0.5) xpos (start_x + sway)
        ease (duration * 0.5) xpos (start_x - sway * 0.3)
    parallel:
        linear duration rotate 360

    repeat

screen leaf_overlay():
    zorder 1

    for i, params in enumerate([
        (0.05, 12.0, 80, "leaf_particle"),
        (0.25, 15.0, -60, "leaf_particle_2"),
        (0.45, 10.0, 50, "leaf_particle_3"),
        (0.65, 14.0, -70, "leaf_particle"),
        (0.80, 11.0, 40, "leaf_particle_2"),
        (0.15, 16.0, -50, "leaf_particle_3"),
        (0.55, 13.0, 60, "leaf_particle"),
        (0.90, 9.0, -40, "leaf_particle_2"),
    ]):
        add params[3] at leaf_fall(int(params[0] * 1280), params[1], params[2]):
            pass


screen vignette_overlay():
    zorder 2
    if not (main_menu or renpy.get_screen("game_menu")):
        add Solid("#000000"):
            ysize 200
            ypos 520
            alpha 0.35
        add Solid("#000000"):
            xsize 80
            ysize 720
            xpos 0
            alpha 0.12
        add Solid("#000000"):
            xsize 80
            ysize 720
            xpos 1200
            alpha 0.12


screen location_label(place):
    zorder 5
    timer 3.0 action Hide("location_label")

    frame:
        xalign 0.5
        yalign 0.15
        xpadding 30
        ypadding 10
        background "#00000066"

        text place:
            color "#e8c09a"
            size 22
            font "DejaVuSans.ttf"


init python:
    config.overlay_screens.append("vignette_overlay")
