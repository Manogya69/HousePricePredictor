//new

// Define the price values for each entity
const priceValues = {
  apartment: 500000,
  house: 800000,
  condo: 600000,
  townhouse: 700000,
  bedrooms: 10000,
  // Add more entities and their corresponding prices here
  // ...
  pool: 15000,
  gym: 10000,
  fireplace: 5000,
  yard: 8000,
  garage: 12000,
};

let predictedPrice = 0; // Initial predicted price
const predictedPriceElement = document.getElementById("predicted-price");

// Function to update the predicted price
function updatePredictedPrice() {
  predictedPrice = 0; // Reset the predicted price
  const typeInput = document.getElementById("type");
  const selectedType = typeInput.value;
  predictedPrice += priceValues[selectedType] || 0;

  const bedroomsInput = document.getElementById("bedrooms");
  console.log(bedroomsInput);
  const selectedBedrooms = parseInt(bedroomsInput.value);
  predictedPrice += priceValues.bedrooms * selectedBedrooms;

  const budgetInput = document.getElementById("budget");
  const budgetValue = budgetInput.value.trim();
  const budgetAmount = parseFloat(budgetValue.replace(/[^\d.]/g, ""));
  if (!isNaN(budgetAmount)) {
    predictedPrice += budgetAmount;
  }

  const locationInput = document.getElementById("location");
  const selectedLocation = locationInput.value.trim();
  // Add any calculations based on location, if needed

  const amenitiesInputs = document.querySelectorAll(
    "input[name='amenities']:checked"
  );
  amenitiesInputs.forEach(function (input) {
    const selectedAmenity = input.value;
    predictedPrice += priceValues[selectedAmenity] || 0;
  });

  predictedPriceElement.textContent = "$" + predictedPrice.toLocaleString();
}
document.addEventListener("DOMContentLoaded", function () {
  // Add event listeners to input elements
  const typeInput = document.getElementById("type");
  typeInput.addEventListener("change", updatePredictedPrice);

  //   const bedroomsInput = document.getElementById("bedrooms");
  //   bedroomsInput.addEventListener("input", updatePredictedPrice);

  //   const budgetInput = document.getElementById("budget");
  //   budgetInput.addEventListener("input", updatePredictedPrice);

  //   const locationInput = document.getElementById("location");
  //   locationInput.addEventListener("input", updatePredictedPrice);

  const amenitiesInputs = document.querySelectorAll("input[name='amenities']");
  amenitiesInputs.forEach(function (input) {
    input.addEventListener("change", updatePredictedPrice);
  });
});
