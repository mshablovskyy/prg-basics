import re
def f(addr):
    letters = re.findall("[a-zA-Z]", addr)
    nums = re.findall("[0-9]", addr)
    ok = True
    if len(letters) > 2 or len(nums) > 4:
        ok = False
    if ok:
        try:
            addr_l = letters+nums
            for i in range(len(addr)):
                if addr[i] != addr_l[i]:
                    ok = False
        except Exception:
            return False
    return ok

if __name__ == "__main__":
    print(f("A4"))
    print(f("a4"))
    print(f("4a"))
    print(f("bC123"))
    print(f("bcd555"))
    print(f("g_945"))
