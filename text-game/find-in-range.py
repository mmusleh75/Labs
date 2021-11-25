
def Banner(msg, border="-"):
        print(len(msg)*border)
        print(msg)
        print(len(msg)*border)


def FindWordsRange(file_name, from_word, to_word):

    InRange = False

    with open(file_name) as f:
        content = f.read()

        content = content.split()

        content.sort()

    #    print(content)

        for token in content:

            if token >= from_word:
                InRange = True
            if token == to_word:
                print(token)
                InRange = False
            if token > to_word:
                InRange = False
            if InRange:
                print(token)

if __name__ == "__main__":

    file_name = "data.txt"
    from_word = "above"
    to_word = "in"

    FindWordsRange(file_name, from_word, to_word)

    #Banner("MBC NEWS - Breaking News !", border="+")
