# Written by Crunch ThunderChunk and Tex HamDelt
import random


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

first_titles = [
"Captain",
"Admiral",
"Papa",
"Commondant"
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

first = []
first += first_manly 
first += first_grungy 
first += first_animal
first += first_titles
first += first_wimpy


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

last_a_food =[
"Ham",
"Bacon",
"Muffin"
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


fullname = random.choice(first) + " " + random.choice(last_a) + random.choice(last_b)
keyboard.send_keys(fullname)

