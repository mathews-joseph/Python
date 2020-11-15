"""
Bloom filters:
* lightweight version of a hash table.
Efficient lookups and insertions.

* Probabilistic DS

* More space efficient than a hash table,
but at the cost of having false positives
for entry lookup.

* No false negatives though.

* Useful when we want a DS that allows for
fast lookups and insertions and care about
how much space the DS uses. But don't care
if the DS sometimes indicates an item is
present when in fact it is not.

* If both the bits are set for a particular
element like "Bulbasaur" then we might have
seen "Bulbasaur" before but can't say for
sure.
"""

import pyhash

bit_vector = [0] * 20

# Non cryptographic hash functions (Murmur and FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calculate the values for Pikachu and Charmander
fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[fnv_char] = 1
bit_vector[murmur_pika] = 1
bit_vector[murmur_char] = 1

# A wild Bulbasaur appears
fnv_bulb = fnv("Bulbasaur") % 20
murmur_bulb = murmur("Bulbasaur") % 20
