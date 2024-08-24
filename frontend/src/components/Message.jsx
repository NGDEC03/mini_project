import React from 'react'

const Message = () => {
  return (
    <div  >
    <div className="chat-image avatar">
        <div className="w-10 rounded-full">
            <img alt="Tailwind CSS chat bubble component" src="https://static.vecteezy.com/system/resources/thumbnails/002/002/403/small/man-with-beard-avatar-character-isolated-icon-free-vector.jpg"/>
        </div>
    </div>
    <div className="chat-header">
        <time className="text-xs opacity-50 text-white">12:45</time>
    </div>
    <div className='chat-bubble'>Message</div>
</div>
  )
}

export default Message
