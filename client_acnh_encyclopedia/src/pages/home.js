import React from 'react'
import { useContentContext } from '../context/contentContext'
import { FaFish, FaBug } from 'react-icons/fa';
function Home() {
  const { contentType} = useContentContext();
  // console.log(contentType)
  return (
    <div className='page__container'>
      home
      {contentType}
      <button 
      // onClick={}
      >
        <FaFish/>
      </button>
    </div>
  )
}

export default Home