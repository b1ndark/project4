
// SetTimeOut to dismiss automatically the messages after 3.5 seconds with the help of Code Institute Django Blog tutorial
setTimeout(function () {
    let messages = document.getElementById('alert-msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3500);