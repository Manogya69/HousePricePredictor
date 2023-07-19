// const priceValues = {
//   houseType: {
//     trailer: 50000,
//     apartment: 100000,
//     house: 200000,
//     mansion: 500000,
//   },
//   priceType: {
//     cheap: -20000,
//     normal: 10000,
//     "above-average": 30000,
//     luxury: 50000,
//   },
//   location: {
//     cheapNeighborhood: -10000,
//     goodNeighborhood: 20000,
//     greatView: 30000,
//     richNeighborhood: 50000,
//   },
//   amenities: {
//     pool: 10000,
//     gym: 5000,
//     fireplace: 2000,
//     yard: 3000,
//     garage: 5000,
//   },
// };
const priceValues = {
  trailer: 10000,
  apartment: 100000,
  house: 500000,
  mansion: 1000000,
  cheap: 5000,
  normal: 10000,
  "above-average": 20000,
  luxury: 50000,
  cheapNeighborhood: -10000,
  goodNeighborhood: 20000,
  greatView: 30000,
  richNeighborhood: 50000,
  pool: 10000,
  gym: 5000,
  fireplace: 2000,
  yard: 3000,
  garage: 5000,
};

let cumulativePrice = 0; // Initial cumulative predicted price
const predictedPriceElement = document.getElementById("predicted-price");

// Function to update the predicted price
function updatePredictedPrice() {
  let predictedPrice = 0; // Reset predicted price

  const houseType = document.getElementById("houseType").value;
  const priceType = document.getElementById("priceType").value;
  const cheap = document.getElementById("cheap").checked;
  const normal = document.getElementById("normal").checked;
  const aboveAverage = document.getElementById("above-average").checked;
  const luxury = document.getElementById("luxury").checked;
  const pool = document.getElementById("pool").checked;
  const gym = document.getElementById("gym").checked;
  const fireplace = document.getElementById("fireplace").checked;
  const yard = document.getElementById("yard").checked;
  const garage = document.getElementById("garage").checked;

  if (houseType) {
    predictedPrice += priceValues.houseType[houseType];
  }
  if (priceType) {
    predictedPrice += priceValues.priceType[priceType];
  }
  if (cheap) {
    predictedPrice += priceValues.location.cheap;
  }
  if (normal) {
    predictedPrice += priceValues.location.goodNeighborhood;
  }
  if (aboveAverage) {
    predictedPrice += priceValues.location.greatView;
  }
  if (luxury) {
    predictedPrice += priceValues.location.richNeighborhood;
  }
  if (pool) {
    predictedPrice += priceValues.amenities.pool;
  }
  if (gym) {
    predictedPrice += priceValues.amenities.gym;
  }
  if (fireplace) {
    predictedPrice += priceValues.amenities.fireplace;
  }
  if (yard) {
    predictedPrice += priceValues.amenities.yard;
  }
  if (garage) {
    predictedPrice += priceValues.amenities.garage;
  }
  cumulativePrice += predictedPrice;
  predictedPriceElement.textContent = "$" + predictedPrice.toLocaleString();
}

// Get references to the buttons and the content container
const prevButtonSection = document.getElementById("prev");
const nextButtonSection = document.getElementById("next");
const ContentContainer = document.querySelector(".content-container");

// Event delegation to handle dynamic sections
ContentContainer.addEventListener("click", function (event) {
  const target = event.target;
  if (target.matches("#next")) {
    updatePredictedPrice();
  }
});

// Event delegation to handle previous sections
ContentContainer.addEventListener("click", function (event) {
  const target = event.target;
  if (target.matches("#prev")) {
    predictedPrice = 0; // Reset predicted price when going to the previous section
    predictedPriceElement.textContent = "$" + predictedPrice.toLocaleString();
  }
});
