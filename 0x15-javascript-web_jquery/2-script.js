//updates the text color when the user clicks on the tag DIV#red_header
$(document).ready(function(){
  $('header').click(function() {
    $(this).css('color', '#FF0000');
  });
});
