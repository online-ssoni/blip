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
    $(".input-msg").val("");
    let message = {
        'type' : 'chat',
        'message' : newMessageText,
        'session_id': '1235',
        'username' : USERNAME
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

const handleNewMessage = (peerMessage)=> {
    var senderName = peerMessage['username'];
    var newMessage = document.createElement('div');
    var msgContainer = document.getElementsByClassName('conversation-container')[0];
    var nameSpan = document.createElement('span')
    nameSpan.classList.add('metadata')
    nameSpan.innerHTML = `<small style="font-size:10px; color:gray;font-style:italic;">${senderName}</small></span>`
    
              
    messageText = peerMessage['message'];
    if(senderName == USERNAME){
        newMessage.classList.add('sent'); 
    } else {
        newMessage.classList.add('received');
    }
    newMessage.classList.add('message');
    
    newMessage.innerText = messageText;
    newMessage.append(nameSpan);
    msgContainer.append(newMessage);
    notifyUser();
}


/*===================================== End Of Functions For Chats ===================================*/

