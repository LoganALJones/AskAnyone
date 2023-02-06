type Author = {
    id: number
    first_name: string
    last_name: string
    imageSrc: string
}

type Book = {
    id: number
    title: string
    author: author[] 
    publication_date: string
    author_id: number
}
