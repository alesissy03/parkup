// TODO (Task 7):
// - initializează harta Leaflet
// - setează view folosind coordonatele din backend (DEFAULT_CENTER)
// - încarcă /api/parking/lots și /api/parking/spots
// - desenează poligoane și marchează starea locurilor
// TODO Task 7: inițializează harta Leaflet
function initializeMap() {
  // - creează obiectul map
  // - setează view-ul pe DEFAULT_CENTER
  // - adaugă tile layer (OpenStreetMap)
}

// TODO Task 7: încarcă parcările (parking lots) de la backend
function loadParkingLots() {
  // fetch("/api/parking/lots") ...
}

// TODO Task 7: încarcă locurile de parcare (parking spots)
function loadParkingSpots(filters = {}) {
  // fetch("/api/parking/spots?...") cu eventualele filtre
}

// TODO Task 8: aplică filtre (număr locuri libere, nume parcare, status etc.)
function applyFilters() {
  // citește valori din UI și apelează loadParkingSpots cu filtre
}

// Punct de intrare
document.addEventListener("DOMContentLoaded", () => {
  console.log("map.js – entrypoint");
  // TODO Task 7: initializeMap(); loadParkingLots(); loadParkingSpots();
});
