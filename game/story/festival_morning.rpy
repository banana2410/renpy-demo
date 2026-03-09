# act 2 — festival
label festival_morning:

    scene bg festival with fade
    show screen leaf_overlay
    show screen location_label("Pinewood — Harvest Festival")

    "You didn't plan to stay the night, but the one inn in town
    had a room and the mountain air made it hard to leave."

    "The festival has taken over the main street — wooden stalls,
    string lights, the smell of cinnamon and woodsmoke."

    $ mood = get_mood_text()
    "[mood]"

    jump festival_sam_encounter


label festival_sam_encounter:

    "You spot Sam behind a stall, pouring drinks from a massive
    thermos into paper cups."

    if drink_choice == "special":
        s "Hey, you came back! Want another maple latte? I brought
        the good syrup."
    elif drink_choice == "tea":
        s "The tea person returns! I've got a festival blend today —
        pine needle and orange peel."
    else:
        s "Coffee! I remember. Got a fresh batch going — festival
        strength. Fair warning."

    if helped_sam:
        s "And hey — I set up this whole stall by myself this
        morning. Thought of you when I was hauling boxes."

        s "...That was a joke. I absolutely guilt-tripped two
        neighbors into helping."

    if first_impression == "friendly":
        s "Grab a cup, mingle, enjoy. You already feel like
        a local to me."
        $ sam_affection += 1
    elif first_impression == "curious":
        s "There's a lot to see. The woodcarving demos are
        weirdly hypnotic."
    else:
        s "Take your time. No pressure to be social — half
        the town is just here for the food."

    jump festival_topics


## Looping topic menu — tracks what's been asked so options
## don't repeat. Player picks until they choose to move on.

label festival_topics:

    menu (festival_topics_asked):

        set festival_topics_asked

        "Who's performing on that little stage?":
            $ personality_curiosity += 1

            s "Local talent night. We've got a fiddle player, a
            poet, and someone who does birdcalls."

            s "The birdcall guy is... surprisingly good, actually.
            Got a standing ovation last year."

            if personality_curiosity >= 3:
                "You make a mental note to check out every act.
                Something about this town keeps pulling at your
                attention."
            else:
                "You nod politely."

            jump festival_topics

        "Is Riley here somewhere?":
            if riley_affection >= 3:
                s "Yeah! They're over by the book swap stall.
                Shocking, I know."

                s "They actually asked if you were coming today.
                Which, for Riley, is basically rolling out a
                red carpet."
                $ riley_affection += 1
            elif riley_affection >= 1:
                s "Somewhere around, yeah. Probably near the
                quietest corner they can find."
            else:
                s "I think so? Riley's not really a festival
                person, but they show up for an hour or two."

            jump festival_topics

        "Can I help with anything?" if not festival_volunteered:
            $ festival_volunteered = True
            $ personality_warmth += 1
            $ sam_affection += 2

            s "Twice in two days? You're going to put the
            neighbors to shame."

            if helped_sam:
                s "At this rate I'm going to have to put you
                on the payroll. Or at least the free coffee list."

                "You spend fifteen minutes helping Sam restock
                cups and napkins. It feels oddly comfortable —
                like a routine you've done a hundred times."
            else:
                s "Sure — if you could hand out cups while I
                pour, that'd be a huge help."

                "You fall into a rhythm with Sam. Pour, hand,
                smile, repeat. It's meditative."

            $ sam_affection += 1

            jump festival_topics

        "Tell me about the history of this festival.":
            $ personality_curiosity += 1

            s "It started about twenty years ago when the town
            needed something to do in October besides watch
            leaves fall."

            s "Now it's the one weekend a year where every
            single person in Pinewood is outside at the same
            time. Even the hermits."

            if asked_about_town:
                "You remember what Sam said yesterday about the
                two hundred residents. Looking around, that
                number feels about right."

            jump festival_topics

        "I'm going to look around. Thanks, Sam.":
            pass

    if riley_affection >= 2:
        jump festival_riley_encounter
    else:
        jump festival_solo_walk


label festival_riley_encounter:

    "You find Riley exactly where Sam said — standing in front
    of a folding table covered in paperbacks."

    ## Greeting depends on which flags are set from yesterday.
    if shared_book_interest and helped_sam:
        r "Oh — you're here. I was hoping... I mean. Hi."

        r "I found something at the book swap I think you'd
        like. About mycorrhizal networks in old-growth forests."

        $ riley_affection += 2

    elif shared_book_interest:
        r "Hey. I saw this and thought of our conversation
        yesterday."

        "Riley holds up a field guide to local fungi."

        $ riley_affection += 1

    elif helped_sam:
        r "Sam said you helped set up the stall. That's...
        nice of you."

        r "I don't usually come to these things, but the
        book swap table is worth it."

        $ riley_affection += 1

    else:
        r "Oh. Hi again."

        "Riley gives you a small nod and goes back to
        browsing the books."

    ## Nested conversation — goes up to 3 levels deep.
    menu:
        "Tell me more about the book you found." if shared_book_interest:
            $ riley_affection += 1

            r "It's a local author — someone who actually studied
            the forests around here for thirty years."

            r "There's a chapter on how the oldest trees send
            nutrients to saplings through the fungal network.
            Like... parenting, but underground."

            menu:
                "That's beautiful. Trees taking care of each other.":
                    $ personality_warmth += 1
                    $ riley_affection += 1

                    r "Right? It makes the whole forest feel...
                    intentional. Like it's choosing to cooperate."

                    menu:
                        "Do you think people could learn from that?":
                            $ riley_affection += 1

                            "Riley is quiet for a moment. When they
                            speak, their voice is softer."

                            r "I think some people already do. Small
                            towns like this — everyone's connected
                            whether they want to be or not."

                            r "The trick is wanting to be."

                        "I'd love to see those forests with you sometime.":
                            $ riley_affection += 2
                            $ festival_trail_promised = True

                            "Riley's cheeks flush — just slightly,
                            but enough to notice."

                            r "I... yeah. I'd like that. The trail
                            starts about a mile past the inn."

                            r "Morning is best. The light through
                            the canopy is worth waking up early for."

                "Is that why you like Pinewood? The forests?":
                    $ personality_curiosity += 1
                    $ riley_affection += 1

                    r "Partly. It's also that nobody here pretends
                    to be something they're not."

                    r "The trees don't, the people don't. Everything
                    is just... what it is."

                    if first_impression == "reserved":
                        r "You seem like that too, actually. What
                        you see is what you get."

        "What's the best find at the book swap?" if not shared_book_interest:
            $ personality_curiosity += 1

            r "Depends what you're into. There's a decent mystery
            novel, a cookbook that's mostly pie recipes, and..."

            "Riley pauses, considering."

            r "...a field guide to local birds. It has hand-drawn
            illustrations. Really lovely."

            menu:
                "The bird guide sounds nice. I like hand-drawn things.":
                    $ riley_affection += 1
                    $ took_bird_guide = True

                    r "Good choice."

                    "Riley hands you the guide. Your fingers brush
                    as you take it."

                    r "The artist lives two valleys over. She's
                    been drawing birds for forty years."

                "I'll take the pie cookbook. Priorities.":
                    $ personality_warmth += 1

                    "Riley almost smiles."

                    r "Understandable. The apple crumble recipe on
                    page twelve is legitimately life-changing."

        "How are you finding the festival?":
            if riley_affection >= 5:
                r "Better than usual, actually."

                "A pause."

                r "I think that might be your fault."

                $ riley_affection += 1
            elif riley_affection >= 3:
                r "It's... fine. Louder than I'd like, but the
                book swap makes up for it."
            else:
                r "Crowded."

                "A one-word answer. Classic Riley."

        "I should keep exploring. See you around.":
            r "Sure. Enjoy the festival."

            if riley_affection >= 4:
                "You turn to leave. After a few steps—"

                r "Hey."

                "You look back."

                r "I'm glad you stayed."

            jump festival_solo_walk

    jump festival_wrapup


label festival_solo_walk:

    "You wander through the festival alone. It's not lonely —
    it's the comfortable kind of solitude where you're choosing
    to be with your own thoughts."

    if personality_warmth >= 2:
        "You stop to help an older woman carry a box of apples
        to her car. She insists on giving you three."

        $ personality_warmth += 1

    elif personality_curiosity >= 2:
        "You spend ten minutes watching the woodcarver shape a
        block of pine into a small owl. She doesn't seem to
        mind the audience."

        $ personality_curiosity += 1

    else:
        "You buy a cup of cider and lean against a fence post,
        watching the town move around you."

    # TODO: maybe add more solo activities here

    jump festival_wrapup


label festival_wrapup:

    scene bg festival with dissolve

    "The afternoon light slants through the pines, turning the
    festival stalls into something out of a painting."

    $ reflection = get_personality_reflection()
    "[reflection]"

    ## Sam's farewell
    if sam_affection >= 6:
        s "Hey — I meant what I said. You've got a standing
        invitation at The Roost. Any time."

        s "And I'm not just saying that because you helped
        me carry things."

    elif sam_affection >= 3:
        s "It was really good meeting you. Pinewood could
        use more people like you passing through."

    else:
        "You wave to Sam from across the stalls. Sam waves
        back — a quick, warm gesture."

    ## Riley's farewell — most conditional-heavy part
    if riley_affection >= 6 and shared_book_interest and festival_trail_promised:
        r "So... tomorrow morning? The trailhead is past the
        inn, about a ten-minute walk."

        r "I'll bring the field guide. And coffee. Sam's
        recipe."

        "Something about the way Riley says it makes tomorrow
        feel like a certainty rather than a question."

    elif riley_affection >= 5 and shared_book_interest:
        r "If you're ever back in Pinewood... the trail offer
        still stands."

        r "The forests don't go anywhere. Neither do I."

    elif riley_affection >= 4:
        "Riley catches your eye across the crowd and raises
        a hand — palm out, fingers slightly curled. Not quite
        a wave, but more than a nod."

        "It feels like an invitation to come back."

    elif riley_affection >= 2:
        "You think you spot Riley leaving the festival, a stack
        of books under one arm. They don't look back."

        "But they're smiling."

    ## Final ending card
    hide screen leaf_overlay
    scene black with fade

    if sam_affection >= 5 and riley_affection >= 5:
        "{b}Ending: Roots{/b}"
        "Some places hold onto you. Pinewood wrapped its roots
        around your ankles while you weren't looking — and you
        don't mind at all."

    elif riley_affection >= 5:
        "{b}Ending: The Trail{/b}"
        "Tomorrow, you'll walk into the forest with someone who
        sees the world differently than anyone you've met. That
        feels like enough of a reason to stay."

    elif sam_affection >= 5:
        "{b}Ending: The Regular{/b}"
        "You've been here two days and you already have a usual
        order. Some people take years to find their café. You
        found yours by accident."

    elif personality_curiosity >= 4:
        "{b}Ending: The Wanderer{/b}"
        "Pinewood was a good stop — one of many. The road goes
        on, and so do you, carrying a few warm memories and
        the taste of mountain air."

    else:
        "{b}Ending: October{/b}"
        "You came to Pinewood and you left again. That's not
        a failure — it's just October, doing what October does."

    ## Returns to main menu (reached via jump, not call)
    return
