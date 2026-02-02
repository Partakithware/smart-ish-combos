import itertools

# Common words in pop culture phrases
adjectives = [
    'big', 'little', 'great', 'super', 'mega', 'ultra', 'double', 'triple', 
    'magic', 'holy', 'divine', 'dark', 'light', 'golden', 'silver', 'crystal', 
    'rainbow', 'invisible', 'secret', 'hidden', 'ancient', 'eternal', 'infinite', 
    'cosmic', 'stellar', 'legendary', 'mythic', 'exotic', 'unstable', 'quantum', 
    'void', 'sentient', 'heavy', 'portable', 'kinetic', 'astral', 'cyber'
]

nouns = [
    'portal', 'gun', 'chest', 'treasure', 'box', 'cube', 'sphere', 'weapon', 
    'tool', 'device', 'machine', 'unicorn', 'rainbow', 'light', 'hallow', 
    'heaven', 'sky', 'surface', 'world', 'land', 'realm', 'kingdom', 'power', 
    'force', 'energy', 'launcher', 'cannon', 'vault', 'crate', 'cache', 
    'battery', 'engine', 'rift', 'wormhole', 'anchor', 'beacon', 'terminal'
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

# Save
with open('smart_combos.txt', 'w') as f:
    for combo in sorted(combos):
        f.write(combo + '\n')

print(f"Generated {len(combos)} smart combinations")
