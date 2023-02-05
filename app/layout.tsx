import "../styles/globals.css";
import Header from "./Header";
import { Providers } from './providers'
import ThinkerList from "./ThinkerList";

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
        <div>
          <Providers>{children}</Providers></div>
      </body>
    </html>
  )
}

