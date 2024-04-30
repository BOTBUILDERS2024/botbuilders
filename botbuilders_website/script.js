document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    var inputField = document.getElementById('userInput');
    var userInput = inputField.value;
    inputField.value = '';

    displayMessage(userInput, 'user');

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }) // Make sure this matches what your Flask expects
    })
    .then(response => response.json())
    .then(data => {
        // The key used here must match what your Flask route is sending back in the JSON response
        displayMessage(data.answer, 'bot'); 
    })
    .catch(error => {
        console.error('Error:', error);
        displayMessage('Error: Could not get a response from the server.', 'bot');
    });
}

function displayMessage(message, sender) {
    var conversation = document.getElementById('conversation');
    var newMessage = document.createElement('li');
    newMessage.textContent = message;
    newMessage.className = sender;
    conversation.appendChild(newMessage);
    conversation.scrollTop = conversation.scrollHeight; // Scroll to the bottom to show latest message
}
