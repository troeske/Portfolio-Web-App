document.addEventListener('DOMContentLoaded', function () {
    // For the next and previous buttons on the image carousels
    const carousels = document.querySelectorAll(".ts-list"); // Select all carousels

    carousels.forEach(function(list) {
        const sectionId = list.id.split('-')[2]; // Extract the section ID from the list's ID
        const item = list.querySelector(".ts-item");

        // Ensure item is not null and has been loaded
        if (item) {
            const itemWidth = item.offsetWidth;
            const listWidth = list.clientWidth;
            const totalItemsWidth = itemWidth * list.children.length;

            // Show buttons only if scrolling is necessary
            const buttonsContainer = document.querySelector(`.ts-carousel-buttons[data-section-id="${sectionId}"]`);
            if (totalItemsWidth > listWidth) {
                buttonsContainer.style.display = 'flex';
            }

            function handleClick(direction) {
                // Get current scroll position
                let currentScroll = list.scrollLeft;
                const maxScroll = list.scrollWidth - list.clientWidth; // Calculate max scroll distance

                if (direction === "previous") {
                    list.scrollTo({
                        left: Math.max(currentScroll - itemWidth, 0),
                        behavior: "smooth"
                    });
                } else {
                    list.scrollTo({
                        left: Math.min(currentScroll + itemWidth, maxScroll),
                        behavior: "smooth"
                    });
                }
            }

            // Attach event listeners to the respective buttons for this section
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