
// <!-- feedback form project field show js start -->
document.addEventListener('DOMContentLoaded', function() {
    const testimonialTypeField = document.querySelectorAll('input[name="testimonial_type"]');
    const projectFieldWrapper = document.querySelector('.project-field');
    const generalLabel = document.querySelector('label[for="id_testimonial_type_0"]');
    const projectLabel = document.querySelector('label[for="id_testimonial_type_1"]');

    function toggleProjectField() {
        const selectedType = document.querySelector('input[name="testimonial_type"]:checked').value;
        if (selectedType === 'project') {
            projectFieldWrapper.style.display = 'block';
            projectLabel.style.color = '#27b674'; // Change project label color to green
            generalLabel.style.color = '#26362E'; // Reset general label color
        } else {
            projectFieldWrapper.style.display = 'none';
            generalLabel.style.color = '#27b674'; // Change general label color to blue
            projectLabel.style.color = '#26362E'; // Reset project label color
        }
    }

    testimonialTypeField.forEach(field => field.addEventListener('change', toggleProjectField));
    toggleProjectField();  // Initial call to set the correct state
});


// feedback/testimonial 3 cards continous silder js start || index page
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.three-card-slider-wrapper').forEach((sliderWrapper, index) => {
        let productCards = sliderWrapper.querySelectorAll('.three-card');
        const prevBtn = sliderWrapper.closest('.three-card-slider-container').querySelector('.prev-btn');
        const nextBtn = sliderWrapper.closest('.three-card-slider-container').querySelector('.next-btn');
        let currentIndex = 3; // Start from the first real card set after cloning
        let slideInterval;

        // Clone first and last few slides to create infinite looping effect
        for (let i = 0; i < 3; i++) {
            const firstClone = productCards[i].cloneNode(true);
            const lastClone = productCards[productCards.length - 1 - i].cloneNode(true);
            sliderWrapper.appendChild(firstClone);
            sliderWrapper.insertBefore(lastClone, sliderWrapper.firstChild);
        }

        // Update productCards to include cloned elements
        productCards = sliderWrapper.querySelectorAll('.three-card');

        // Adjust the initial position to be at the start of the actual cards
        const cardWidth = productCards[0].offsetWidth + 24; // Adjust margin here
        sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;

        function slideTo(index) {
            const translateXValue = -(index * cardWidth);
            sliderWrapper.style.transition = 'transform 0.5s ease-in-out';
            sliderWrapper.style.transform = `translateX(${translateXValue}px)`;
            currentIndex = index;

            // Handle looping effect
            sliderWrapper.addEventListener(
                'transitionend',
                () => {
                    if (index === 0) {
                        sliderWrapper.style.transition = 'none';
                        currentIndex = productCards.length - 6; // Real last set of cards
                        sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
                    } else if (index === productCards.length - 3) {
                        sliderWrapper.style.transition = 'none';
                        currentIndex = 3; // Real first set of cards
                        sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
                    }
                },
                { once: true }
            );
        }

        function nextSlide() {
            slideTo(currentIndex + 1);
        }

        function prevSlide() {
            slideTo(currentIndex - 1);
        }

        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);

        function startAutoSlide() {
            slideInterval = setInterval(nextSlide, 3000); // Adjust interval as needed
        }

        function stopAutoSlide() {
            clearInterval(slideInterval);
        }

        sliderWrapper.addEventListener('mouseover', stopAutoSlide);
        sliderWrapper.addEventListener('mouseout', startAutoSlide);

        startAutoSlide();
    });
});
