/**
 * Name: socket_client.js
 * Description: File for handing sockets for chat and the codeeditor
 * Input: Session ID for the seminar session
 * author: Monish, Abhiyan
 */


/*===================================== Opening and propagating message===================================*/

const SOCKET_ENDPOINT_URL = "ws://localhost:8848/" 

const WS = new WebSocket(SOCKET_ENDPOINT_URL)

WS.onmessage = (event) => {
    endPointData = JSON.parse(event['data'])
    console.log(endPointData,'session_id' , SESSION_ID)
    if(endPointData['session_id'] != SESSION_ID){
        return;
    }
   
    if(endPointData['toggle'] == 'dirty' && loggedInUser=='participant') {
    toggleHostEditor();      
  
   }
   if(!validate(endPointData['session_id'])){
        return;
   }
   if(endPointData['type']=='state') {
       if(endPointData['content_type']=='text'){
            handleText(endPointData); 
       } else {
         hostEditorHandler(endPointData);
       }
       
   }
   else if(endPointData['type']=='chat') {
      //Call Chat Service Here
      handleNewMessage(endPointData);
   }
   
}


WS.onclose = (event) => {
    alert('WEB SOCKET HAS GONE AWAY');
}

//This will have the validation logic for session
function validate(sessionToken) {
    return true
}

function broadcastMessage(message) {
    message['session_id'] = SESSION_ID;
    message['username'] = USERNAME;
    
    WS.send(JSON.stringify(message));
}

function toggleHostEditor() {
	$('#cke_text_editor').fadeToggle(0,'swing',()=>{
            $('#host_code_editor').fadeToggle(0,'swing');
        });
}
/*===================================== End Of Opening and propagating message===================================*/

