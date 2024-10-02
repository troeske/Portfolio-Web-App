/* re-used from CodeStar project */
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("ts-btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated registration ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific registration.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let username = e.target.getAttribute("data-user");
        deleteConfirm.href = `delete_client/${username}`;
        deleteModal.show();
    });
}