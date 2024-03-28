#
# youtube.com/ridwaanhall
#

# Is Immutability A Lie In Python?
# %%
text: str = 'Ridwan Halim <3 Hafidhah Afkariana'
text = text.replace('<3', '❤️')
print(text)

# %%
coordinates: tuple[float, float] = (90.0, 180.0)
print('BEFORE:', id(coordinates))
coordinates += 3
print('AFTER:', id(coordinates))