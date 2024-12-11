module Entry
open System

printfn "Hello from F#"

let xTest = 10
let testText = "It's my test"
let yTest = 10.3

printfn "Text = %s" testText
printfn "X = %d" xTest
printfn "Y = %f" yTest
printfn "Y.2 = %.2f" yTest


printfn ""


printfn "Podaj imię: "
let name = Console.ReadLine()
printfn "Twoje imię: %s" name

let powitanie = "Witaj " + name
printfn "%s" powitanie


printfn ""

if xTest > 0 then
    printfn "Liczba dodatnia"
else
    printfn "Liczba ujemna"

let lista = [1;2;3]
let nowaLista = 0 :: lista // :: - dodanie do listy nowego elementu

for i = 1 to 5 do
    printfn "Wartość %d" i


for i = 5 downto 1 do
    printf "Wartość %d" i

let mutable x = 5 // mutable - jeżeli będzie zmieniać się liczba
while x<5 do
    printfn "Wartość %d" x
    x <- x+1

type Osoba = 
    {
        Imie: string
        Wiek: int
    }
type Student = 
    {
        Imie: string
        Wiek: int
        Adres: string
    }

printfn ""

let osoba1 = {Imie = "Dmytro"; Wiek = 19}
let student1 = {Imie = "Kasia"; Wiek = 20; Adres = "Ulica X, Mieszkanie Y"}

printfn "Imie: %s, Wiek: %d" osoba1.Imie osoba1.Wiek
printfn "Imie studenta: %s, Wiek studenta: %d, Adres studenta: %s" student1.Imie student1.Wiek student1.Adres


printfn ""

// Zmiana typu dannych
let str = "3.14"
let liczba = Double.TryParse(str)

printfn ""

printfn "Podaj liczbe całkowitą: "
let input = Console.ReadLine() // "34" strig
let number = Int32.Parse(input) // 34 zmiana na int

// match
//match wyrazenie with
//    | wzorzec1 -> wynik1
//    | wzorzec2 -> wynik2
//    | wzorzec3 -> wynik3
//    | _ -> wynikDomyslny

let zmianna = 3

match zmianna with
    | 1 -> printfn "Jeden"
    | 2 -> printfn "Dwa"
    | 3 -> printfn "Trzy"
    | _ -> printfn "Inna liczba"

printfn ""

let age = 20

match age with
    | x when x<18 -> printfn "Osoba niepełnoletnia"
    | x when x>18 && x<65 -> printfn "Osoa pełnoletnia"
    | _ -> printfn "Senior"

// Rekurencja
let rec suma n =
    if n<=0 then 0
    else n + suma(n-1)

printfn "Suma liczb od 1 do 5 = %d" (suma 5)

let tablica = [|10;20;30|]
for i = 0 to tablica.Length - 1 do
    printfn "element %d: %d " i tablica.[i]

// rekurencja ogonowa
let sumrekTail n =
    let rec loop n acc =
        if n <= 0 then acc
        else loop (n-1) (acc+n) // rekurencja ogonowa
    loop n 0 // wywołanie funkcji pomicniczej

//let funkcja =
//    printfn "dsaa"

//let funkcja1 =
//    printfn "sdda"

//let funkcja2 =
//    printfn "sdaaa"

//[<EntryPoint>]
//let main argv =
//    // ciało
//    funkcja
//    funkcja1
//    //
