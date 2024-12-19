document.addEventListener("DOMContentLoaded", () => {
    const create_forms = document.querySelectorAll(".create-comment-form");
    

    create_forms.forEach(function (form) {
        
        const textarea = form.querySelector(".adaptive-textarea");
        const url = form.action;
        const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
        const type = form.dataset.parentType;

        form.addEventListener("submit", (event) => {
            event.preventDefault();

            // console.log(form);
            // console.log(textarea);
            console.log(type);

            const text = textarea.value;
            


            
        });
    });
});
