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
                // Get current scroll position
                let currentScroll = list.scrollLeft;
                const maxScroll = list.scrollWidth - list.clientWidth; // Calculate max scroll distance

                // Check if the list is right-aligned
                const isRightAligned = list.classList.contains('ts-list-aligmnet-right');

                if (isRightAligned) {
                    // Reverse scroll direction for right-aligned lists
                    if (direction === "previous") {
                        // Scroll towards the right, moving left in the UI
                        list.scrollTo({
                            left: Math.min(currentScroll + itemWidth, maxScroll), // Ensure we don't scroll past max
                            behavior: "smooth"
                        });
                    } else {
                        // Scroll towards the left, moving right in the UI
                        list.scrollTo({
                            left: Math.max(currentScroll - itemWidth, 0), // Ensure we don't scroll past 0
                            behavior: "smooth"
                        });
                    }
                } else {
                    // Standard behavior for left-aligned lists
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
