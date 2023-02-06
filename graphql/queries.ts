import { gql } from '@apollo/client'

export const GET_ALL_BOOKS = gql`
    query MyQuery {
        bookList {
            title
            author
            publication_date
            id
            author {
                first_name
                last_name
                imageSrc
            }
        }
    }
`;

export const GET_ALL_AUTHORS = gql` 
    query MyQuery {
        authorList {
            first_name
            last_name
            imageSrc
        }
    }
`;

export const GET_BOOK_BY_AUTHOR = gql `
    query MyQuery($author_id: Int!) {
        getBookListByAuthor(id: $author_id) {
            id
            title 
            publication_date
        }
    }
`;