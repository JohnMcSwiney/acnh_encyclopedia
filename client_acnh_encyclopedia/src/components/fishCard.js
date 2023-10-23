import React from 'react'
import './ComponentStyles.css'
function FishCard({fishName,fishIcon, isCaught, isSelected }) {
  return (
    <button 
    className={isSelected ? 'fish__card card__selected' : 'fish__card'}
    >
        <img src={fishIcon} alt={fishName}></img>
    </button>
  )
}

export default FishCard