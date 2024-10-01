document.addEventListener('DOMContentLoaded', function () {
    // For the next and previous buttons on the image carousels
    const carousels = document.querySelectorAll(".ts-list"); // Select all carousels

    carousels.forEach(function(list) {
        const sectionId = list.id.split('-')[2]; // Extract the section ID from the list's ID
        const item = list.querySelector(".ts-item");

        // Ensure item is not null and has been loaded
        if (item) {
            const itemWidth = item.offsetWidth;

            function handleClick(direction) {
                // Based on the direction we call `scrollBy` with the item width we got earlier
                if (direction === "previous") {
                    list.scrollBy({
                        left: -itemWidth,
                        behavior: "smooth"
                    });
                } else {
                    list.scrollBy({
                        left: itemWidth,
                        behavior: "smooth"
                    });
                }
            }

            // Attach event listeners to the respective buttons for this section proposed by ChatGpt
            const prevButton = document.querySelector(`.ts-button--previous[data-section-id="${sectionId}"]`);
            const nextButton = document.querySelector(`.ts-button--next[data-section-id="${sectionId}"]`);

            if (prevButton && nextButton) {
                prevButton.addEventListener('click', function() {
                    handleClick('previous');
                });

                nextButton.addEventListener('click', function() {
                    handleClick('next');
                });
            }
        }
    });
});
