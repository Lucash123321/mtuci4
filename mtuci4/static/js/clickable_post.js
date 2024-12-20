document.addEventListener("DOMContentLoaded", () => {
    const posts = document.querySelectorAll(".clickable-post");

    posts.forEach(function (post) {
        post.addEventListener("click", (event) => {
            let tagName = event.target.tagName.toLowerCase();
            if (tagName == "input" || tagName == "textarea") event.preventDefault();
        });
    });
});
