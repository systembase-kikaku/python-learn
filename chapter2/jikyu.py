user = input("時給はいくらですか？")
jikyu = int(user)

user = input("何時間働きましたか？")
jikan = int(user)

kyuryou = jikyu * jikan

fmt = """\
時給{0}円で、{1}時間働いたので...
給料は、{2}円です。
"""
desc = fmt.format(jikyu, jikan, kyuryou)
print(desc)
