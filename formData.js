// Function to retrieve form data
function getFormData() {
    const houseType = document.getElementById("houseType").value;
    const priceType = document.getElementById("priceType").value;
    const location = document.getElementById("location").value;

    console.log(location.value);
    
    const amenitiesCheckboxes = document.querySelectorAll(".amenities-checkbox");
    const amenities = Array.from(amenitiesCheckboxes)
        .filter(checkbox => checkbox.checked)
        .map(checkbox => checkbox.value);

    return {
        houseType,
        priceType,
        location,
        amenities,
    };
}

// Function to send form data to Python backend
function submitForm() {
    const formData = getFormData();

    fetch('/api/house-predictor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data here
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Add an event listener to the form submit button
document.getElementById("submit").addEventListener("click", submitForm);
