from drafter import *
from dataclasses import dataclass
from bakery import assert_equal

set_website_title("Game Matchmaker")
set_site_information(
    author="Grace Colvin",
    description="Take a short quiz and recive a game recommendation from my personal library.",
    sources="Thanks to the Drafter docs and Claude.",
    planning=["plan.pdf", "design.pdf"],
    links=[]
)
hide_debug_information()
set_website_framed(False)


# ---------------------------------------------------------------
# DATACLASSES
# ---------------------------------------------------------------
@dataclass
class Game:
    """what makes up each game in my library."""
    title: str
    genres: list[str]    
    platform: str
    difficulty: int      # 1 = Easy, 2 = Medium, 3 = Hard
    multiplayer: bool
    length: str
    description: str
    notes: str         


@dataclass
class Preferences:
    """What the user told the quiz they like."""
    genre: str
    platform: str
    difficulty: int
    multiplayer: bool


@dataclass
class State:
    """Everything the website remembers between pages."""
    username: str
    games: list[Game]
    preferences: Preferences
    recommendations: list[Game]   
    favorites: list[Game]
    selected_game: Game


# ---------------------------------------------------------------
# GLOBAL CONSTANTS
# ---------------------------------------------------------------
GAMES = [
    Game("Minecraft", ["sandbox", "survival", "open world"], "PC", 1, True,
         "Endless",
         "Explore a randomly generated world made of blocks, mine resources, and craft tools "
         "to build anything you can imagine. You can play peacefully and just build, or "
         "survive the night against monsters, solo or with friends.",
         "Minecraft never gets old. Its sandbox style makes it enjoyable for players of all ages. "
         "It is great with friends or solo, with creative building, grinding, and both PvP and PvE options."),
    Game("Red Dead Redemption 2", ["open world", "action", "adventure"], "PlayStation", 2, False,
         "50-60 hours",
         "Live as outlaw Arthur Morgan in a dying Wild West, riding across huge landscapes "
         "and completing story missions with the Van der Linde gang. The world is packed "
         "with detail, side stories, hunting, and random encounters.",
         "My favorite game of all time. The story is fantastic, and the world itself is beautiful. "
         "You can follow the main missions or spend hours exploring, enjoying the scenery, and meeting strangers."),
    Game("Cyberpunk 2077", ["open world", "rpg", "action"], "PC", 2, False,
         "30-60 hours",
         "Play as V, a mercenary in the neon-lit Night City, where your choices and "
         "upgrades change how missions play out. Mix gunplay, hacking, and stealth in a "
         "story-driven sci-fi world.",
         "A visually impressive game with unique gameplay and lots of replay value. "
         "The different builds and skill trees make each playthrough feel fresh."),
    Game("Grand Theft Auto V", ["open world", "action", "adventure"], "PlayStation", 2, True,
         "30 hours",
         "Switch between three criminals in the sprawling city of Los Santos, pulling off "
         "heists and causing chaos. GTA Online adds a huge multiplayer world to play with "
         "friends.",
         "The story mode is great for players who enjoy planning, problem-solving, action, and character development. "
         "GTA Online is especially fun with friends as you work together to earn money and complete activities."),
    Game("Hollow Knight", ["platformer", "action", "adventure"], "Switch", 3, False,
         "30-40 hours",
         "Explore the vast, hand-drawn underground kingdom of Hallownest as a tiny silent "
         "knight. Tough boss fights and tricky platforming reward careful, patient play.",
         "The art and music are excellent. The gameplay is challenging, but learning from each attempt is rewarding and addictive."),
    Game("Hollow Knight: Silksong", ["platformer", "action", "adventure"], "Switch", 3, False,
         "30+ hours",
         "Play as Hornet in the new kingdom of Pharloom, with faster movement and a bigger "
         "variety of tools than the first game. Expect tough bosses and a map full of "
         "secrets to uncover.",
         "A harder follow-up to the original, but just as fun. It has great music and gameplay, along with an engaging story."),
    Game("Raft", ["survival", "sandbox", "adventure"], "PC", 2, True,
         "20-30 hours",
         "Stranded on a tiny raft in the middle of the ocean, you collect floating debris to "
         "expand your raft while fending off sharks and finding food and water. Co-op makes "
         "the survival much more fun and a little more chaotic.",
         "A classic game to play with friends. Working together can be fun, but the chaos can also test your friendships."),
    Game("Stardew Valley", ["simulation", "rpg"], "PC", 1, True,
         "50+ hours",
         "Inherit your grandfather's run-down farm, grow crops, raise animals, and get to "
         "know the townspeople. It's a relaxed game with no pressure, and up to four "
         "players can farm together.",
         "Cute and cozy on the surface, but much more detailed than it first appears. There is something here for many types of players."),
    Game("Slime Rancher", ["simulation", "adventure"], "PC", 1, False,
         "15-25 hours",
         "Run a ranch on a faraway planet by collecting colorful slimes, feeding them, and "
         "selling their products to unlock new areas. It's a bright, cheerful game about "
         "exploring and managing your ranch.",
         "A feel-good farming game that is cute, relaxing, and fun to explore."),
    Game("The Legend of Zelda: Breath of the Wild", ["open world", "adventure", "action"],
         "Switch", 2, False,
         "50+ hours",
         "Wake up as Link in a ruined Hyrule and explore a huge open world however you want. "
         "Solve puzzles in shrines, cook meals, and take on Calamity Ganon whenever "
         "you feel ready.",
         "A great introduction to open-world games. The world is beautiful, and exploring it is a lot of fun."),
    Game("Crime Scene Cleaner", ["simulation", "puzzle"], "PC", 1, False,
         "5-10 hours",
         "Take on the job of a crime scene cleaner and scrub, mop, and dispose of evidence "
         "in a first-person simulation. It's a quirky, relaxing game with a dark sense "
         "of humor.",
         "A very unusual game, but surprisingly satisfying in its own strange way."),
    Game("The Sims", ["simulation", "sandbox"], "PC", 1, False,
         "Endless",
         "Create your own characters, build them a home, and guide their careers, "
         "relationships, and daily lives. You set the goals, so every household ends up "
         "with its own funny or dramatic story.",
         "A classic that can be played differently every time. It is fun to create characters and guide their lives."),
    Game("Portal and Portal 2", ["puzzle", "adventure"], "PC", 2, True,
         "10-15 hours",
         "Use a portal gun to create linked doorways and solve physics-based puzzles in a "
         "testing facility run by the sarcastic AI GLaDOS. Portal 2 adds a full two-player "
         "co-op campaign.",
         "A really fun puzzle game, whether you play on your own or work through the co-op puzzles with a friend."),
    Game("Mario Kart 8 Deluxe", ["racing", "party"], "Switch", 1, True,
         "Endless",
         "Race colorful tracks with items, drifts, and shortcuts, either alone or against "
         "up to seven other players. Easy to pick up for beginners, with plenty of "
         "skill for experts.",
         "A classic party game where having fun with friends is just as important as the competition."),
    Game("Super Smash Bros. Ultimate", ["fighting", "party", "action"], "Switch", 2, True,
         "Endless",
         "Pit Nintendo characters against each other in fast arena brawls where the goal is "
         "to knock opponents off the stage. It has a huge roster and works great as a "
         "party game.",
         "One of the most competitive games on this list, but its large roster and variety of characters can help less experienced players keep things interesting."),
    Game("Cuphead", ["platformer", "shooter", "action"], "Switch", 3, True,
         "5-8 hours",
         "Run and gun through hand-drawn 1930s cartoon levels and a long series of "
         "difficult boss fights. You'll die often, but each attempt teaches you the "
         "pattern, and a friend can join in co-op.",
         "Very unique and difficult, but still incredibly fun once you get the hang of it."),
    Game("Undertale", ["rpg", "adventure"], "PC", 1, False,
         "6-10 hours",
         "Fall into the underground world of monsters in an RPG where you can choose to "
         "fight or spare every enemy. Your choices change the story, and it has a "
         "memorable soundtrack and lots of humor.",
         "The music always gets stuck in my head in the best way. It has a great story and many different ways to play."),
    Game("Halo: The Master Chief Collection", ["shooter", "action"], "Xbox", 2, True,
         "40+ hours",
         "Play through the campaigns of several Halo games as Master Chief, fighting the "
         "Covenant in a sci-fi universe. The collection also includes classic "
         "multiplayer modes to play with friends.",
         "A classic that never gets old. It is a straightforward, old-school shooter that is fun to revisit."),
    Game("Counter-Strike: Global Offensive", ["shooter", "action"], "PC", 3, True,
         "Endless",
         "Join a team of terrorists or counter-terrorists in tense, round-based matches "
         "where one mistake can cost you the round. Success depends on aim, game "
         "knowledge, and teamwork.",
         "Great to play with friends, with plenty of opportunities for competition and ranked play."),
    Game("Valorant", ["shooter", "action"], "PC", 3, True,
         "Endless",
         "A 5-versus-5 tactical shooter where each agent has special abilities on top of "
         "precise gunplay. Teams take turns attacking and defending sites, so "
         "communication and strategy matter.",
         "Very fun with friends, especially if you enjoy teamwork, competition, and ranked play."),
]

VALID_GENRES = ["action", "adventure", "simulation", "racing", "shooter", "sandbox",
                "open world", "platformer", "puzzle", "fighting", "rpg", "survival", "party"]
VALID_PLATFORMS = ["PC", "PlayStation", "Xbox", "Switch"]
DIFFICULTY_OPTIONS = ["1 - Easy", "2 - Medium", "3 - Hard"]


# ---------------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------------
def difficulty_name(number: int) -> str:
    """takes in an int and returns a string :Turns a difficulty number (1, 2, or 3) into a readable label."""
    if number == 1:
        return "Easy"
    elif number == 2:
        return "Medium"
    return "Hard"






def calculate_score(game: Game, prefs: Preferences) -> int:
    """takes in a Game and Preferences and returns an int
        Adds one point for each preference (genre, platform, difficulty, multiplayer) matched."""
    score = 0
    # "x in list" checks every genre of the game, so a game with several
    # genres earns the point if ANY of them matches the user's genre.
    if prefs.genre.lower() in game.genres:
        score += 1
    if game.platform == prefs.platform:
        score += 1
    if game.difficulty == prefs.difficulty:
        score += 1
    if game.multiplayer == prefs.multiplayer:
        score += 1
    return score



def find_top_games(games: list[Game], prefs: Preferences) -> list[Game]:
    """takes in a list of games and the preferences and returns a list of games:
    Returns the three games with the highest match scores."""
    remaining_games = games[:]
    top_games = []

    for i in range(3):
        if len(remaining_games) == 0:
            break

        best_game = remaining_games[0]
        best_score = calculate_score(best_game, prefs)

        for game in remaining_games:
            score = calculate_score(game, prefs)
            if score > best_score:
                best_score = score
                best_game = game

        top_games.append(best_game)
        remaining_games.remove(best_game)

    return top_games



def parse_genres(text: str) -> list[str]:
    """takes in a string and returns a list of strings
        Splits comma-separated text into genres; returns [] if none are given or any is invalid."""
    genres = []
    for piece in text.split(","):      
        genre = piece.strip().lower()
        if genre not in VALID_GENRES:
            return []
        genres.append(genre)
    return genres



def game_buttons(games: list[Game]) -> list:
    """takes in a list of games and returns a list: Makes one 'see more info' button (plus a line break) for each game."""
    buttons = []
    for game in games:
        # Argument(name, value): sends the game's title to game_details_page
        buttons.append(Button(game.title, game_details_page,
                              [Argument("title", game.title)]))
        buttons.append(LineBreak())
    return buttons






# ---------------------------------------------------------------
# ROUTES: HOME AND USERNAME
# ---------------------------------------------------------------
@route
def index(state: State) -> Page:
    """takes in State and returns a Page: Starting route that Drafter loads first; shows the home page."""
    return home_page(state)


@route
def home_page(state: State) -> Page:
    """takes in State and returns a Page: Shows the site name, description, name box, and buttons to the other pages."""
    greeting = "Welcome!"
    if state.username != "":
        greeting = f"Welcome back, {state.username}!"
    return Page(state, [
        Header("Game Matchmaker"),
        greeting,
        LineBreak(),
        "Find your next favorite game! Take a short quiz about what you like, "
        "and I'll recommend a game from my personal library of favorites.",
        LineBreak(),
        "Your name: ",
        TextBox("username", state.username),
        Button("Save Name", save_username),
        LineBreak(),
        Button("Start the Quiz", quiz_page),
        Button("See All Games", game_library_page),
        Button("My Favorites", favorites_page),
        Button("Past Recommendations", history_page),
        Button("Add a Game", add_game_page),
    ])




@route
def save_username(state: State, username: str) -> Page:
    """takes in a State and a str and returns a Page: Saves the user's name (without extra spaces) in the state and returns home."""
    state.username = username.strip()
    return home_page(state)



@route
def back_to_home(state: State) -> Page:
    """takes in a state and returns a Page: Returns the user to the home page without changing anything."""
    return home_page(state)



# ---------------------------------------------------------------
# ROUTES: QUIZ, HELP, RECOMMENDATIONS
# ---------------------------------------------------------------
@route
def quiz_page(state: State, error: str = "") -> Page:
    """takes in a state and a string and returns a Page: Shows the quiz inputs; displays an error message if one is given."""
    # Default parameter (error: str = ""): lets other routes call this page
    # with an error message, while the button can call it with no error at all.
    content = [Header("Find Your Game")]
    if error != "":
        content.append("ERROR: " + error)
        content.append(LineBreak())
    content += [
        "Favorite genre: ",
        TextBox("genre", ""),
        LineBreak(),
        "Platform: ",
        SelectBox("platform", VALID_PLATFORMS, "PC"),
        LineBreak(),
        "Difficulty: ",
        SelectBox("difficulty", DIFFICULTY_OPTIONS, "1 - Easy"),
        LineBreak(),
        "Style: ",
        CheckBox("multiplayer", False),
        " Multiplayer game",
        LineBreak(),
        Button("Submit", submit_quiz),
        Button("Help (accepted answers)", help_page),
    ]
    return Page(state, content)






@route
def help_page(state: State) -> Page:
    """takes in a State and returns a page: Lists the accepted answers for every quiz question."""
    # ", ".join(list): glues the items of a list into one string separated by ", "
    return Page(state, [
        Header("Help: Accepted Answers"),
        Header("Genre (type one of these):", 3),
        ", ".join(VALID_GENRES),
        Header("Platform (choose from the box):", 3),
        ", ".join(VALID_PLATFORMS),
        Header("Difficulty (choose from the box):", 3),
        ", ".join(DIFFICULTY_OPTIONS),
        Header("Style:", 3),
        "Check the box if you want a multiplayer game, leave it unchecked for single-player.",
        LineBreak(),
        Button("Back to Quiz", quiz_page),
        Button("Return Home", back_to_home),
    ])






@route
def submit_quiz(state: State, genre: str, platform: str,
                difficulty: str, multiplayer: bool) -> Page:
    """takes in a state, strings, and a bool and returns a page
    Validates the answers, saves the preferences, and saves the best-matching game."""
    genre = genre.strip().lower()

    # Error check: the genre must be an available option
    if genre not in VALID_GENRES:
        return quiz_page(state, "Sorry, that genre isn't available. "
                                "Please try a different answer (see Help for options).")

    # difficulty[0]: the SelectBox gives text like "2 - Medium", so index 0
    # is the first character ("2"), which int() turns into a number.
    difficulty_number = int(difficulty[0])
    state.preferences = Preferences(genre, platform, difficulty_number, multiplayer)

    top_games = find_top_games(state.games, state.preferences)
    for game in top_games:
        state.recommendations.append(game)
    state.selected_game = top_games[0]
    return recommendations_page(state)






@route
def recommendations_page(state: State) -> Page:
    """takes in a State and returns a Page: Shows the top three recommended games and their match percentages."""

    top_games = state.recommendations[-3:]

    content = [
        Header("Your Top 3 Recommended Games"),
        "Based on your quiz answers, here are your best matches!",
        LineBreak()
    ]

    for i in range(len(top_games)):
        game = top_games[i]
        score = calculate_score(game, state.preferences)
        percent = int(score / 4 * 100)

        favorite_label = "Add to Favorites"
        if game in state.favorites:
            favorite_label = "Remove from Favorites"

        content += [
            Header(game.title, 2),
            "Match: " + str(percent) + "%",
            LineBreak(),
            Button("See Details", game_details_page,
                   [Argument("title", game.title)]),
            Button(favorite_label, toggle_favorite,
                   [Argument("title", game.title)]),
            LineBreak(),
        ]

    content += [
        Button("Try Quiz Again", quiz_page),
        Button("Past Recommendations", history_page),
        Button("Return Home", back_to_home),
    ]
    return Page(state, content)





# ---------------------------------------------------------------
# ROUTES: PAST RECOMMENDATIONS
# ---------------------------------------------------------------
@route
def history_page(state: State) -> Page:
    """takes in a State and returns a Page: Lists every game the site has recommended so far, newest first."""
    content = [Header("Past Recommendations")]
    if len(state.recommendations) == 0:
        content.append("No recommendations yet. Take the quiz to get one!")
        content.append(LineBreak())
    else:
        content.append("Newest first. Click a game to see more information:")
        content.append(LineBreak())
        # reversed(list): goes through the list backwards; list() turns it
        # back into a normal list so game_buttons can loop over it.
        content += game_buttons(list(reversed(state.recommendations)))
    content.append(Button("Take the Quiz", quiz_page))
    content.append(Button("Return Home", back_to_home))
    return Page(state, content)






# ---------------------------------------------------------------
# ROUTES: GAME LIBRARY, FILTER, DETAILS
# ---------------------------------------------------------------
@route
def game_library_page(state: State) -> Page:
    """takes in a State and returns a Page: Shows a genre filter and a button for every game in the library."""
    content = [
        Header("Game Library"),
        "Filter by genre: ",
        SelectBox("genre_filter", ["all"] + VALID_GENRES, "all"),
        Button("Filter", filter_games),
        LineBreak(),
        "Click a game to see more information:",
        LineBreak(),
    ]
    content += game_buttons(state.games)
    content.append(Button("Return Home", back_to_home))
    return Page(state, content)






@route
def filter_games(state: State, genre_filter: str) -> Page:
    """takes in a State and returns a Page: Shows only the games that have the chosen genre ('all' shows every game)."""
    if genre_filter == "all":
        shown = state.games
    else:
        shown = []
        for game in state.games:
            if genre_filter in game.genres:    # matches any of the game's genres
                shown.append(game)

    content = [
        Header(f"Game Library: {genre_filter}"),
        "Click a game to see more information:",
        LineBreak(),
    ]
    content += game_buttons(shown)
    content.append(Button("Back to Full Library", game_library_page))
    content.append(Button("Return Home", back_to_home))
    return Page(state, content)






@route
def game_details_page(state: State, title: str) -> Page:
    """takes in a State and returns a Page: Finds the game with the given title, saves it as selected, and shows all its details."""
    for game in state.games:
        if game.title == title:
            state.selected_game = game

    game = state.selected_game
    # Conditional expression: picks one of two strings based on a boolean.
    multiplayer_text = "Multiplayer" if game.multiplayer else "Single-player"
    genre_text = ", ".join(game.genres)

    return Page(state, [
        Header(game.title),
        f"Genres: {genre_text}", LineBreak(),
        f"Platform: {game.platform}", LineBreak(),
        f"Difficulty: {difficulty_name(game.difficulty)}", LineBreak(),
        f"Style: {multiplayer_text}", LineBreak(),
        f"Length: {game.length}", LineBreak(),
        f"Description: {game.description}", LineBreak(),
        f"Developer's notes: {game.notes}", LineBreak(),
        Button("Return Home", back_to_home),
    ])






# ---------------------------------------------------------------
# ROUTES: FAVORITES
# ---------------------------------------------------------------
@route
def toggle_favorite(state: State, title: str) -> Page:
    """takes in a Stateabd a string and returns a Page:Adds the game to the favorites if it isn't there, or removes it if it is."""
    for game in state.games:
        if game.title == title:
            if game in state.favorites:
                state.favorites.remove(game)
            else:
                state.favorites.append(game)
    return recommendations_page(state)






@route
def favorites_page(state: State) -> Page:
    """takes in a State and returns a Page: Shows a button for each favorite game, or a message if there are none."""
    content = [Header("My Favorites")]
    if len(state.favorites) == 0:
        content.append("You haven't saved any favorites yet.")
        content.append(LineBreak())
    content += game_buttons(state.favorites)
    content.append(Button("Return Home", back_to_home))
    return Page(state, content)






# ---------------------------------------------------------------
# ROUTES: GAME SUBMISSION
# ---------------------------------------------------------------
@route
def add_game_page(state: State, error: str = "") -> Page:
    """takes in a State and a str and returns a Page:
    Shows the form for adding a new game; displays an error message if one is given."""
    # Default parameter (error: str = ""): same idea as quiz_page.
    content = [Header("Add a Game")]
    if error != "":
        content += ["ERROR: " + error, LineBreak()]
    content += [
        "Title: ", TextBox("title", ""), LineBreak(),
        "Genres (separate with commas): ", TextBox("genre", ""), LineBreak(),
        "Platform: ", SelectBox("platform", VALID_PLATFORMS, "PC"), LineBreak(),
        "Difficulty: ", SelectBox("difficulty", DIFFICULTY_OPTIONS, "1 - Easy"), LineBreak(),
        "Multiplayer: ", CheckBox("multiplayer", False), LineBreak(),
        "Length: ", TextBox("length", ""), LineBreak(),
        "Description: ", TextBox("description", ""), LineBreak(),
        "Notes: ", TextBox("notes", ""), LineBreak(),
        Button("Add Game", submit_game),
        Button("Return Home", back_to_home),
    ]
    return Page(state, content)



@route
def submit_game(state: State, title: str, genre: str, platform: str,
                difficulty: str, multiplayer: bool, length: str,
                description: str, notes: str) -> Page:
    """takes in a State, strings, and a bool and returns a page:
    Checks the new game's answers and, if valid, adds it to the game library."""
    genres = parse_genres(genre)
    title = title.strip()
    if title == "":
        return add_game_page(state, "Please enter a title.")
    if len(genres) == 0:
        return add_game_page(state, "Those genres aren't available. Please try different ones.")
    for game in state.games:
        if game.title.lower() == title.lower():
            return add_game_page(state, "That game is already in the library.")

    # difficulty[0]: first character of text like "2 - Medium", turned into a number
    state.games.append(Game(title, genres, platform, int(difficulty[0]),
                            multiplayer, length, description, notes))
    return game_library_page(state)




# ---------------------------------------------------------------
# UNIT TESTS FOR ROUTES
# These are kept together because pages refer to routes defined later.
# ---------------------------------------------------------------

test_state = State("", list(GAMES), Preferences("", "PC", 1, False), [], [], GAMES[0])

# Home and username
assert_equal(isinstance(index(test_state), Page), True)
assert_equal(isinstance(home_page(test_state), Page), True)
save_username(test_state, "  Sam  ")
assert_equal(test_state.username, "Sam")
back_to_home(test_state)

# Quiz and help pages
assert_equal(isinstance(quiz_page(test_state), Page), True)
assert_equal(isinstance(help_page(test_state), Page), True)
assert_equal(isinstance(quiz_page(test_state, "test error"), Page), True)

# Quiz submission and recommendations
test_quiz_state = State("", list(GAMES), Preferences("", "PC", 1, False), [], [], GAMES[0])
submit_quiz(test_quiz_state, "open world", "PlayStation", "2 - Medium", False)
assert_equal(len(test_quiz_state.recommendations), 3)
assert_equal(test_quiz_state.preferences.genre, "open world")
assert_equal(isinstance(recommendations_page(test_quiz_state), Page), True)
assert_equal(isinstance(history_page(test_quiz_state), Page), True)

# Invalid quiz genre should not add recommendations
invalid_quiz_state = State("", list(GAMES), Preferences("", "PC", 1, False), [], [], GAMES[0])
submit_quiz(invalid_quiz_state, "not a genre", "PC", "1 - Easy", False)
assert_equal(len(invalid_quiz_state.recommendations), 0)

# Game library, filtering, and details
assert_equal(isinstance(game_library_page(test_state), Page), True)
assert_equal(isinstance(filter_games(test_state, "all"), Page), True)
assert_equal(isinstance(filter_games(test_state, "open world"), Page), True)
assert_equal(isinstance(filter_games(test_state, "not a genre"), Page), True)
assert_equal(isinstance(game_details_page(test_state, "Minecraft"), Page), True)
assert_equal(test_state.selected_game.title, "Minecraft")

# Favorites
favorite_state = State("", list(GAMES), Preferences("", "PC", 1, False), [], [], GAMES[0])
toggle_favorite(favorite_state, "Minecraft")
assert_equal(len(favorite_state.favorites), 1)
assert_equal(favorite_state.favorites[0].title, "Minecraft")
toggle_favorite(favorite_state, "Minecraft")
assert_equal(len(favorite_state.favorites), 0)
assert_equal(isinstance(favorites_page(favorite_state), Page), True)

# Add-game page and submitting games
assert_equal(isinstance(add_game_page(test_state), Page), True)
assert_equal(isinstance(add_game_page(test_state, "test error"), Page), True)

new_game_state = State("", list(GAMES), Preferences("", "PC", 1, False), [], [], GAMES[0])
submit_game(new_game_state, "New Test Game", "action, open world", "PC",
            "2 - Medium", False, "5 hours", "Test description", "Test notes")
assert_equal(len(new_game_state.games), len(GAMES) + 1)
assert_equal(new_game_state.games[-1].title, "New Test Game")
assert_equal(new_game_state.games[-1].genres, ["action", "open world"])
assert_equal(new_game_state.games[-1].difficulty, 2)

# Invalid game submissions should not add a game
submit_game(new_game_state, "New Test Game", "action", "PC",
            "2 - Medium", False, "5 hours", "d", "n")
assert_equal(len(new_game_state.games), len(GAMES) + 1)
submit_game(new_game_state, " ", "action", "PC",
            "2 - Medium", False, "5 hours", "d", "n")
assert_equal(len(new_game_state.games), len(GAMES) + 1)
submit_game(new_game_state, "Another Game", "notagenre", "PC",
            "2 - Medium", False, "5 hours", "d", "n")
assert_equal(len(new_game_state.games), len(GAMES) + 1)


start_server(State("", list(GAMES), Preferences("", "PC", 1, False), [], [], GAMES[0]))


