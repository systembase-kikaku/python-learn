try:
    a = 0
    b = "hoge"
    # print(100/a)
    # print(a + b)
    raise ZeroDivisionError("Hello")
except ZeroDivisionError as e:
    print("ゼロ除算", e)
except Exception as e:
    print("その他のエラー", e)
finally:
    print("終了")
