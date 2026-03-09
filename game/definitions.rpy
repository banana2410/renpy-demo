define n = Character(None, kind=nvl_narrator)
define s = Character("Sam", color="#e8a735", who_suffix=":")
define r = Character("Riley", color="#7ba1c7", who_suffix=":")

image bg road_overlay = "images/bg/road_overlay.png"
image bg cafe_exterior = "images/bg/cafe_exterior.png"
image bg cafe_interior = "images/bg/cafe_interior.png"
image bg cafe_counter = "images/bg/cafe_counter.png"
image bg cafe_corner = "images/bg/cafe_corner.png"
image bg cafe_evening = "images/bg/cafe_evening.png"
image bg outside_evening = "images/bg/outside_evening.png"
image bg festival = "images/bg/festival.png"

## Show grayed-out choices the player can't pick yet.
define config.menu_include_disabled = True

## Ending thresholds — tweak these to adjust routing.
define ENDING_FRIENDS_AFFECTION = 4
define ENDING_FRIENDS_WARMTH = 1
define ENDING_BOOK_AFFECTION = 4
