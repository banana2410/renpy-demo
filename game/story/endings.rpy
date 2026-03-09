# priority: both high + warm → festival, riley bond → book, else quiet start
label ending_route:

    if sam_affection >= ENDING_FRIENDS_AFFECTION and riley_affection >= ENDING_FRIENDS_AFFECTION and personality_warmth >= ENDING_FRIENDS_WARMTH:
        jump ending_new_friends

    elif riley_affection >= ENDING_BOOK_AFFECTION and shared_book_interest:
        jump ending_book_exchange

    else:
        jump ending_quiet_start


label ending_new_friends:

    s "Hey, wait — before you go."

    "Sam ducks behind the counter and comes back with a small
    flyer, hand-drawn in colored marker."

    s "There's a harvest festival this weekend. The whole town
    comes out — lanterns, food, terrible karaoke."

    if helped_sam:
        s "And after you helped me today, you've basically earned
        honorary Pinewood citizenship."

    s "You should come. Both of you."

    "Sam glances at Riley. Riley looks down at their book,
    then back at you."

    r "...It's not terrible. The festival, I mean."

    r "The karaoke is exactly as bad as Sam says. But the
    food is good."

    "You look at the flyer. A hand-drawn pine tree wearing
    a party hat stares back at you."

    "You tell them you'll think about it. But you're already
    smiling."

    scene bg outside_evening with dissolve
    show screen leaf_overlay

    "As you step outside, the mountain air hits you — cold
    and clean and full of pine. The kind of air that makes
    you want to take a deep breath and hold it."

    "Pinewood might be worth more than a quick stop."

    hide screen leaf_overlay
    scene black with fade

    "You find a room at the inn. The bed is narrow but the
    quilt is thick, and you fall asleep to the sound of wind
    in the pines."

    jump festival_morning


label ending_book_exchange:

    "As you stand to leave, Riley catches your arm — then
    immediately lets go, looking embarrassed."

    r "Sorry. I just — here."

    "They pull the forest ecology book from their bag and
    hold it out."

    r "If you're going to be on the road, it's a good one
    for bus rides. The chapter on mother trees is around
    page two hundred."

    "You take the book. It's warm from being in their bag,
    the spine cracked from rereading."

    menu:
        "I'll take care of it. How do I return it?":
            $ riley_affection += 1

            r "You could... come back through Pinewood."

            r "I'm here most afternoons."

            "A pause."

            r "The café, I mean. Not — standing here holding
            books out at strangers."

        "Are you sure? This looks well-loved.":
            r "That's why I want someone else to read it."

            r "Books aren't meant to stay on one shelf forever."

    s "Look at that. Riley made a friend."

    r "Sam."

    s "I'm just saying!"

    scene bg outside_evening with dissolve
    show screen leaf_overlay

    "You step outside with the book tucked under your arm.
    The weight of it feels like a small promise."

    hide screen leaf_overlay
    scene black with fade

    "{b}Ending: The Book Exchange{/b}"

    return


label ending_quiet_start:

    "You set your empty mug on the counter."

    s "Heading out?"

    "You nod. It's getting dark, and you should find somewhere
    to stay tonight."

    if sam_affection >= 2:
        s "Well, it was good meeting you. If you're ever back this
        way, The Roost is always open."

        s "And I mean that. Small towns remember the good ones."

    else:
        s "Safe travels. Hope you find what you're looking for."

    if riley_affection >= 2:
        "From the corner table, Riley gives you a small nod.
        Not quite a wave, but close."
    elif riley_affection >= 1:
        "You think you see Riley glance up from their book
        as you pass. Maybe."

    scene bg outside_evening with dissolve
    show screen leaf_overlay

    "The bell chimes one last time as you step outside."

    "The street is quiet. The mountains are turning blue
    in the fading light, and somewhere nearby, a woodpecker
    is hammering at a dead pine."

    "Pinewood feels like a place you passed through once
    and might remember fondly on some future afternoon."

    "That's enough. Not every place needs to be a destination."

    hide screen leaf_overlay
    scene black with fade

    "{b}Ending: A Quiet Start{/b}"

    return
