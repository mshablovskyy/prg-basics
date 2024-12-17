def f(subjects):
    min_v = 6
    min_key = None
    for k, v in subjects.items():
        avg = 0
        for i in v:
            avg += i
        avg = avg/len(v)
        if avg < min_v:
            min_v = avg
            min_key = k
    return min_key

if __name__ == "__main__":
    s = {"bio":[3,4,4,3,3], "his": [3,3,4,3,3]}
    print(f(s))
    s = {"math":[3,4,4], "geo": [5,4,4,4], "comp": [5,4]}
    print(f(s))