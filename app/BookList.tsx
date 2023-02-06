import React from 'react'
import { GET_BOOK_BY_AUTHOR } from '../graphql/queries'

function BookList() {




    try {
        await client.query({
            query: GET_BOOK_BY_AUTHOR
            variables: FormData.author 

    })
  return (
    <div>BookList</div>
  )
}

export default BookList