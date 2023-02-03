import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
function Header() {
  return <header>
<div className="grid grid-cols-4 p-8 h-8 items-center justify-center gap-5 shadow-md" style={{ display: "flex", justifyContent: "center" }}>
        
        <Image className="h-150 w-50 cursor-pointer"
            src = "/AskAnyoneResized-removebg.png"
            width = {250}
            height = {170}
            alt = "AskAnyone"
        />

        <Link href="/" prefetch={false} className="pl-10">
            <h1>Browse Bots</h1>
        </Link>

        <Link href="/" prefetch={false} className="pl-10">
            <h1>Create Bot</h1>
        </Link>

        {/* Button Dark Mode */}

        <button className="hidden md:inline bg-slate-900 text-white px-4 lg:px-8 py-2 lg:py-3 rounded-full dark:bg-slate-800" style={{ marginLeft: "300px" }}>
            Contact
        </button>
    </div>

  </header>
}

export default Header