// For more information see https://aka.ms/fsharp-console-apps
open System

// Zadanie 1. Stwórz aplikację konsolową, która oblicza wskaźnik masy ciała (BMI) użytkownika na
// podstawie wprowadzonych przez niego wagi (kg) i wzrostu (cm). Program powinien komunikować się z
// użytkownikiem, odczytywać dane wejściowe, przeliczać BMI i wyświetlać wynik wraz z kategorią BMI.
// Wymagane funkcje:
// • Komunikacja z użytkownikiem: Odczyt danych za pomocą Console.ReadLine() i wyświetlanie
// wyników za pomocą printfn.
// • Przekształcanie typów: Konwersja danych wejściowych z string na float.
// • Instrukcje warunkowe: Określenie kategorii BMI na podstawie wartości obliczonej.
// • Niezmienne struktury danych: Możesz użyć rekordów do przechowywania danych użytkownika.

type Uzytkownik = { Waga: float; Wzrost: float }

let obliczBMI (waga: float) (wzrost: float) =
    let wzrostM = wzrost / 100.0
    waga / (wzrostM * wzrostM)

let kategoriaBMI bmi =
    if bmi < 16.0 then "Wygłodzenie"
    elif bmi < 16.9 then "Wychudzenie"
    elif bmi < 18.4 then "Niedowaga"
    elif bmi < 24.9 then "Waga prawidłowa"
    elif bmi < 29.9 then "Nadwaga"
    elif bmi < 34.9 then "I stopień otyłości"
    elif bmi < 39.9 then "II stopień otyłości"
    else "III stopień otyłości (otyłość skrajna)"

let obliczBMINaPodstawieDanych () =
    printfn "Podaj swoją wagę w kg: "
    let wagaString = System.Console.ReadLine()
    let waga = float wagaString

    printfn "Podaj swój wzrost w cm: "
    let wzrostString = System.Console.ReadLine()
    let wzrost = float wzrostString

    let uzytkownik = { Waga = waga; Wzrost = wzrost }

    let bmi = obliczBMI uzytkownik.Waga uzytkownik.Wzrost
    printfn "Twoje BMI wynosi: %f" bmi

    let kategoria = kategoriaBMI bmi
    printfn "Twoja kategoria BMI: %s" kategoria

obliczBMINaPodstawieDanych ()




