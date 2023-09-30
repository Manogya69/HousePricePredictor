function calculatePredictedPrice(user_preferences) {
  let predictedPrice = 0;

  //Logic for Price Prediction
  
  // For House
  if (user_preferences.houseType === "apartment") {
    predictedPrice += 50000; 
  } else if (user_preferences.houseType === "house") {
    predictedPrice += 250000; 
  } else if (user_preferences.houseType === "mansion") {
    predictedPrice += 500000; 
  }
   // For house price range
   if (user_preferences.housePrice === "cheap") {
    predictedPrice -= 20000; // Extra discount for a cheap house
  } else if (user_preferences.housePrice === "normal") {
    predictedPrice += 0; // No additional cost for normal house.
  }  else if (user_preferences.housePrice === "above-average") {
    predictedPrice += 50000; // Extra cost  for an above-average house
  } else if (user_preferences.housePrice === "luxury") {
    predictedPrice += 100000; // Extra cost for a luxury house
  }

  // For Location
  if (user_preferences.location === "cheapNeighborhood") {
    predictedPrice -= 25000; // discount for cheap neighborhood
  } else if (user_preferences.location === "greatViewLocation") {
    predictedPrice += 50000; // premium for a great view location
  } else if (user_preferences.location === "richNeighborhood") {
    predictedPrice += 100000; // premium for a rich neighborhood
  }

  // For amenities
  const selectedAmenities = user_preferences.amenities || []; // Default to an empty array if amenities is undefined
  if (selectedAmenities.includes("pool")) {
    predictedPrice += 15000; // Example price increase for a pool
  }
  if (selectedAmenities.includes("gym")) {
    predictedPrice += 10000; // Example price increase for a gym
  }
  if (selectedAmenities.includes("fireplace")) {
    predictedPrice += 8000; // Example price increase for a fireplace
  }
  if (selectedAmenities.includes("yard")) {
    predictedPrice += 12000; // Example price increase for a yard
  }
  if (selectedAmenities.includes("garage")) {
    predictedPrice += 10000; // Example price increase for a garage
  }

  return predictedPrice;
}

// Define a function to update the predicted price in the HTML
function updatePredictedPrice(userPreferences) {
  const predictedPrice = calculatePredictedPrice(userPreferences);
  const predictedPriceElement = document.getElementById("predicted-price");

  if (predictedPriceElement) {
      predictedPriceElement.textContent = `Predicted Price: Rs ${predictedPrice}`;
  }
}