document.addEventListener("DOMContentLoaded", () => {
    const textareas = document.querySelectorAll(".adaptive-textarea");

    const adjustHeight = (textarea) => {
      textarea.style.height = "auto"; // Сбрасываем высоту
      textarea.style.height = `${textarea.scrollHeight}px`; // Устанавливаем по содержимому
    };
  
    textareas.forEach(function (textarea) {
      textarea.addEventListener("input", (event) => {
          
        adjustHeight(textarea);

      });
    });
  
});