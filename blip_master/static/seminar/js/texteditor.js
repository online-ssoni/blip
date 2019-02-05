 var ckeditor = CKEDITOR.replace( 'editor1' );
 ckeditor.on('change', function(event) {
          console.log(event.editor.getData())
 });