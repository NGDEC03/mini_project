import React from 'react'

const OtherUser = () => {
  return (
    <div>
       <div className='flex gap-2 items-center hover:bg-zinc-200 rounded p-2 cursor-pointer'>
        <div className='avatar online'>
          <div className='w-12 rounded-full'>
            <img src='https://static.vecteezy.com/system/resources/thumbnails/002/002/403/small/man-with-beard-avatar-character-isolated-icon-free-vector.jpg' alt='' />
          </div>
        </div>
        
        <div className='flex flex-col flex-1'>
          <div className='flex justify-between items-center gap-2'>
            <p>Lalit</p>
          </div>
        </div>
      </div>
      <div className='divider my-0 py-0 h-1'></div>
     </div>
  )
}

export default OtherUser
