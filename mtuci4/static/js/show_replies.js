document.addEventListener("DOMContentLoaded", () => {
    const showButtons = document.querySelectorAll(".comment-show-replies");

    
    const showReplies = (showButton) => {
        const container = showButton.parentElement.parentElement.parentElement;
        const replies = container.querySelector(".replies");

        replies.classList.toggle("hidden");
    }

    showButtons.forEach(function (showButton) {
        showButton.addEventListener("click", () => showReplies(showButton));
    });
});