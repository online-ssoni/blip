/**
 * Name: codeeditor.js
 * Description: File for handing code editor and RTC for syncronizing editor content with all the hosts
 * Input: Session ID for the seminar session
 */


/*===================================== Variable Initialization For Code Editor===================================*/

// $('code_editor').hide()
// $('#loading-spinner').hide()

// Initial editor configuration 
var language_selector = $('#select-language');
var theme_selector = $('#select-themes');
var runButton = $('#run-button');
var host_editor = $('.host-codemirror-textarea')[0]
var code = $('.codemirror-textarea')[0];



// Initial Configuration for the participant code editor
var editorconfig =  {
    theme: 'blackboard',
    mode: 'javascript',
    lineNumbers : true,
    styleActiveLine: true,
    extraKeys: {"Ctrl-Space":"autocomplete"} 
}

//Participant Code Editor Instance
var editor = CodeMirror.fromTextArea(code, editorconfig);

try {

    var hosteditorConfig = {
        lineNumbers: true,
        cursorHeight: 1.3,
        mode: null,
        styleActiveLine: true,
        theme: 'rubyblue',
        readOnly: 'cursor'
    }
//Host board editorconfiguration
var host_code_editor = CodeMirror.fromTextArea(host_editor,hosteditorConfig);

// This is very important for syncronizing the conetents in all the participants
host_code_editor.setSize(580,380);
editor.setSize(580,380);

} catch {
  console.log('This is host');
}


/*===================================== End Of Variable Initialization For Code Editor===================================*/


/*===================================== Functions for Code Editor ===================================*/


function runCode(script) {
    requestURL = "/seminar/run/"
    $.post(requestURL, {'script':script}, (data, status)=>{
        $('.editor-body').hide();
        $('#code_result').show();
        $('#loading-spinner').hide();
        result_html = `
        
            <hr>     
         <div style="color:white; font-weight:bolder; font-size:18px;">
         <p class="output_stats" >CPU TIME: ${data['cpuTime']} </p>
         <p class="output_stats" >Memory: ${data['memory']} </p>
         <p class="output_result" >Output: ${data['output']}   </p>   
   

         </div>

              `
        $('#exec_result').html(result_html);
    });
}


editor.on("change", broadcastHostChanges);

language_selector.on('change',function(){
    editor.toTextArea();
    var code = $('.codemirror-textarea')[0];
    editorconfig.mode = this.value;
    editorconfig.theme = theme_selector.val();
    editor = CodeMirror.fromTextArea(code, editorconfig);
    if(loggedInUser == 'host')
      editor.on('change',broadcastHostChanges) 
});



runButton.click(()=> {
    $('#code_editor').hide();
    $('.editor-body').hide()
    $('#loading-spinner').show();
    runCode(editor.getValue());
});

function broadcastHostChanges(){
    currentEditorConent = editor.getValue()
        editor.focus()
        currentCursorPosition = editor.getCursor()
        WS.send(JSON.stringify({'type':'board','user_type': 'host',
                    'content' : currentEditorConent,
                    'cursor_position' : currentCursorPosition,
                    'content_type' : 'code',
                    'board_state' : editorconfig,
                    'toggle' : 'pristine',
                    'session_id' : SESSION_ID
        }));
}

function hostEditorHandler (boardState) {
    if(loggedInUser != 'host') {
        console.log(boardState['toggle']);
         try {
            if(boardState['toggle'] == 'dirty') {
                alert('hello');
            } 
            if(hosteditorConfig.mode != boardState['board_state']['mode'] || hostEditorHandler.theme != boardState['board_state']['theme'] ) {
                hosteditorConfig.mode = boardState['board_state']['mode'];
                hosteditorConfig.theme = boardState['board_state']['theme'];
                host_code_editor.toTextArea();
                host_code_editor = CodeMirror.fromTextArea(host_editor, hosteditorConfig);
            }
            let content = boardState['content'];
            host_code_editor.getDoc().setValue(content);
            host_code_editor.setCursor(boardState['cursor_position'])
            host_code_editor.focus();
        } catch(TypeError) {
            console.log('Failed to parse the data or get contents')
        }
    }
   
}

function handleText(boardState){
    if(loggedInUser != 'host')
    ckeditor.setData(boardState['content']); 
}

/*===================================== End Of Functions for Code Editor ===================================*/

const dot1 = document.querySelector('.dot1');
const dot2 = document.querySelector('.dot2');
let hue = 0;

const adjustBgCol = () => {
  dot1.style.backgroundColor = 'hsl(' + hue + ',50%,50%)';
  dot2.style.backgroundColor = 'hsl(' + hue + ',50%,50%)';
}

$('#close_result').click(()=>{
    $('#code_result').hide();
    $('#code_editor').show();
   $('.editor-body').show();
});

setInterval(function(){ 
  hue++;
  adjustBgCol();
}, 15);