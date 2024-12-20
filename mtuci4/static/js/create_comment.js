document.addEventListener("DOMContentLoaded", () => {
    const create_forms = document.querySelectorAll(".create-comment-form");


    create_forms.forEach(function (form) {

        const textarea = form.querySelector(".adaptive-textarea");
        const url = form.action;
        const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
        const type = form.dataset.parentType;
        const parent_id = form.dataset.parentId;

        form.addEventListener("submit", (event) => {
            event.preventDefault();

            const text = textarea.value;
            const formData = new FormData();

            formData.append('type', type);
            formData.append('id', parent_id);
            formData.append('text', text);

            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.code == 200) {
                        location.reload();
                    }
                })
                .catch((error) => console.error(error));
        });
    });
});
