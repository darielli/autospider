
def test(key):
    with open("cache/data.txt", 'r+') as f:
        data = f.readlines()
        for i in data:
            if i.startswith(key):
                print(i.split(':')[1])
                f.write(key * 2)
                return
        print("no in it")
