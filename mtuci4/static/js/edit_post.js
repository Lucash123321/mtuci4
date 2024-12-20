document.addEventListener("DOMContentLoaded", () => {
    const show_buttons = document.querySelectorAll(".show-edit-elements");
    const edit_forms = document.querySelectorAll(".edit-post-form");

    // console.log(show_buttons);

    show_buttons.forEach(function (button) {
        const title_to_hide = button.parentElement.parentElement.querySelector(".post-header h2");
        const text_to_hide = button.parentElement.parentElement.querySelector(".post-text p");
        const input_to_show = button.parentElement.parentElement.querySelector(".adaptive-title-input");
        const textarea_to_show = button.parentElement.parentElement.querySelector(".adaptive-textarea");
        const button_to_show = button.parentElement.parentElement.querySelector(".submit-button");

        console.log(title_to_hide);
        console.log(text_to_hide);
        console.log(input_to_show);
        console.log(textarea_to_show);
        console.log(button_to_show);

        button.addEventListener("click", (event) => {
            event.preventDefault();
            title_to_hide.classList.toggle("hidden");
            text_to_hide.classList.toggle("hidden");
            input_to_show.classList.toggle("hidden");
            textarea_to_show.classList.toggle("hidden");
            button_to_show.classList.toggle("hidden");
        });
    });




    edit_forms.forEach(function (form) {
        const title_to_change = form.parentElement.querySelector(".post-header h2");
        const text_to_change = form.parentElement.querySelector(".post-text p");
        const input = form.querySelector(".adaptive-title-input");
        const textarea = form.querySelector(".adaptive-textarea");
        const button_to_hide = form.querySelector(".submit-button");
        const url = form.action;
        const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;

        form.addEventListener("submit", (event) => {
            event.preventDefault();
            console.log(title_to_change);
            console.log(text_to_change);
            console.log(textarea);
            console.log(button_to_hide);
            title_to_change.textContent = input.value;
            text_to_change.textContent = textarea.value;
            title_to_change.classList.toggle("hidden");
            text_to_change.classList.toggle("hidden");
            input.classList.toggle("hidden");
            textarea.classList.toggle("hidden");
            button_to_hide.classList.toggle("hidden");

            const formData = new FormData();
            formData.append('title', input.value);
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
