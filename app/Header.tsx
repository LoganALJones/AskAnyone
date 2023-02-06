import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
import styled from 'styled-components'


function Header() {
  return <header>
<div className="relative flex grid grid-cols-4 p-10 h-8 items-center justify-start gap-5 shadow-md" style={{ display: "flex", justifyContent: "left" }}>
    <Link href="/">
        <Image className="h-150 w-50 cursor-pointer"  
            src = "/AskAnyoneResized-removebg.png"
            width = {250}
            height = {170}
            alt = "AskAnyone"
        ></Image>     
    </Link>
    
        <Link href="/" prefetch={false} className="flex items-center pl-5">
            <h1>Browse Bots</h1>s
        </Link>

        <Link href="/" prefetch={false} className="flex items-center pl-5">
            <h1>Create Bot</h1>
        </Link>

        {/* Button Dark Mode */}

        <button className="flex items-center hidden md:inline bg-slate-900 text-white px-4 lg:px-8 py-2 lg:py-4 rounded-full dark:bg-slate-800" style={{ marginLeft: "auto" }}>
            Contact
        </button>
    </div>

  </header>
}

export default Header