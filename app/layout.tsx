import "../styles/globals.css";
import Banner from "./Banner";
import Header from "./Header";
import SearchBox from "./SearchBox";
import { Providers } from './providers'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <head />
      

      <body className="bg-black-100">
        <Header />
        <Banner />
        <SearchBox />
        <div
        className="max-w-6xl mx -auto">
          <Providers>{children}</Providers></div>
      </body>
    </html>
  )
}

