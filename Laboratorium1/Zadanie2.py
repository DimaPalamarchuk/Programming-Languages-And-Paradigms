def bfsTask(graph, start, end):
    odwiedzone.append(start)

def test(graph, start, end):
    odwiedzone.append(start)
    kolejka.append(end)

    while kolejka:
        m = kolejka.pop(0)
        print(m, end=" ")

        for sasiedzi in graph[m]:
            if sasiedzi not in odwiedzone:
                odwiedzone.append(sasiedzi)
                kolejka.append(sasiedzi)


graph = {
    '1' : ['2','3','5'],
    '2' : ['1', '4'],
    '3' : ['1', '5', '6'],
    '4' : ['2', '7'],
    '5' : ['1', '3', '7'],
    '6' : ['3', '8'],
    '7' : ['4', '5', '8'],
    '8' : ['6', '7']
}
odwiedzone = []
kolejka = []

print(test(graph, '1', '7'))


