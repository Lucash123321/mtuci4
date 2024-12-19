document.addEventListener("DOMContentLoaded", () => {
    const show_buttons = document.querySelectorAll(".show-edit-elements");
    const edit_forms = document.querySelectorAll(".edit-comment-form");

    // console.log(show_buttons);

    show_buttons.forEach(function (button) {
        const text_to_hide = button.parentElement.querySelector(".comment-text");
        const textarea_to_show = button.parentElement.querySelector(".adaptive-textarea");
        const button_to_show = button.parentElement.querySelector(".submit-button");

        button.addEventListener("click", (event) => {
            text_to_hide.classList.toggle("hidden");
            textarea_to_show.classList.toggle("hidden");
            button_to_show.classList.toggle("hidden");
            
        });
    });

    edit_forms.forEach(function (form) {
        
        const text_to_change = form.querySelector(".comment-text");
        const textarea = form.querySelector(".adaptive-textarea");
        const button_to_hide = form.querySelector(".submit-button");
        const url = form.action;
        const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;

        form.addEventListener("submit", (event) => {
            event.preventDefault();

            // console.log(text_to_change);
            // console.log(textarea);
            // console.log(button_to_hide);
            
            text_to_change.textContent = textarea.value;
            text_to_change.classList.toggle("hidden");
            textarea.classList.toggle("hidden");
            button_to_hide.classList.toggle("hidden");

            const formData = new FormData();
            formData.append('text', textarea.value);


            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                })
                .catch((error) => console.error(error));
        });
    });
});
