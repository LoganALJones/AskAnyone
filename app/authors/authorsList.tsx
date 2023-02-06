import React from 'react'


const fetchAuthors = async () => {
}


function authorsList() {
const authors = await fetchAuthors()
  return (
    <div>authorsList</div>
  )
}

export default authorsList