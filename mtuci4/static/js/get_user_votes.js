// console.log("Подключён скрипт")
// fetch('{% url 'topics:posts:get_user_vote' topic.slug post.topic_post_id  %}', {
//     method: 'POST', // Указываем метод запроса
//     headers: {
//       'Content-Type': 'application/json', // Указываем тип содержимого (если отправляем JSON)
//     },
//     body: JSON.stringify({ // Данные, которые отправляются на сервер
//       key1: 'value1',
//       key2: 'value2',
//     }),
//   })
//     .then(response => response.json()) // Преобразуем ответ в JSON
//     .then(data => console.log(data)) // Обрабатываем данные ответа
//     .catch(error => console.error('Ошибка:', error)); // Обрабатываем ошибки