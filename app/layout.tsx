import "../styles/globals.css";
import Banner from "./Banner";
import Header from "./Header";
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <head />
      

      <body>
        <Header />
        <Banner />
        <div>{children}</div>
      </body>
    </html>
  )
}
