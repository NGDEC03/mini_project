import React from 'react'
import SendInput from './SendInput'

const MessageContainer = () => {
  return (
    
    <div className='md:min-w-[550px] flex flex-col'>
    <div className='flex gap-2 items-center bg-zinc-800 text-white px-4 py-2 mb-2'>
        <div className= 'avatar online'>
            <div className='w-12 rounded-full'>
                <img src='https://static.vecteezy.com/system/resources/thumbnails/002/002/403/small/man-with-beard-avatar-character-isolated-icon-free-vector.jpg' alt="user-profile" />
            </div>
        </div>
        <div className='flex flex-col flex-1'>
            <div className='flex justify-between gap-2'>
                <p>lalit</p>
            </div>
        </div>
    </div>
    <MessageContainer/>
    <SendInput/>
</div> 
  )
}


export default MessageContainer
