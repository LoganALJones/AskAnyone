'use client';
import React from 'react'
import { useQuery } from '@apollo/client'
import { GET_ALL_AUTHORS } from '../graphql/queries'
import Author from './Author';

function AuthorPage() {
    const {data, error} = useQuery(GET_ALL_AUTHORS)

    const authors: Author[] = data?.authorList;
    return (
        <div>
            {authors?.map(author => (
                <Author key={author.id} author={author} />
            ))}
        </div>
    )
}

export default AuthorPage