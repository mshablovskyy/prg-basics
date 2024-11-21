def hide(text):
    if len(text) > 6:
        f = text[:2] + "*" * (len(text) - 6) + text[-4:]
    else:
        f = text
    return f