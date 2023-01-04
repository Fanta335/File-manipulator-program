def duplicate_contents(inpath: str, n: int) -> None:
    contents = ''
    result = ''
    with open(inpath) as f:
        contents = f.read()

    with open(inpath, 'w') as f:
        for i in range(n):
            result += contents
        f.write(contents + result)
