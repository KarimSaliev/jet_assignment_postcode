const dropdown = document.querySelector('.dropdown');
const select = dropdown.querySelector('.select');
const caret = dropdown.querySelector('.caret');
const menu = dropdown.querySelector('.menu');
const options = dropdown.querySelectorAll('.menu li');
const grid_table = document.querySelector('.grid-table');


select.addEventListener('click', () => {
    caret.classList.toggle('caret-rotate');
    menu.classList.toggle('menu-open');
    if (grid_table.style.display=='none' && document.querySelector('tbody').innerHTML.trim()!='') {
        grid_table.style.display='table'}
    else {
        grid_table.style.display='none';}
});

options.forEach(option=>{
    option.addEventListener('click', ()=> {
        caret.classList.remove('caret-rotate');
        menu.classList.remove('menu-open');

    });
});




