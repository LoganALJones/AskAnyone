import { ApolloClient, InMemoryCache, ApolloProvider, gql } from '@apollo/client';

const client = new ApolloClient({
    uri: 'http://localhost:5001/api/wrinkled-nightingale',
    headers: {
        Authorization: `Apikey ${process.env.NEVT_PUBLIC_STEPZEN_KEY}}`
    },
    cache: new InMemoryCache(),
  })

  export default client