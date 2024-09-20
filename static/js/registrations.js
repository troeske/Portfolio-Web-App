const approvalButtons = document.getElementsByClassName("btn-approve");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

alert("evenet listener working");

/*
 * Initializes edit functionality for the provided aproval buttons.
 * 
 * For aproval button in the `approvalButtons` collection:
 * - Retrieves the associated registration ID upon click.
 * - Sets the approved field to True
 * - Updates the submit button's text to "Approve".
 * ???:
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */

for (let button of approvalButtons) {
    button.addEventListener("click", (e) => {
        let client_id = e.target.getAttribute("data-registration_id");

        /* commentForm.setAttribute("action", `edit_comment/${commentId}`); */
    });
} 

/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let client_id = e.target.getAttribute("data-registration_id");
        console.log(client_id);
        deleteConfirm.href = `delete_client/${client_id}`;
        console.log(`delete_client/${client_id}`);
        deleteModal.show();
    });
}