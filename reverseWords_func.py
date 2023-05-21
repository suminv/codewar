def reverseWords(str):
    """Reversed Words"""
    return " ".join(str.split(" ")[::-1])


assert reverseWords("The greatest victory is that which requires no battle") == "battle no requires which that is " \
                                                                                "victory greatest The"
