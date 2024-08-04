const checkbox = document.querySelector(".theme-switch__checkbox");

checkbox.addEventListener('change', function() {
    if (this.checked) {
        document.body.style.backgroundColor = "#212121";
    } else {
        document.body.style.backgroundColor = "#e8e8e8";
    }
});