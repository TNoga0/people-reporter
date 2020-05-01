var number_of_people = null;
$('.ppl-number').click((e) => {
  number_of_people = e.target.value;
});

var activity_of_people = null;
$('.ppl-activity').click((e) => {
  activity_of_people = e.target.value;
});

var save_button = document.getElementById("btn-save");
var modal = document.getElementById("reportModal");

save_button.onclick = function () {
  var args = {
    'number': number_of_people,
    'action': activity_of_people,
    'lat': window.value['lat'],
    'lng': window.value['lng']
  };
  activity_of_people = null;
  number_of_people = null;
  window.value = null;
  $.get("/add/", args).done(function(data) {
    modal.style.display = "none";
    map.closePopup();
    window.location.reload(true);
  });
}