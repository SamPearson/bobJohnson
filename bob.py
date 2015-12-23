# Written by Crunch ThunderChunk and Tex HamDelt
import random

titles = [
"Captain",
"Admiral",
"Papa",
"Commandant"
]

# Name arrays should follow this naming convention
# first_(category name)
# last_a_(category name)
# last_b_(category name)

first_manly = [
"Flex",
"Tex",
"Hunk",
"Butch",
"Delt",
"Bulk",
"Tank",
"Punt",
"Bold",
"Splint",
"Flint",
"Thick",
"Blast",
"Buff",
"Slam",
"Fist",
"Smash",
"Punch",
"Buck",
"Dirk",
"Rip",
"Slate",
"Crunch",
"Slab",
"Smoke",
"Max",
"Flank"
]

first_grungy = [
"Stump",
"Lunk",
"Stump",
"Gristle",
"Lump",
"Crud"
]

first_animal = [
"Wolf",
]

first_wimpy = [
"Dunk",
"Touch",
"Flap",
"Tiny",
"Wink",
"Tiddles",
"Tinkles"
]

# All categories are built, so we initialize the full
# array of possible first names 
first = []
# and then append all of category arrays. In the end,
# "first" contains all possible first names. 
first += first_manly 
first += first_grungy 
first += first_animal
#first += first_titles
first += first_wimpy

# categories can be removed by commenting them out
#first += first_doesntWorkAndIsLame

# any categories must be defined as arrays before
# being appended to the main name array
# (just copy/paste an existing one and change the name)


last_a_prefixes = [
"Mc",
"Vander",
"Von "
]

last_a_manly = [
"Bulge",
"Grunge",
"Hard",
"Thunder",
"Squat",
"Dead",
"Saw",
"Thorn",
"Speed",
"Fridge",
"Huge",
"Power",
"Hunger",
"Full",
"War",
"Thick"
]

last_a_animals = [
"Shark",
"Tiger",
"Lion",
"Bear",
"Kitty"
]

last_a_body = [
"Muff"
]

last_a_deprecating = [
"Oopsie"
]
last_a_food =[
"Ham",
"Bacon",
"Muffin"
]

last_a_materials = [
"Rock",
"Iron",
"Steel",
"Oak",
"Rust"
]

last_a_gator = [
"Loose",
"Kindly",
"Active"
]

last_a = []
last_a += last_a_manly
last_a += last_a_food
last_a += last_a_animals
last_a += last_a_body
last_a += last_a_materials
last_a += last_a_gator



last_b_manly = [
"Slab",
"Meal",
"Body",
"Punch",
"Flex",
"Curl",
"Blade",
"Dodge",
"Rod",
"Quad",
"Lift",
"Chunk",
"Thrust",
"Flash",
"Swing",
"Delt",
"Large",
"Chest",
"Tooth",
"Bone",
"Pec",
"Face",
"Cheek",
"Iron",
"Branch",
"Broth",
"Fist",
"Beef",
"Point",
"Boom",
"Machine"
]

last_b_gator = [
"Reply",
"Emulsion",
]

last_b_food = [
"Burger",
"Cheese",
"Quiche"
]

last_b_jobs = [
"Monger",
"Builder",
"Buster",
"Quilter",
"Blaster",
"Pilot",
"Breaker",
"Handler"
]

last_b_body = [
"Hump",
"Muff",
"Flap",
"Loin",
"Jaw",
"Butt",
"Turd",
"Stag"
]

last_b = []
last_b += last_b_manly
last_b += last_b_gator
last_b += last_b_food
last_b += last_b_body
last_b += last_b_jobs

#Rolling a dice to use in percentage chances
diceRoll = random.randrange(100);
fullname = ""

# add a title sometimes
#if diceRoll > 75 :
#    fullname += random.choice(titles) + " " 

# sometimes two first names is funny
#if diceRoll > 80 : 
#    fullname += random.choice(first) 

# Add a random first name
fullname += random.choice(first) + " " 

# Sometimes prepend "mc" to the lastname 
if diceRoll > 90 : 
    fullname += "Mc" 

fullname += random.choice(last_a) 
fullname += random.choice(last_b)

# we have the full name, send it out
keyboard.send_keys(fullname)

