import React from 'react'

const OtherUser = (props) => {
  const user = props.user;
  return (
    <div>
       <div className='flex gap-2 items-center text-white hover:bg-zinc-900 hover:bg-zinc-200 rounded p-2 cursor-pointer'>
        <div className='avatar online'>
          <div className='w-12 rounded-full'>
            <img src={user?.profilePhoto} alt='' />
          </div>
        </div>
        
        <div className='flex flex-col flex-1'>
          <div className='flex justify-between items-center gap-2'>
            <p>{user?.fullName}</p>
          </div>
        </div>
      </div>
      <div className='divider my-0 py-0 h-1'></div>
     </div>
  )
}

export default OtherUser
