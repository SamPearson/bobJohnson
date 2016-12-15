# Written by Crunch ThunderChunk and Tex HamDelt
import random

# Name arrays should follow this naming convention
# first_(category name)
# last_a_(category name)
# last_b_(category name)

first_animal = [
"Wolf",
]


first_grungy = [
"Stump",
"Lunk",
"Stump",
"Gristle",
"Lump",
"Crud"
]

first_manly = [
"Flex",
"Tex",
"Hunk",
"Butch",
"Delt",
"Dunk",
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


first_titles = [
"Captain",
"Admiral",
"Papa",
"Commandant"
]


# All categories are built, so we initialize the full
# array of possible first names 
first = []
# and then append all of category arrays. In the end,
# "first" contains all possible first names. 
first += first_manly 
first += first_grungy 
first += first_animal
first += first_titles


# categories can be removed by commenting them out
#first += first_doesntWorkAndIsLame

# any categories must be defined as arrays before
# being appended to the main name array
# (just copy/paste an existing one and change the name)

titles = [
"St. ",
"Mc",
"O'"
]

last_a_prefixes = [
"Vander",
"Von "
]

last_a_manly = [
"Grunge",
"Grudge",
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
"Bear"
]

last_a_food =[
"Ham",
"Muffin"
]

last_a_materials = [
"Rock",
"Iron",
"Steel",
"Oak",
"Rust"
]

last_a = []
last_a += last_a_prefixes
last_a += last_a_manly
last_a += last_a_food
last_a += last_a_animals
last_a += last_a_materials



last_b_manly = [
"Slab",
"Meal",
"Body",
"Punch",
"Flex",
"Curl",
"Blade",
"Dodge",
"Quad",
"Lift",
"Chunk",
"Flash",
"Swing",
"Delt",
"Large",
"Chest",
"Tooth",
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

last_b_weak = [
"Doodle",
"Flop",
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


last_b = []
last_b += last_b_manly
last_b += last_b_food
last_b += last_b_weak
last_b += last_b_jobs



fullname = ""

#Rolling a dice to use in percentage chances
diceRoll = random.randrange(100);

# sometimes two first names is funny
#if diceRoll > 80 : 
#    fullname += random.choice(first) 

# Add a random first name
fullname += random.choice(first) + " " 

# Sometimes prepend "mc" to the lastname 
if diceRoll > 90 : 
    fullname += random.choice(titles)

fullname += random.choice(last_a) 
fullname += random.choice(last_b)

# we have the full name, send it out
keyboard.send_keys(fullname)

