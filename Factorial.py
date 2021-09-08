result = []
def rotate(num):

    if not num:
        result.append(num)
        return

    result.append(num)
    rotate(num-3)
    result.append(num)

if __name__ == '__main__':

    num = 12

    # let's rotate
    rotate(num)

    # convert numeric list to string list
    string_result = [str(e) for e in result]

    # concaticate the list items with comma
    final_answer = ",".join(string_result)


    print(final_answer)
