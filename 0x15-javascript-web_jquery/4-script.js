//Toggles the class of the HTML tag HEADER to red 
$(document).ready(function(){
  $('#toggle_header').click( function() {
    $('header').toggleClass('red green');
  });
});
