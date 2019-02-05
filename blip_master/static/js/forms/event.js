
  document.addEventListener('DOMContentLoaded', function() {
    var dateElems = document.querySelectorAll('#id_start_time_date_0');
    M.Datepicker.init(dateElems, autoClose=true);

    var timeElems = document.querySelectorAll('#id_start_time_date_1');
    M.Timepicker.init(timeElems, autoClose=true);
  });