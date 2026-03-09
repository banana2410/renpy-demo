# Autumn in Pinewood

A short visual novel built with [Ren'Py](https://www.renpy.org/). You arrive at a café in a small mountain town on an autumn afternoon and meet a couple of locals. Choices shape your personality and relationships, leading to one of 7 endings across two acts.

## Playing the game

Pre-built versions are in `autumn_in_pinewood-1.0-dists/`:

- **Windows** — open `autumn_in_pinewood-1.0-pc/` and run `autumn_in_pinewood.exe`
- **Mac** — open `autumn_in_pinewood.app`

## Controls

- **J** — open/close the journal (tracks personality, relationships, and memories)
- **R** — toggle the relationship stats overlay

## Project structure

```
game/
  script.rpy              — entry point
  variables.rpy           — all game state (flags, affection, personality)
  definitions.rpy         — character definitions, constants, images
  options.rpy             — window title, build config, transitions
  text_utils.rpy          — dynamic narration helpers (mood text, journal entries)
  story/
    cafe_arrival.rpy      — act 1: arriving in Pinewood, meeting Sam
    riley_scene.rpy       — Riley conversation (called from cafe_arrival)
    endings.rpy           — ending router + act 1 endings
    festival_morning.rpy  — act 2: harvest festival, final endings
  screens/
    journal_screen.rpy    — journal UI
    relationship_screen.rpy — stats overlay
    visual_effects.rpy    — leaf particles, location labels
```
