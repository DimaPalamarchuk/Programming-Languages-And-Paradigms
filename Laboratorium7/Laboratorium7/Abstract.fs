module Abstract

type Person(name: string, age: int) =
    // pola prywatne
    let mutable privateAge = age

    // właściwości
    member this.Name = name

    // get i set
    member this.Age
        with get() = privateAge
        and set(value) =
            if value > 0 then
                privateAge <- value
            else
                printf "Wiek musi być liczbą dodatnią"
    
    // metoda
    member this.View() =
        printfn "Witaj %s masz %d lat." this.Name this.Age


// klasa pochodna
type Student(name: string, age: int, nrAlbumu: string) =
    // Dziedziczenie
    inherit Person(name, age)

    // Właściwość
    member this.NrAlbumu = nrAlbumu

    member this.View() = // Zamiast member == override
        printfn "Witaj %s masz %d lat, nr albumu %s" this.Name this.Age this.NrAlbumu

// obiekt klasy
let person = Person("Jan", 23)
person.View()

// Klasa abstrakcyjna
[<AbstractClass>]
type Shape() =
    abstract member Area: unit -> float

    member this.View() =
        printfn "To jest zwykła metoda z klasy abstrakcyjnej"

type Circle(radius: float) =
    inherit Shape()

    override this.Area () =
        System.Math.PI * radius * radius

// Interfaces
type IShape =
    abstract member Area: float
    abstract member Area1: unit -> float

type Circle1(radius: float) =
    interface IShape with
        // Właściwości
        member this.Area = System.Math.PI * radius * radius
        // Metoda
        member this.Area1 (): float =
            System.Math.PI * radius * radius
       

