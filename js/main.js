const tooltip = document.querySelector(".tooltip");
const text = document.querySelector(".tooltip").getAttribute("data-copy");
const tooltipText = document.querySelector(".tooltip-text");

const copyContent = async () => {
    try {
        await navigator.clipboard.writeText(text);
        tooltipText.textContent = "Email copiado!";
    } catch (err) {
        console.error("Failed to copy: ", err);
        tooltipText.textContent = "Falha ao copiar";
    }
};

tooltip.addEventListener("click", copyContent);
