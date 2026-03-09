# personality — negative = reserved/cautious, positive = warm/curious
default personality_warmth = 0
default personality_curiosity = 0

## Relationships (0-10)
default sam_affection = 0
default riley_affection = 0

## Flags
default helped_sam = False
default asked_about_town = False
default shared_book_interest = False

## What the player picked
default first_impression = "neutral"
default drink_choice = "coffee"

## Café conversation
default sam_topics_asked = set()

## Festival scene
default festival_topics_asked = set()
default festival_volunteered = False
default festival_trail_promised = False
default took_bird_guide = False

# hud
default show_relationships = False

## Patch missing vars for old saves
label after_load:
    if not hasattr(store, "shared_book_interest"):
        $ shared_book_interest = False
    if not hasattr(store, "show_relationships"):
        $ show_relationships = False
    if not hasattr(store, "sam_topics_asked"):
        $ sam_topics_asked = set()
    if not hasattr(store, "festival_topics_asked"):
        $ festival_topics_asked = set()
    if not hasattr(store, "festival_volunteered"):
        $ festival_volunteered = False
    if not hasattr(store, "festival_trail_promised"):
        $ festival_trail_promised = False
    if not hasattr(store, "took_bird_guide"):
        $ took_bird_guide = False
    return
