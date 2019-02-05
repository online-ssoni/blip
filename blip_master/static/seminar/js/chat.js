/**
 * Name: chat.js
 * Description: Chat Service for all the connected clients in a session  
 * Input: Session ID for the seminar session
 */

/*===================================== Variable Initialization For Chats ===================================*/

var chatWindow = $('#chat-container');
var chatPannel = $('#chat-pannel');
var chatMessages = $('.chat-message');
var messageContainer = $('#message-container');
var chatForm = $('#chat-form');
var messageCounter = $('#new-message-count')
var chatsTab = $('#chat-link')
var messageCount = 0

/*===================================== End Of Variable Initialization For Chats ===================================*/


/*===================================== Functions For Chats ===================================*/


chatsTab.click(()=>{
    messageCounter.text('0')
});

chatForm.submit((event)=>{
    event.preventDefault();
    let newMessageText = decodeURI(chatForm.serialize().split('=')[1]);
    
    let message = {
        'type' : 'chat',
        'message' : newMessageText,
        'session_id': '1235'
    }
    broadcastMessage(message);
});

function notifyUser(){
    newMessageAudio.play();
    if(!chatsTab.hasClass('cd-selected')){
        messageCount++;
        messageCounter.text(messageCount);
    }
}

const handleNewMessage = (peerMessage)=>{
    var newMessage = document.createElement('div');
    var msgContainer = document.getElementsByClassName('conversation-container')[0];
    messageText = peerMessage['message'];
    newMessage.classList.add('message');
    newMessage.classList.add('received');
    newMessage.innerText = messageText;
    msgContainer.append(newMessage);
    notifyUser();
}


/*===================================== End Of Functions For Chats ===================================*/

