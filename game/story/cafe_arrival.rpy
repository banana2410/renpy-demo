## Opening scene — player arrives in Pinewood and meets Sam.

label cafe_arrival:

    scene bg road_overlay with fade
    show screen leaf_overlay
    show screen location_label("Pinewood — Mountain Road")

    "The bus dropped you off at the edge of town twenty minutes ago."

    "Pinewood isn't much to look at from the road — a handful of rooftops
    tucked between pines, the mountains rising steeply behind them."

    "But the air is sharp and clean, and the leaves have turned every
    shade of amber. It's hard not to slow down and stare."

    "A wooden sign points you toward the town center. Below it,
    someone has taped a smaller note: {i}Hot drinks this way →{/i}"

    "You follow the arrow."

    jump meet_sam


label meet_sam:

    scene bg cafe_exterior with dissolve
    show screen location_label("The Roost — Exterior")

    "The café sits at the corner of the main street — a squat stone
    building with steam curling from a vent above the door."

    scene bg cafe_interior with dissolve
    hide screen leaf_overlay

    "A bell chimes as you step inside. Warm air and the smell of
    fresh coffee wrap around you."

    "Behind the counter, someone looks up from a stack of cups and
    breaks into a wide grin."

    s "Hey! New face in town — welcome to The Roost."

    s "I'm Sam. Owner, barista, and — on slow days — the entire
    wait staff."

    s "What brings you all the way up here?"

    menu:
        "I heard Pinewood was beautiful this time of year. Had to see it for myself.":
            $ personality_warmth += 1
            $ personality_curiosity += 1
            $ first_impression = "friendly"
            $ sam_affection += 1

            s "Ha! Well, you heard right. The valley gets like this
            for about three weeks every October — total magic."

            s "Glad someone's out there spreading the word."

        "Just needed to get away for a while. Somewhere quiet.":
            $ first_impression = "reserved"

            s "Yeah, I get that. Pinewood's good for quiet."

            s "No rush, no noise. Just the trees and the occasional
            very opinionated squirrel."

        "I'm passing through on a longer trip. Saw the sign outside.":
            $ personality_curiosity += 1
            $ first_impression = "curious"

            s "The sign works! I keep telling the town council
            that marketing matters."

            s "Well, passing through or not — you picked a good
            spot to stop."

    jump cafe_order


label cafe_order:

    s "So, what can I get you? The menu's up there, but honestly,
    I'd just ask me. I know what's good today."

    menu:
        "What do you recommend?":
            $ personality_curiosity += 1
            $ sam_affection += 1
            $ drink_choice = "special"

            s "Ooh, adventurous. I like that."

            s "Try the spiced maple latte. I make the syrup myself
            from trees up on the ridge."

            "Sam slides a warm mug across the counter. It smells
            like autumn distilled into liquid form."

        "Just a regular coffee, please.":
            $ drink_choice = "coffee"

            s "Classic. Nothing wrong with that."

            "Sam pours a cup from a pot that looks like it's been
            going since dawn. It's strong and honest."

        "Do you have tea?":
            $ drink_choice = "tea"

            s "Got a whole shelf of local blends. Pine needle,
            wildberry, chamomile — name your mood."

            "You pick one at random. It's earthy and faintly sweet."

    if first_impression == "friendly":
        s "First drink's on the house for anyone who says nice
        things about my town."
    elif first_impression == "curious":
        s "First one's a dollar. Traveler's discount."
    else:
        s "Take a seat wherever. No assigned seating — perk of
        being the only café in town."

    jump sam_conversation


label sam_conversation:

    scene bg cafe_counter with dissolve

    "You settle onto a stool at the counter. Sam leans against
    the back shelf, clearly happy for the company."

    s "So, you got questions about Pinewood? I'm basically the
    unofficial tourism department."

    jump sam_topics


label sam_topics:

    menu:

        set sam_topics_asked

        "What's the town like? Who lives here?":
            $ asked_about_town = True
            $ personality_curiosity += 1

            s "Small. Maybe two hundred people, give or take
            a few seasonal hikers."

            s "Mostly folks who grew up here and never left,
            plus a few like me who came from somewhere else
            and couldn't make ourselves leave."

            s "It's that kind of place."

            jump sam_topics

        "Need any help around the café? I've got time.":
            $ helped_sam = True
            $ personality_warmth += 1
            $ sam_affection += 2

            s "Wait, really? You just got here and you're
            already volunteering?"

            s "...Actually, yeah. If you could help me move
            those boxes from the back, that'd be amazing.
            My delivery guy has zero concept of 'stack neatly.'"

            "You spend ten minutes hauling boxes of coffee beans
            and ceramic mugs into the storeroom. Sam directs
            traffic with enthusiastic pointing."

            s "You're officially my favorite customer today.
            And I mean that — the bar is very low."

            jump sam_topics

        "This place has a nice feel to it. Been here long?":
            $ sam_affection += 1

            s "Four years now. Came up here on a hiking trip,
            found this building sitting empty, and thought —
            why not?"

            s "Took about a year to stop feeling like a tourist
            and start feeling like a local. Worth every awkward
            town meeting."

            jump sam_topics

        "I'm good for now. Let's move on.":
            pass

    $ sip_text = "maple latte" if drink_choice == "special" else drink_choice
    "You take a slow sip of your [sip_text]. Outside, the
    afternoon light is turning golden."

    "The bell above the door chimes again."

    # $ print("sam_affection:", sam_affection, "riley_affection:", riley_affection)

    jump riley_enters


label riley_enters:

    "A figure steps inside — bundled in a dark green coat, a tote
    bag stuffed with books slung over one shoulder."

    "They give Sam a small wave and head for a corner table without
    a word."

    s "That's Riley. Don't take the silence personally — they're
    like that with everyone at first."

    if helped_sam:
        s "But hey, you helped me with the boxes, so you've got
        good energy. Riley'll warm up to you."
    else:
        s "Give it time. Pinewood people are worth the wait."

    menu:
        "Go say hello to Riley.":
            $ personality_warmth += 1

            "You pick up your mug and walk over to the corner table."

            call riley_conversation from _call_riley_conversation

        "Stay at the counter. They seem like they want to be alone.":
            "You stay where you are. Some people need their space,
            and you can respect that."

    jump cafe_evening


label cafe_evening:

    scene bg cafe_evening with dissolve
    show screen location_label("The Roost — Evening")

    "The light outside has shifted from gold to deep orange.
    The café windows glow."

    if helped_sam:
        s "Hey — thanks again for the help earlier. Seriously."

    $ refill_text = "maple latte" if drink_choice == "special" else drink_choice
    s "Want a refill on that [refill_text] before I start closing up?"

    "You shake your head. It's getting late, and you should figure
    out where you're staying tonight."

    jump ending_route
