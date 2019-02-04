
  document.addEventListener('DOMContentLoaded', function() {
    var dateElems = document.querySelectorAll('.datepicker');
    M.Datepicker.init(dateElems, autoClose=true);

    var timeElems = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timeElems, autoClose=true);
  });