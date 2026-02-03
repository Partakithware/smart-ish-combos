import itertools

# Common words in pop culture phrases
adjectives = [
    'big', 'little', 'great', 'super', 'mega', 'ultra', 'magic', 'holy', 
    'divine', 'dark', 'light', 'golden', 'silver', 'crystal', 'rainbow', 
    'invisible', 'secret', 'hidden', 'ancient', 'eternal', 'infinite', 
    'cosmic', 'stellar', 'green', 'lime', 'emerald', 'chlorophyte', 
    'mossy', 'jungle', 'distal', 'coastal', 'western', 'eastern', 'terminal',
    'terra', 'true', 'rare', 'fixed', 'worthy', 'broken', 'left', 'right',
    'bottom', 'top', 'central', 'western', 'eastern', 'crimson', 'corrupt',
    'hallowed', 'zen', 'drunk', 'constant', 'celebration', 'ultimate'
]

nouns = [
    'portal', 'gun', 'chest', 'treasure', 'box', 'cube', 'sphere', 'weapon', 
    'tool', 'device', 'machine', 'unicorn', 'rainbow', 'light', 'hallow', 
    'heaven', 'sky', 'surface', 'world', 'land', 'realm', 'kingdom', 'power', 
    'force', 'energy', 'border', 'boundary', 'coast', 'shore', 'ocean', 
    'abyss', 'clover', 'leaf', 'blade', 'spore', 'vines', 'edge', 'horizon',
    'beam', 'bolt', 'spark', 'pulse', 'terraprisma', 'zenith', 'excalibur',
    'night', 'brick', 'slab', 'platform', 'house', 'corner', 'marker',
    'point', 'center', 'origin', 'cross', 'spot', 'rim', 'beach'
]

verbs = [
    'is', 'has', 'does', 'makes', 'takes', 'gives', 'brings', 'finds', 'gets', 
    'sees', 'knows', 'thinks', 'wants', 'needs', 'spawns', 'contains', 
    'unlocks', 'equips', 'drops', 'crafts', 'summons', 'warps', 'teleports'
]

prepositions = [
    'in', 'on', 'at', 'to', 'from', 'with', 'of', 'for', 'by', 
    'inside', 'behind', 'under', 'through', 'across', 'within'
]

articles = ['the', 'a', 'an']


# Generate 2-word combinations
combos = set()

# article + noun
for art in articles:
    for noun in nouns:
        combos.add(f"{art} {noun}")

# adjective + noun  
for adj in adjectives:
    for noun in nouns:
        combos.add(f"{adj} {noun}")

# 2-word: noun + noun (The 2-Gram "compound" logic)
# Examples: "Ocean Chest", "Terra Blade", "Edge House"
for n1 in nouns:
    for n2 in nouns:
        if n1 != n2:
            combos.add(f"{n1} {n2}")

# 3-word: adjective + article + noun
for adj in adjectives:
    for art in articles:
        for noun in nouns:
            combos.add(f"{adj} {art} {noun}")

# 3-word: article + adjective + noun
for art in articles:
    for adj in adjectives:
        for noun in nouns:
            combos.add(f"{art} {adj} {noun}")

# 3-word: noun + preposition + noun
for n1 in nouns:
    for prep in prepositions:
        for n2 in nouns:
            combos.add(f"{n1} {prep} {n2}")

# 4-word: Noun + Preposition + Article + Noun
# Examples: "Gun in the Chest", "Portal from a Box"
for n1 in nouns:
    for prep in prepositions:
        for art in articles:
            for n2 in nouns:
                combos.add(f"{n1} {prep} {art} {n2}")

# 3-word: Color + Noun + Location
# Examples: "Green Chest Edge", "Emerald Box Coast"
for color in ['green', 'lime', 'emerald']:
    for n in ['chest', 'box', 'vault', 'shrine']:
        for loc in ['edge', 'ocean', 'border', 'shore']:
            combos.add(f"{color} {n} {loc}")

# Specific Green-Edge-X Logic
for color in ['green', 'terra', 'lime', 'emerald']:
    for obj in ['beam', 'bolt', 'blade', 'spark', 'chest']:
        for rel in ['at', 'on', 'near']:
            for loc in ['edge', 'corner', 'marker', 'x']:
                combos.add(f"{color} {obj} {rel} {loc}")

# Save
with open('smart_combos.txt', 'w') as f:
    for combo in sorted(combos):
        f.write(combo + '\n')

print(f"Generated {len(combos)} smart combinations")
