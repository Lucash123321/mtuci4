document.addEventListener("DOMContentLoaded", function () {
    const voteForms = document.querySelectorAll(".vote-form");

    voteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const url = form.action;
            const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
            let pressed_button = event.submitter;
            const voteType = pressed_button.value;
            
            let other_button;
            if (voteType === "up") other_button = pressed_button.parentNode.querySelector("input[value='down']");
            else if (voteType === "down") other_button = pressed_button.parentNode.querySelector("input[value='up']");
            
            
            pressed_button.classList.toggle("selected");
            other_button.classList.remove("selected");

            const formData = new FormData();
            formData.append('vote_type', voteType);
            
            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    form.querySelector(".upvotes").textContent = `${data.upvotes}`;
                    form.querySelector(".downvotes").textContent = `${data.downvotes}`;
                })
                .catch((error) => console.error(error));
        });
    });
});


