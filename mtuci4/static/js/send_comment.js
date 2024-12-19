document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.getElementById("adaptive-textarea");
  
    const adjustHeight = () => {
      textarea.style.height = "auto"; // Сбрасываем высоту
      textarea.style.height = `${textarea.scrollHeight}px`; // Устанавливаем по содержимому
    };
  
    textarea.addEventListener("input", adjustHeight);
  
    // Для предзаполненного текста (если нужно)
    adjustHeight();
  });