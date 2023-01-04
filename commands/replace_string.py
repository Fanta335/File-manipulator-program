def replace_string(inpath: str, needle: str, newstring: str) -> None:
    contents = ''
    with open(inpath) as f:
        contents = f.read()

    with open(inpath, 'w') as f:
        f.write(contents.replace(needle, newstring))
