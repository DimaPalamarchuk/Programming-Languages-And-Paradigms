#podejście proceduralne

def plecak_dynamiczne(wagi, wartosci, pojemnosc):
    n = len(wartosci)
    dp = [[0 for _ in range(pojemnosc + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(pojemnosc + 1):
            if wagi[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wagi[i - 1]] + wartosci[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    maks_wartosc = dp[n][pojemnosc]
    w = pojemnosc
    wybrane_przedmioty = []

    for i in range(n, 0, -1):
        if maks_wartosc != dp[i - 1][w]:
            wybrane_przedmioty.append(i - 1)
            w -= wagi[i - 1]
            maks_wartosc -= wartosci[i - 1]
    return dp[n][pojemnosc], wybrane_przedmioty

wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 6]
pojemnosc = 5
maks_wartosc, przedmioty = plecak_dynamiczne(wagi, wartosci, pojemnosc)
print("Maksymalna wartość:", maks_wartosc)
print("Wybrane przedmioty:", przedmioty)

