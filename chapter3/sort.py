animals = [
  ("ライオン", 58),
  ("チーター", 110),
  ("シマウマ", 60),
  ("トナカイ", 80)
]

flist = sorted(animals, key = lambda a : a[1], reverse = True)

for i in flist:
    print(i)

animal_map = {
    "ライオン": 58,
    "チーター": 110,
    "シマウマ": 60,
    "トナカイ": 80
}

flist2 = sorted(animal_map.items(), key = lambda a : a[1], reverse = True)

for i in flist2:
    print(i)
