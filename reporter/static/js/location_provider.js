var center_button = document.getElementById("center-view");

function getLocation() {
  var geolocation = navigator.geolocation;
  geolocation.getCurrentPosition(showLocation, errorHandler);
}

function showLocation( position ) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  map.setView([latitude, longitude], 16);
  var circle_pos_marker = L.circle([latitude, longitude], {
    color: '#3449eb',
    fillColor: '#74bffc',
    fillOpacity: 0.5,
    radius: 40,
  }).addTo(map)
}

function errorHandler( error ) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      alert("Request for Geolocation denied.");
      break;
    case error.POSITION_UNAVAILABLE:
      alert("Location information is unavailable.");
      break;
    case error.TIMEOUT:
      alert("The request to get user location timed out.");
      break;
    case error.UNKNOWN_ERROR:
      alert("An unknown error occurred.");
      break;
  }
}

center_button.onclick  = function () {
  getLocation()
};

getLocation()