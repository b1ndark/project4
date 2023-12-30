// sendMail function to send email using emailJS where I have set auto reply aswell. from Code institue
function sendMail(contactForm) {
    // collects the values from the form
    emailjs.send('service_nxryx3l', 'typerforum', {
        'from_name': contactForm.name.value,
        'from_subject': contactForm.subject.value,
        'from_email': contactForm.emailaddress.value,
        'from_message': contactForm.message.value
    })
    .then(
        function(response) {
            console.log('SUCCESS', response); // Display a notification to the User 
            document.getElementById('alert-success').style.display = 'block';
            setTimeout(function () {
                window.location.reload();
            }, 3500); // Refreshes the page after 3.5 seconds, also notification disappears
        },
        function (response) {
            console.log('FAILED', response); // Display a notification to the User 
            document.getElementById('alert-failed').style.display = 'block';
            setTimeout(function () {
                window.location.reload();
            }, 3500); // Refreshes the page after 3.5 seconds, also notification disappears
        }
    );
    // to prevent the page from refreshing
    return false;
}


// SetTimeOut to dismiss automatically the messages after 3.5 seconds with the help of Code Institute Django Blog tutorial
setTimeout(function () {
    let messages = document.getElementById('alert-msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3500);