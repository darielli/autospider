
def test(key):
    with open("data.txt", 'r+') as f:
        data = f.readlines()
        for i in data:
            if i.startswith(key):
                print(i.split(':')[1])
                break