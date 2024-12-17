document.addEventListener("DOMContentLoaded", function () {
    const voteForms = document.querySelectorAll(".vote-form");

    voteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const url = form.action;
            const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
            const postId = form.dataset.postId || form.dataset.commentId;
            const voteType = form.querySelector(".vote-button").dataset.voteType;
            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/json",
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    if (data.upvotes !== undefined && data.downvotes !== undefined) {
                        const parentElement = form.parentNode;
                        const upvoteButton = parentElement.querySelector(".vote-button[data-vote-type='up']");
                        const downvoteButton = parentElement.querySelector(".vote-button[data-vote-type='down']");

                        parentElement.querySelector(".upvotes").textContent = `Upvotes: ${data.upvotes}`;
                        parentElement.querySelector(".downvotes").textContent = `Downvotes: ${data.downvotes}`;

                        if (data.removed) {
                            upvoteButton.dataset.selected = false;
                            downvoteButton.dataset.selected = false;
                        } else {
                            upvoteButton.dataset.selected = voteType === "up";
                            downvoteButton.dataset.selected = voteType === "down";
                        }

                        upvoteButton.classList.toggle("selected", upvoteButton.dataset.selected === "true");
                        downvoteButton.classList.toggle("selected", downvoteButton.dataset.selected === "true");
                    } else {
                        alert(data.error);
                    }
                })
                .catch((error) => console.error(error));
        });
    });
});


