function togglemenu() {
    const el = document.getElementsByClassName("nav-sections")[0];

    const currentDisplay = window.getComputedStyle(el).display;

    if (currentDisplay === 'none'){
        el.style.display = 'flex';
    } else {
        el.style.display = 'none';
    }
}

