function calculatePredictedPrice(formData) {
  let predictedPrice = 0;

  //Logic for Price Prediction
  
  // For House
  if (formData.houseType === "apartment") {
    predictedPrice += 50000; 
  } else if (formData.houseType === "house") {
    predictedPrice += 250000; 
  } else if (formData.houseType === "mansion") {
    predictedPrice += 500000; 
  }
   // For house price range
   if (formData.housePrice === "cheap") {
    predictedPrice -= 20000; // Extra discount for a cheap house
  } else if (formData.housePrice === "normal") {
    predictedPrice += 0; // No additional cost for normal house.
  }  else if (formData.housePrice === "above-average") {
    predictedPrice += 50000; // Extra cost  for an above-average house
  } else if (formData.housePrice === "luxury") {
    predictedPrice += 100000; // Extra cost for a luxury house
  }

  // For Location
  if (formData.location === "cheapNeighborhood") {
    predictedPrice -= 25000; // discount for cheap neighborhood
  } else if (formData.location === "greatViewLocation") {
    predictedPrice += 50000; // premium for a great view location
  } else if (formData.location === "richNeighborhood") {
    predictedPrice += 100000; // premium for a rich neighborhood
  }

  // For amenities
  const selectedAmenities = formData.amenities || []; // Default to an empty array if amenities is undefined
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


// Function to update the predicted price element
function updatePredictedPrice(formData) {
  const predictedPrice = calculatePredictedPrice(formData);
  const predictedPriceElement = document.getElementById("predicted-price");
  predictedPriceElement.textContent = `Predicted Price: Rs ${predictedPrice}`;
}
