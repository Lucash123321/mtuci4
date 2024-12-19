document.addEventListener("DOMContentLoaded", function () {

    const voteForms = document.querySelectorAll(".vote-form");

    function updateVoteCounts(form, upvotes, downvotes) {
        form.querySelector(".upvotes").textContent = `${upvotes}`;
        form.querySelector(".downvotes").textContent = `${downvotes}`;
    }

    voteForms.forEach(function (form) {
        const url = form.dataset.getUrl;
        
        fetch(url, {
            method: "GET",
            headers: {
                "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
            }
        })
        .then((response) => response.json())
        .then((data) => {
            updateVoteCounts(form, data.upvotes, data.downvotes);
            let user_vote = data.user_vote;
            let pressed_button;
            if (user_vote == "up") {
                pressed_button = form.querySelector("button[value='up']")
            } else if (user_vote == "down") {
                pressed_button = form.querySelector("button[value='down']")
            }

            if (pressed_button) pressed_button.classList.add("selected");
            
        })
        .catch((error) => console.error('Ошибка загрузки данных:', error));
    });
})