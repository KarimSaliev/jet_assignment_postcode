
//Declare the const variables from the document
const dropdown = document.querySelector('.dropdown');
const select = dropdown.querySelector('.select');
const caret = dropdown.querySelector('.caret');
const menu = dropdown.querySelector('.menu');
const options = dropdown.querySelectorAll('.menu li');
const grid_table = document.querySelector('.grid-table');


// Executes the logic on the 'click' event of the select element
select.addEventListener('click', () => {
    // Makes the caret rotate
    caret.classList.toggle('caret-rotate');
    // Opens the menu
    menu.classList.toggle('menu-open');
    // Hides the table with restaurant data if is populated to avoid overlap with droplist menu
    if (grid_table.style.display=='none' && document.querySelector('tbody').innerHTML.trim()!='') {
        grid_table.style.display='table'}
    else {
        grid_table.style.display='none';}
});

// Executes logic on 'click' events for droplisted options
options.forEach(option=>{
    option.addEventListener('click', ()=> {
        // Rotates the caret back after the option is chosen
        caret.classList.remove('caret-rotate');
        // Closes the menu after the option is chosen
        menu.classList.remove('menu-open');

    });
});




