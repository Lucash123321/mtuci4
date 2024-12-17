document.addEventListener("DOMContentLoaded", function () {
    const voteForms = document.querySelectorAll(".vote-form");

    function updateVoteCounts(form, upvotes, downvotes) {
        form.querySelector(".upvotes").textContent = `${upvotes}`;
        form.querySelector(".downvotes").textContent = `${downvotes}`;
    }

    voteForms.forEach(function (form) {
        const url = form.action; // Получаем URL для запроса (из атрибута action формы)
        
        // Получаем текущие данные о голосах
        fetch(url, {
            method: "GET", // Используем GET для запроса текущих данных
            headers: {
                "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
            }
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data); // Логируем данные для проверки
            // Обновляем количество голосов
            updateVoteCounts(form, data.upvotes, data.downvotes);
        })
        .catch((error) => console.error('Ошибка загрузки данных:', error));
    });

    voteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const url = form.action;
            const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
            const voteType = event.submitter.value;

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
                    console.log(data);
                    form.querySelector(".upvotes").textContent = `${data.upvotes}`;
                    form.querySelector(".downvotes").textContent = `${data.downvotes}`;
                })
                .catch((error) => console.error(error));
        });
    });
});


