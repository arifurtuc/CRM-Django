// Notication message timer

var alert_timeout = document.getElementById("alert-message-text");

// Set timeout to hide the alert message after 4 seconds
setTimeout(function()
    {
        alert_timeout.style.display = "none"
    }, 4000
);