import { gql } from '@apollo/client'

export const GET_BOOK_BY_AUTHOR = gql `
    query MyQuery($author_id: Int!) {
        getBookListByAuthor(id: $author_id) {
        id
        title 
        publication_date
    }
}
`