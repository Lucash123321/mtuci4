document.addEventListener("DOMContentLoaded", () => {
    const delete_forms = document.querySelectorAll(".edit-comment-form");

    // delete_forms.forEach(function (form) {
    //     form.addEventListener("submit", (event) => {
    //         event.preventDefault();
            
    //         const url = form.action;
    //         const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
    //         const itemToChange = form.parentElement.parentElement;

    //         itemToDelete.remove();

    //         fetch(url, {
    //             method: "POST",
    //             headers: {
    //                 "X-CSRFToken": csrfToken,
    //             }
    //         })
    //             .then((response) => response.json())
    //             .then((data) => {
    //                 console.log(data)
    //             })
    //             .catch((error) => console.error(error));
    //     });
    // });
});
