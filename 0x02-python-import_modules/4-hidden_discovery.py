#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    jina = dir(hidden_4)
    for named in jina:
        if named[:2] != "__":
            print(named)
