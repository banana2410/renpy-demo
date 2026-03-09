# Autumn in Pinewood

A short visual novel built with Ren'Py. You arrive at a café in a small mountain town on an autumn afternoon and meet a couple of locals. Choices shape your personality and relationships, leading to one of 8 endings across two acts.

## How to run

1. Download [Ren'Py](https://www.renpy.org/latest.html)
2. Drop this project in your Ren'Py projects directory
3. Launch from the Ren'Py launcher

## Structure

Story scripts are in `game/story/`, screens and UI in `game/screens/`. Game state is centralized in `variables.rpy` with save compatibility patching. Dynamic narration is generated through Python helpers in `text_utils.rpy`.

Press J for the journal, R for a quick stats overlay.
