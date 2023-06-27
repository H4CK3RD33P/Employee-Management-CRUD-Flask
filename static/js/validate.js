const employeeForm = document.querySelector('#employee-form');
const nameInput = document.querySelector('#name');
const deptInput = document.querySelector('#dept');
const roleInput = document.querySelector('#role');
const salInput = document.querySelector('#sal');
const errorMessage = document.querySelector('#error-message');

employeeForm.addEventListener('submit', (event) => {
    // Regular expressions for validation
    const nameRegex = /^[a-zA-Z]+ [a-zA-Z]+$/;
    const deptRegex = /^[a-zA-Z]+$/;
    const roleRegex = /^[a-zA-Z1-9\-]+$/;
    const salRegex = /^\d+$/;

    // Array to store error messages
    let errors = [];

    // Check if name input is valid
    if (!nameRegex.test(nameInput.value)) {
        errors.push('Name must only contain letters.');
    }

    // Check if department input is valid
    if (!deptRegex.test(deptInput.value)) {
        errors.push('Department must only contain letters.');
    }

    // Check if role input is valid
    if (!roleRegex.test(roleInput.value)) {
        errors.push('Role must only contain letters.');
    }

    // Check if salary input is valid
    if (!salRegex.test(salInput.value) || parseInt(salInput.value) < 10000) {
        errors.push('Salary must be a number greater than or equal to 10000.');
    }

    // Prevent form from submitting if there are any errors
    if (errors.length > 0) {
        event.preventDefault();

        // Set error message and style
        errorMessage.innerHTML = errors.join('<br>');
        errorMessage.style.color = 'red';
    } else {
        // Clear error message if validation passes
        errorMessage.textContent = '';
    }
});
