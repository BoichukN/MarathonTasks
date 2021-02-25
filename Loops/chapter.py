# John wants to filter all the verses in a specific chapter in the Bible by the verse id.
# The Bible has 66 books, each book has a lot of chapters, and each chapter has a lot of verses.
# The pattern of the id is 'bb_ccc_vvv', where:
#
# bb is the Book ID. (01 < bb ≤ 66);
# ccc is the Chapter ID. (001 ≤ ccc);
# vvv is the Verse ID. (001 ≤ vvv).
# John wants to find verses that belong to the Book and Chapter, given by their IDs.


def filter_bible(scripture, book, chapter):
    """
    :param scripture: list
    :param book: str
    :param chapter: str
    :return: list
    """
    out = []
    start = book + chapter
    for i in scripture:
        if i[:5] == start:
            out.append(i)
        else:
            continue
    return out
