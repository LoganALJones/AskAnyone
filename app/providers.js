'use client';
import { ApolloProvider } from "@apollo/client";
import client from "../apollo-client";

export function Providers({ children }) {
  return (
    <ApolloProvider client={client}>
          {children}
    </ApolloProvider>
  );
}