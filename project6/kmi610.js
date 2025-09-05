document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const showRegisterFormBtn = document.getElementById('showRegisterFormBtn');
    const showLoginFormLink = document.getElementById('showLoginFormLink');

    // Function to show/hide forms
    function showForm(formToShow, formToHide) {
        formToShow.classList.remove('hidden');
        formToHide.classList.add('hidden');
    }

    // Event listener for "Create New Account" button
    showRegisterFormBtn.addEventListener('click', (e) => {
        e.preventDefault();
        showForm(registerForm, loginForm);
    });

    // Event listener for "Already have an account? Log In" link
    showLoginFormLink.addEventListener('click', (e) => {
        e.preventDefault();
        showForm(loginForm, registerForm);
    });

    // Handle Login Form Submission
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevent default form submission

        const emailPhone = document.getElementById('loginEmailPhone').value;
        const password = document.getElementById('loginPassword').value;

        // Basic validation (you'll need more robust validation and backend interaction)
        if (emailPhone && password) {
            console.log('Login attempt:');
            console.log('Email/Phone:', emailPhone);
            console.log('Password:', password);
            alert('Login button clicked! (This is a demo. No actual login is performed.)');
            // In a real application, you would send this data to a server for authentication.
        } else {
            alert('Please enter your email/phone and password.');
        }
    });

    // Handle Register Form Submission
    registerForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevent default form submission

        const registerEmail = document.getElementById('registerEmail').value;
        const registerPhone = document.getElementById('registerPhone').value;
        const registerPassword = document.getElementById('registerPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        // Basic validation (you'll need more robust validation and backend interaction)
        if (registerEmail && registerPassword && confirmPassword) {
            if (registerPassword !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }
            console.log('Register attempt:');
            console.log('Email:', registerEmail);
            console.log('Phone:', registerPhone);
            console.log('Password:', registerPassword);
            alert('Register button clicked! (This is a demo. No actual registration is performed.)');
            // In a real application, you would send this data to a server to create a new account.
            // After successful registration, you might redirect them or log them in.
            showForm(loginForm, registerForm); // Optionally, go back to login after registration
        } else {
            alert('Please fill in all required fields for registration.');
        }
    });
});