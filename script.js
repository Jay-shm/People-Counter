const increment = document.getElementById('increment');
const decrement = document.getElementById('decrement');
const count = document.getElementById('count');

let counter = 0;

function updatecountdisplay() {
    count.innerText = counter;
    count.classList.add('bump');
    setTimeout(() => {
        count.classList.remove('bump');
    }, 200);
}

increment.addEventListener('click', () => {
    counter++;
    updatecountdisplay();
});

decrement.addEventListener('click', () => {
    if(counter > 0) {
        counter--;
    }
    updatecountdisplay();
});