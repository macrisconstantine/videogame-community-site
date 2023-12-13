// script.js
document.getElementById('custom-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        var userInput = this.value;
    }
});