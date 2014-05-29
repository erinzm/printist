$(function() {
  $.getJSON('/api/printer/lock', function(data) {
    alert(data);
  });
});