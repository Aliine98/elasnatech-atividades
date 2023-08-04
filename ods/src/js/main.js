window.addEventListener("scroll", () => {
    const headerMenu = document.querySelector(".header-menu");
    if (window.scrollY > 0) {
        headerMenu.classList.add("scrolled");
    } else {
        headerMenu.classList.remove("scrolled");
    }
});
