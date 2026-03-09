init python:

    def get_mood_text():
        warmth = store.personality_warmth
        curiosity = store.personality_curiosity
        sam_aff = store.sam_affection
        riley_aff = store.riley_affection

        if warmth >= 2 and curiosity >= 2:
            return (
                "You feel a pull toward the crowd — part warmth, part "
                "curiosity. You want to see everything and talk to everyone."
            )
        elif warmth >= 2:
            return (
                "There's something inviting about the noise and the laughter. "
                "You find yourself smiling before you've even said hello to anyone."
            )
        elif curiosity >= 2:
            return (
                "Your eyes jump from stall to stall — woodcarvings, jams, "
                "hand-knit scarves. You want to know the story behind each one."
            )
        elif sam_aff >= 3 or riley_aff >= 3:
            return (
                "You scan the crowd, looking for a familiar face. "
                "It's strange how quickly 'stranger' can become 'someone you're "
                "hoping to see.'"
            )
        else:
            return (
                "The festival is lively, but you hang back at the edges, "
                "taking it in from a comfortable distance."
            )


    def get_personality_reflection():
        warmth = store.personality_warmth
        curiosity = store.personality_curiosity
        sam_aff = store.sam_affection
        riley_aff = store.riley_affection
        helped = store.helped_sam
        book = store.shared_book_interest

        if warmth >= 2 and curiosity >= 2 and sam_aff >= 4 and riley_aff >= 4:
            return (
                "You've been in Pinewood for barely a day, but it feels like "
                "longer — the good kind of longer, where time stretches because "
                "you're paying attention. You helped where you could, asked "
                "questions when you were curious, and let two strangers become "
                "something more than that."
            )

        if warmth >= 2 and sam_aff >= 4:
            return (
                "You've always been the kind of person who reaches out first. "
                "Sam saw that right away — maybe because Sam is the same way. "
                "Some connections are instant like that."
            )

        if curiosity >= 2 and riley_aff >= 4:
            return (
                "There's a whole world underneath the surface of things — "
                "fungal networks, quiet people with deep thoughts, small towns "
                "with long memories. You're glad you looked closer."
            )

        if book and riley_aff >= 3:
            return (
                "You think about what Riley said — about trees choosing to "
                "cooperate, about things being connected underground where "
                "nobody can see. You wonder if people work the same way."
            )

        if helped and sam_aff >= 3:
            return (
                "There's something satisfying about having been useful. Carrying "
                "boxes, pouring cups — small things that added up to something "
                "that felt like belonging."
            )

        if curiosity >= 3:
            return (
                "Pinewood is full of small details — the grain of the wood "
                "on every stall, the way the light catches the mountains, "
                "the particular shade of amber in every turning leaf. You "
                "noticed all of it."
            )

        if warmth >= 3:
            return (
                "You smiled at strangers today. Most of them smiled back. "
                "That's not nothing — in fact, it might be everything."
            )

        return (
            "The festival is winding down. You stand at the edge of the "
            "crowd, hands in your pockets, watching the string lights "
            "flicker against the darkening sky."
        )


    def get_journal_entries():
        """Build journal entries from what the player has done so far."""
        entries = []

        if store.first_impression != "neutral" or store.drink_choice != "coffee":
            impression_text = {
                "friendly": "You told Sam you came to see the autumn leaves. A warm start.",
                "reserved": "You told Sam you needed somewhere quiet. Fair enough.",
                "curious": "You told Sam you were passing through. The sign worked.",
                "neutral": "You arrived in Pinewood on an autumn afternoon.",
            }
            entries.append({
                "title": "Arrived in Pinewood",
                "text": impression_text.get(store.first_impression, impression_text["neutral"]),
                "icon": "\u2302",
            })

        if store.drink_choice != "coffee" or store.first_impression != "neutral":
            drink_text = {
                "special": "Sam's spiced maple latte — homemade syrup from trees on the ridge.",
                "coffee": "A regular coffee. Strong and honest.",
                "tea": "A local tea blend. Earthy and faintly sweet.",
            }
            entries.append({
                "title": "First Drink at The Roost",
                "text": drink_text.get(store.drink_choice, "A warm drink."),
                "icon": "\u2615",
            })

        if store.helped_sam:
            entries.append({
                "title": "Helped Sam with Boxes",
                "text": "Spent ten minutes hauling coffee beans and ceramic mugs. "
                        "Sam called you their favorite customer.",
                "icon": "\u2661",
            })

        if store.asked_about_town:
            entries.append({
                "title": "Asked About Pinewood",
                "text": "About two hundred people. Mostly locals who never left, "
                        "plus a few who came and couldn't make themselves leave.",
                "icon": "\u263C",
            })

        if store.riley_affection >= 1:
            entries.append({
                "title": "Met Riley",
                "text": "Quiet, guarded, a book always in hand. "
                        "Sam said to give them time.",
                "icon": "\u2606",
            })

        if store.shared_book_interest:
            entries.append({
                "title": "The Wood Wide Web",
                "text": "Riley's eyes lit up when you mentioned mycorrhizal networks. "
                        "Trees sharing nutrients underground — the forest as one organism.",
                "icon": "\u2618",
            })

        if store.festival_volunteered:
            entries.append({
                "title": "Festival Volunteer",
                "text": "Helped Sam run the drink stall at the harvest festival. "
                        "Twice in two days.",
                "icon": "\u2605",
            })

        if store.festival_trail_promised:
            entries.append({
                "title": "Trail Promise",
                "text": "Riley offered to show you the old-growth forest trail. "
                        "Morning light through the canopy.",
                "icon": "\u2767",
            })

        if store.took_bird_guide:
            entries.append({
                "title": "The Bird Guide",
                "text": "A hand-illustrated field guide to local birds. "
                        "The artist has been drawing them for forty years.",
                "icon": "\u2708",
            })

        return entries


    # maps axis + value to a display label for the journal bars
    def get_personality_label(axis, value):
        if axis == "warmth":
            if value >= 3:
                return "Very Warm"
            elif value >= 1:
                return "Warm"
            elif value <= -1:
                return "Reserved"
            else:
                return "Neutral"
        elif axis == "curiosity":
            if value >= 3:
                return "Very Curious"
            elif value >= 1:
                return "Curious"
            elif value <= -1:
                return "Cautious"
            else:
                return "Neutral"
        return "Unknown"


    def get_relationship_label(value):
        if value >= 6:
            return "Close Friend"
        elif value >= 4:
            return "Good Connection"
        elif value >= 2:
            return "Friendly"
        elif value >= 1:
            return "Acquaintance"
        else:
            return "Stranger"
