let librarian = {id : "1",
        available : "true",
        count : "1",
        name : "Jamie",
        author : "king"
}

let newLibrarian = {id : Number(librarian.id),
                    available : Boolean(librarian.available),
                    count : Number(librarian.count),
                    name : String(librarian.name),
                    author : String(librarian.author)
}

console.log(newLibrarian)


