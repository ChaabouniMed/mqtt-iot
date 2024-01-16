// Fonction pour mettre à jour la valeur de température et afficher une alerte si nécessaire
function updateTemperature(temperature) {
    // Récupérer l'élément d'affichage de la température
    const temperatureElement = document.getElementById('temperature-value');

    // Mettre à jour la valeur de température
    temperatureElement.innerText = `Current Temperature: ${temperature}°C`;

    // Vérifier si la température dépasse le seuil
    const threshold = 28; // Seuil de température
    if (parseFloat(temperature) > threshold) {
        // Afficher une alerte si la température dépasse le seuil
        temperatureElement.style.color = 'red'; // Changer la couleur du texte en rouge
        alert(`Alerte : La température a dépassé ${threshold} (${temperature}) !`);
    } else {
        // Réinitialiser la couleur du texte si la température est inférieure au seuil
        temperatureElement.style.color = '#0066cc';
    }
}

// Fonction pour charger la température initiale
function fetchTemperature() {
    fetch('http://127.0.0.1:5000/api/temperature')
        .then(response => response.json())
        .then(data => {
            updateTemperature(data.temperature);
        })
        .catch(error => {
            console.error('Error fetching temperature data:', error);
        });
}

// Mettez à jour la température initiale lors du chargement de la page
fetchTemperature();

// Mettez à jour la température toutes les 5 secondes
setInterval(function () {
    fetchTemperature();
}, 5000);
