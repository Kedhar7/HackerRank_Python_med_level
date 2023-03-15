def merge_the_tools(s, k):
    n = len(s)
    for i in range(0, n, k):
        ti = s[i:i+k]
        ui = []
        seen = set()
        for c in ti:
            if c not in seen:
                seen.add(c)
                ui.append(c)
        print(''.join(ui))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
