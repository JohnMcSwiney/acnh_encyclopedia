import React from 'react'
import { FaLeaf } from 'react-icons/fa';
import './ComponentStyles.css'

function Header() {
  return (
    <div className='header__container'>
        <h1><FaLeaf/> NH Encyclopedia</h1>
        <p>Johnny McSwiney 2023</p> 
    </div>
  )
}

export default Header