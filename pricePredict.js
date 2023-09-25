// Get the form element by ID within the event handler
const form = document.getElementById("housePriceForm");
    
// Get the predicted price element
const predictedPriceElement = document.getElementById("predicted-price");

// Function to retrieve form data
function getFormData() {
  const houseType = form.elements["houseType"].value;
  const housePrice = form.elements["housePrice"].value;
  const location = form.elements["location"].value;

  const amenitiesCheckboxes = document.querySelectorAll(".amenities-checkbox");
  const amenities = Array.from(amenitiesCheckboxes)
    .filter(checkbox => checkbox.checked)
    .map(checkbox => checkbox.value);

  return {
    houseType,
    housePrice,
    location,
    amenities,
  };
}

// Function to calculate the predicted price based on form data
function calculatePredictedPrice(formData) {
  // Example: Calculate predicted price based on user inputs
  let predictedPrice = 0;

  // Adjust the predicted price based on user inputs (e.g., house type, location, amenities)
  if (formData.houseType === "apartment") {
    predictedPrice += 100000; // Example price for an apartment
  } else if (formData.houseType === "house") {
    predictedPrice += 200000; // Example price for a house
  } else if (formData.houseType === "mansion") {
    predictedPrice += 500000; // Example price for a mansion
  }

  // Add more logic to adjust predicted price based on other inputs

  return predictedPrice;
}

// Function to update the predicted price element
function updatePredictedPrice(formData) {
  const predictedPrice = calculatePredictedPrice(formData);
  const predictedPriceElement = document.getElementById("predicted-price");
  predictedPriceElement.textContent = `Predicted Price: Rs ${predictedPrice}`;
}
