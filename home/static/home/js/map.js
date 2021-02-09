// Initialize and add the map
function initMap() {
    
    const gym = { lat: 51.651, lng: -0.072 };
    
    const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: gym,
    });

    const contentString =
        '<div id="content">' +
        '<div id="siteNotice">' +
        "</div>" +
        '<h1 id="firstHeading" class="firstHeading">Address</h1>' +
        '<div id="bodyContent">' +
        "<p>Unit 1, Southbury Road London, GB EN3 4HR</p>"
        "</div>" +
        "</div>";
    const infowindow = new google.maps.InfoWindow({
        content: contentString,
    });
    // The marker, positioned at Gym
    const marker = new google.maps.Marker({
    position: gym,
    map: map,
    });
    marker.addListener("click", () => {
        infowindow.open(map, marker);
    });
}