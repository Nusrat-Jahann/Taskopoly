CATEGORIES = {
    "Study": {
        "xp": 30,
        "keywords": [
            "math",
            "english",
            "science",
            "physics",
            "chemistry",
            "biology",
            "study",
            "homework",
            "assignment",
            "exam",
            "quiz",
            "class",
            "lesson",
            "revision",
            "read",
            "reading",
            "practice"
        ]
    },

    "Health": {
        "xp": 25,
        "keywords": [
            "exercise",
            "workout",
            "gym",
            "run",
            "running",
            "walk",
            "walking",
            "jog",
            "jogging",
            "stretch",
            "stretching",
            "sport",
            "sports"
        ]
    },

    "Chores": {
        "xp": 20,
        "keywords": [
            "clean",
            "cleaning",
            "room",
            "dishes",
            "dish",
            "laundry",
            "wash",
            "washing",
            "organize",
            "organizing",
            "sweep",
            "sweeping",
            "cook",
            "cooking"
        ]
    },

    "Creative": {
        "xp": 25,
        "keywords": [
            "draw",
            "drawing",
            "paint",
            "painting",
            "art",
            "design",
            "write",
            "writing",
            "music",
            "sing",
            "singing",
            "dance",
            "dancing",
            "craft"
        ]
    },

    "Self-care": {
        "xp": 10,
        "keywords": [
            "water",
            "drink",
            "brush",
            "teeth",
            "shower",
            "sleep",
            "breakfast",
            "lunch",
            "dinner",
            "rest"
        ]
    }
}


def detect_category_and_xp(quest_name):
    quest_name = quest_name.lower()

    best_category = "General"
    best_xp = 15
    highest_matches = 0

    for category, data in CATEGORIES.items():
        matches = 0

        for keyword in data["keywords"]:
            if keyword in quest_name:
                matches += 1

        if matches > highest_matches:
            highest_matches = matches
            best_category = category
            best_xp = data["xp"]

    return best_category, best_xp