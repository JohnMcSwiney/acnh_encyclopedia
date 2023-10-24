import React,{useEffect, useState} from 'react'
import './ComponentStyles.css'
import { useContentContext } from "../context/contentContext";
function FishCard({fishObject }) {
    const context = useContentContext();
    
    const [selected, setSelected] = useState(false)
    const handleClick = ()=> {
        context.updateCurrentCreature(fishObject.Fish)
        context.updateCreatureObject(fishObject)
        // setSelected(true)
    };
    // useEffect(()=>{
    //     let currentCreature = context.currentCreature;
    //     // console.log(currentCreature)
    //     // if(currentCreature !== fishName){
    //     //     setSelected(false)
    //     // }
    // },[])
  return (
    <button 
    className={selected ? 'fish__card card__selected' : 'fish__card'}
    onClick={handleClick}
    >
        <img src={fishObject.IconUrl} alt={fishObject.Fish}></img>
    </button>
  )
}

export default FishCard