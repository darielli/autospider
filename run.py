from spider import tuanwei
import os

if __name__ == "__main__":
    key = os.getenv('KEY')
    tuanwei.test(key)
