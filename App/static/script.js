var currentLatitude;
var currentLongitude;


if(navigator.geolocation)
{
    navigator.geolocation.getCurrentPosition(showPosition);
}
  
else
{
    console.log("Geolocation not supported by this browser.");
}

function showPosition(position)
{
    currentLatitude = position.coords.latitude;
    currentLongitude = position.coords.longitude;
    console.log("Latitude: " + currentLatitude);
    console.log("Longitude: " + currentLongitude);
}