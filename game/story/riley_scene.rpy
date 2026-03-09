label riley_conversation:

    scene bg cafe_corner with dissolve

    "Riley glances up as you approach. Their expression is guarded
    but not unfriendly — more like someone deciding whether to
    invest the energy."

    r "...Hi."

    "A pause. They close the book they were reading, keeping a
    finger between the pages."

    r "You're the one who came in on the bus?"

    if first_impression == "friendly":
        r "Sam seems to like you. That's... unusual. It usually
        takes a week."
        $ riley_affection += 1
    elif first_impression == "curious":
        r "Sam said you're traveling. That sounds nice."
    else:
        r "Pinewood doesn't get many visitors this late in the season."

    ## Some options only show up if you did specific things earlier.
    menu:
        "What are you reading?":
            $ personality_curiosity += 1
            $ riley_affection += 1

            "Riley lifts the book so you can see the cover. It's a
            worn paperback — something about forest ecology."

            r "It's about mycorrhizal networks. How trees share
            nutrients through fungal connections underground."

            r "Basically, the forest is one giant organism pretending
            to be a bunch of separate trees."

            menu:
                "That's fascinating. I've read about that — the 'wood wide web.'":
                    $ shared_book_interest = True
                    $ riley_affection += 2

                    "Riley's eyes light up — the first real spark of
                    animation you've seen from them."

                    r "You've heard of it? Most people glaze over
                    when I try to explain."

                    r "There's this one chapter about mother trees
                    that — sorry. I could talk about this for hours."

                    "You tell them you don't mind."

                "Sounds complicated. Is it good, though?":
                    $ riley_affection += 1

                    r "It's... yeah, it's good. Dense, but good."

                    r "I come here to read because the café's quiet
                    enough to focus but not so quiet that it's weird."

        "I helped Sam with some boxes earlier." if helped_sam:
            $ riley_affection += 1

            r "...You helped Sam? Voluntarily?"

            r "That's either very kind or very foolish. Sam's
            'small favor' has a way of turning into an afternoon."

            "A tiny smile. Progress."

        "Sam mentioned you're a regular here." if asked_about_town:
            $ riley_affection += 1

            r "Did they also mention I'm 'quiet but worth the wait'?
            Because that's Sam's line for everyone who doesn't
            immediately start chatting."

            "You can't help but smile."

            r "I'm here most afternoons. It's a good place to think."

        "Just wanted to say hi. I'll let you get back to your book.":
            r "...Thanks. For not making it weird."

            "Riley reopens their book. The conversation is over,
            but it doesn't feel like a rejection."

            return

    label .wind_down:

        "A comfortable silence settles between you. Riley takes a
        sip of whatever they're drinking — it looks like chamomile."

        if shared_book_interest:
            r "You know... if you're staying in town, there's a
            trail that goes through some old-growth forest up
            past the ridge."

            r "You can actually see the fungal networks if you
            know where to look. The fruiting bodies, at least."

            r "I could... show you. If you wanted."

            $ riley_affection += 1

        elif riley_affection >= 3:
            r "Pinewood's not bad once you get used to the pace.
            Everything moves a little slower up here."

            r "I mean that as a compliment."

        else:
            r "Well. It was... nice. Meeting you."

            "The words sound slightly rehearsed, but sincere."

        return
