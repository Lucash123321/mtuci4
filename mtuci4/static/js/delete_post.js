document.addEventListener("DOMContentLoaded", () => {
    const delete_forms = document.querySelectorAll(".delete-post-form");

    delete_forms.forEach(function (form) {
        form.addEventListener("submit", (event) => {
            event.preventDefault();

            const url = form.action;
            const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
            const itemToDelete = form.parentElement.parentElement.parentElement;

            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                }
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.code === 200) {
                    itemToDelete.remove();  // Remove UI element
                    // Optionally show a success message or update other elements
                } else if (data.code === 404) {
                    // Handle not found case or show a different message
                    console.error('Item not found.');
                }
            })
            .catch((error) => console.error(error));
        });
    });
});
