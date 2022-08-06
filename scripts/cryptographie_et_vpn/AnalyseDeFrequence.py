
#%%

freq = {}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
secret = "TESTTESTTEST"

for c in alphabet:
    freq[c] = 0
freq[c]


letter_count = 0


for i in secret:
    if i in freq:
        freq[i] += 1
        letter_count += 1

for c in freq:
    freq[c] = round(freq[c]/letter_count, 4)

new_line_count = 0
for c in freq:
    print(c, ":", freq[c], " ", end='')
    if new_line_count % 3 == 2:
        print()


# %%
