

def test(key):
    with open("a.txt", "r") as f:
        f.write(key)
        f.close()