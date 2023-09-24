// Function to fetch recommended houses from the server
function fetchRecommendedHouses() {
    fetch('/api/get-recommended-houses')
        .then(response => response.json())
        .then(recommendedHouses => {
            // Render the recommended houses on the page
            renderRecommendedHouses(recommendedHouses);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Function to render recommended houses on the page
function renderRecommendedHouses(recommendedHouses) {
    const resultsContainer = document.getElementById('results-container');

    // Clear any previous content
    resultsContainer.innerHTML = '';

    if (recommendedHouses.length === 0) {
        resultsContainer.innerHTML = '<p>No recommended houses found.</p>';
    } else {
        recommendedHouses.forEach(house => {
            const houseElement = document.createElement('div');
            houseElement.classList.add('house');

            // Create and populate elements for house details (e.g., name, price, image)
            // You can customize this part based on your house data structure

            // Append the house element to the results container
            resultsContainer.appendChild(houseElement);
        });
    }
}

// Fetch recommended houses when the page loads
window.addEventListener('load', fetchRecommendedHouses);
// After processing the form and getting recommendations
// Redirect the user to the results page
window.location.href = 'results.html';