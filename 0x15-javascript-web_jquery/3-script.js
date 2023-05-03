//adds the class red to the HTML tag HEADER on click
$(document).ready(function(){
  $('#red_header').click(function() {
    $('header').addClass('red');
  });
});
