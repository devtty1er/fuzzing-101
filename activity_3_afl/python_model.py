def check(buf: str) -> int:
    model_coverage = 0
    if len(buf) < 6:
        return
    model_coverage+=1
    if buf[0] != 'n':
        return
    model_coverage+=1
    if buf[1] != 'e':
        return
    model_coverage+=1
    if buf[2] != 'e':
        return
    model_coverage+=1
    if buf[3] != 'd':
        return
    model_coverage+=1
    if buf[4] != 'l':
        return
    model_coverage+=1
    if buf[5] != 'e':
        raise ValueError("Bug found!")
