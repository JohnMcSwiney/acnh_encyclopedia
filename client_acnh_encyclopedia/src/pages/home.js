import React, { useEffect } from 'react'
import { useContentContext } from '../context/contentContext'
import { FaFish, FaBug } from 'react-icons/fa';
import { TbChartBubbleFilled } from 'react-icons/tb';
import './PageStyles.css'

function Home() {
  const contentContext = useContentContext();
  const  contentType = contentContext.contentType;
  // console.log(contentType)
  // const [tempState,setTempState] = 
  // useEffect(() => {

  // },[])
  return (
    <div className='page__container'>
      
      <div className='selector__box'>
      <button 
      className={contentType === 'FISH' ? 'fish__btn selected ' : 'fish__btn'}
      onClick={() => contentContext.updateContentVal('FISH')}
      >
        <p>Fish</p> <FaFish/>
      </button>

      <button 
      className={contentType === 'BUG' ? 'bug__btn selected ' : 'bug__btn'}
      onClick={() => contentContext.updateContentVal('BUG')}
      >
        <p>Bugs</p> <FaBug/>
      </button>
      <button 
      className={contentType === 'DIVE' ? 'dive__btn selected ' : 'dive__btn'}
      onClick={() => contentContext.updateContentVal('DIVE')}
      >
        <p>Dive</p> <TbChartBubbleFilled/>
      </button>
      <button 
      className='hidden__btn'
      onClick={() => contentContext.updateContentVal('FISH')}
      >
        <p>default val</p>
      </button>
      </div>
      home
      {contentType}
      
    </div>
  )
}

export default Home