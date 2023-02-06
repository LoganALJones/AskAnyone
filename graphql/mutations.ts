import { gql } from '@apollo/client';

export const ADD_AUTHOR = gql`
    mutation MyMutation(
        $first_name: String!
        $last_name: String!
        $imageSrc: String!
    ) {
        insertAuthor(
            first_name: $first_name
            last_name: $last_name
            imageSrc: $imageSrc
        ) {
            id
            first_name
            last_name
            imageSrc
        }
    }

`