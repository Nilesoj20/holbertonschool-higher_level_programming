#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for hi in dir(hidden_4):
        if hi[0] != '_' and hi[1] != '_':
            print(hi)
