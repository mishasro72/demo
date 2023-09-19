def generate_hashtag(s):
    s = '#' + (s.title()).replace(' ', '')
    if 140 >= len(s) > 1:
        return s
    else:
        return "false"

print(generate_hashtag(''))
