document.addEventListener('DOMContentLoaded', function () {
    // For the next and previous button on the special offers carousel
    const list = document.querySelector(".ts-list");
    const item = document.querySelector(".ts-item");
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

        // lets attach these events to to buttons
        document.getElementById('previous-card').addEventListener('click', function() {
            handleClick('previous');
        });

        document.getElementById('next-card').addEventListener('click', function() {
            handleClick('next');
        });
    }
});