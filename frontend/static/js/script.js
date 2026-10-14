async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();

    // Prevent sending empty spaces
    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    // 1. Append the user's message to the chat
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    // Clear input field and auto-scroll immediately
    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // 2. Fetch the response from Flask backend (port 5000)
        let response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error(`Server returned status: ${response.status}`);
        }

        let data = await response.json();

        // Find the top emotion key if available
        let topEmotion = "Neutral";
        if (data.emotion && Object.keys(data.emotion).length > 0) {
            // Gets the emotion label with the highest score
            topEmotion = Object.entries(data.emotion).reduce((a, b) => a[1] > b[1] ? a : b)[0];
        }

        // 3. Append the bot's response along with analytics insights
        chatBox.innerHTML += `
            <div class="bot-message">
                <p>${data.response}</p>
                <div class="analysis-tag" style="font-size: 0.75em; color: #718096; margin-top: 8px; border-top: 1px dashed #e2e8f0; padding-top: 4px;">
                    📊 <b>Emotion:</b> ${topEmotion} |
                    🧠 <b>Assessment:</b> ${data.condition.condition} <span style="opacity: 0.7;">(${Math.round(data.condition.confidence * 100)}%)</span>
                </div>
            </div>
        `;

    } catch (error) {
        console.error("Error communicating with backend:", error);
        chatBox.innerHTML += `
            <div class="bot-message error-message" style="color: #e53e3e;">
                Oops! I'm having trouble connecting to my brain right now. Please ensure the backend server on port 5000 is up and running.
            </div>
        `;
    }

    // 4. Auto-scroll to show the new bot message
    chatBox.scrollTop = chatBox.scrollHeight;
}