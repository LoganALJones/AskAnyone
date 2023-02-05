"use client";
import { useRouter } from 'next/navigation';
import React, { FormEvent, useState } from 'react';

function SearchBox() {
    const [input, setInput] = useState("");
    const router = useRouter();

    const handleSearch= (e: FormEvent<HTMLFormElement>) => { 
        e.preventDefault();
        if (!input) return;

        router.push(`/search?term=${input}`);

    };
    
  return( 
  <form className=" ml-auto max-w-6xl mx-auto flex justify-center items-center pxl-5 py-0 w-1/5 mt-5"
  onSubmit={handleSearch}>

    <input type="text"
    value={input} 
    onChange={(e) => setInput(e.target.value)}
    className="mx-2 w-full h-10 rounded-sm flex-1 placeholder-gray-500 text-purple-900 outline-none " 
    placeholder="Search Thinkers..." />

    <button type="submit"
    disabled={!input}
    className="text-purple-900 disabled:text-gray-400">
    Search</button>
  </form>
  );
}

export default SearchBox