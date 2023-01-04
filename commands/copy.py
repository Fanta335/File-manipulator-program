def copy(inpath: str, outpath: str) -> None:
    contents = ''
    with open(inpath) as f:
        contents = f.read()

    with open(outpath, 'x') as f:
        f.write(contents)
