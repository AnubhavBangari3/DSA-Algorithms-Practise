import React, { useState } from "react";

const Carousel = ({ items }) => {

  const [currentIndex, setCurrentIndex] = useState(0);

  const goToNext = () => {
    setCurrentIndex((prev) => (prev + 1) % items.length);
  };

  const goToPrevious = () => {
    setCurrentIndex((prev) => (prev - 1 + items.length) % items.length);
  };

  return (
    <div>
      <button onClick={goToPrevious}>Previous</button>

      <h2>{items[currentIndex]}</h2>

      <button onClick={goToNext}>Next</button>
    </div>
  );
};

function App() {
  const images = [1, 2, 3];

  return (
    <div>
      <Carousel items={images} />
    </div>
  );
}

export default App;