function setPreferences(element){
    const form = document.querySelector('form');

    if (form.hidden = true) {
        form.hidden = false;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = setPreferences;
});