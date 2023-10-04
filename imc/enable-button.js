const inputs = document.querySelectorAll('input');
const btn = document.querySelector('button');

//button is enabled only when both inputs are filled
for (let input of inputs) {
    input.addEventListener('input', e => {
        if (inputs[0].value === '' || inputs[1].value === '') {
            btn.disabled = true;
        } else {
            btn.disabled = false;
        }
    });
}
