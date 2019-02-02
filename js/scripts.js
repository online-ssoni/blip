
userType = 'participant'
var language_selector = $('#select-language');
var ws = new WebSocket("ws://localhost:8848/")
var fontSize = $('#font-size');
var theme_selector = $('#select-themes');
var clientID = '554726cc60d4d57a2f28a33ad9a521a0'
var clientSecret = 'a09eedfac27ed317c1b80822445a154118aef64e035f11d807c38f7a45c1f0df'
var requestURL = 'https://api.jdoodle.com/v1/execute '
var runButton = $('#run-button');
var code = $('.codemirror-textarea')[0];
var editor = CodeMirror.fromTextArea(code, {
    theme: 'blackboard',
    cursorHeight: 2,
    mode: null
});

$(document).ready(()=>{
    $('#user-type').click(()=>{
        userType = $('#user-type-value').val()
        if(userType == 'host'){
            setInterval(()=>{
                currentEditorConent = editor.getValue()
                console.log(editor.getValue())
                console.log('Data sent')
                    ws.send(JSON.stringify({'user_type': userType,
                    'content' : currentEditorConent }))
                
            },1000);
      }
});
    fontSize.on('change',function(){
        $('#font-size-number').text(this.value)
        $('.CodeMirror').css('font-size',Number(this.value))
    });
    
    var config = {
        lineNumbers : true,
        cursorHeight : 1.3,
        autoCloseBrackets : true,
        scrollbarStyle : 'simple'
     }
    language_selector.on('change',function(){
        editor.toTextArea()
        var code = $('.codemirror-textarea')[0];
        config.mode = this.value;
        config.theme = theme_selector.val();
        editor = CodeMirror.fromTextArea(code, config);
    });

    ws.onmessage = (event)=>{
        if(userType == 'participant'){

            data = JSON.parse(event.data)
            try{
                let content = data['content']
                console.log(content)
                editor.getDoc().setValue(content);
                // document.getElementsByClassName('codemirror-textarea')[0].value = content
                // $('.codemirror-textarea')[0].val(content)
                
            } catch(TypeError){
                console.log("NOT LOADED")
            }
          
        } else {
            console.log('You are the host ')
        }
    }
});
    

    runButton.click(()=> {
    runCode(editor.getValue());
});


function runCode(script) {
    requestBody = {
        'clientId' : clientID,
        'clientSecret' : clientSecret,
        'script' : script,
        'language' : 'python2',
        'versionIndex' : 1,
         
    }
    $.post(requestURL, requestBody, (data, status)=>{
    });
}



ws.onclose = (event)=>{
    alert('WEB SOCKET HAS GONE AWAY');
}
// var config = {
//     apiKey: "AIzaSyADmGUdqp5x01ornjHp-xd5adYIeM9h508",
//     authDomain: "realtimecodesharing.firebaseapp.com",
//     databaseURL: "https://realtimecodesharing.firebaseio.com",
//     projectId: "realtimecodesharing",
//     storageBucket: "realtimecodesharing.appspot.com",
//     messagingSenderId: "1043195952233"
//   };
// firebase.initializeApp(config);
// dbRef.on('value', snap => console.log(snap.val()))

// const dbRef = firebase.database().ref().child('hello');

