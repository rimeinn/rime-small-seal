from gen import parse


def test_parse():
    mappings, missing = parse(
        "# example\n\n"
        "U+3D001\tkSEAL_Rad\t1.3D000\n"
        "U+3D001\tkSEAL_MCJK\t5F0C\n"
        "U+3D002\tkSEAL_MCJK\t5F0C 5143\n"
        "U+3D002\tkSEAL_MCJK\t5F0C\n"
        "U+3D003\tkSEAL_Rad\t1.3D000\n"
    )
    assert mappings == {"弌": ["\U0003d001", "\U0003d002"], "元": ["\U0003d002"]}
    assert missing == ["\U0003d003"]


if __name__ == "__main__":
    test_parse()
