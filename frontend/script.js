function toggleChat() {
    let chat = document.getElementById("chatbox");
    chat.style.display = chat.style.display === "flex" ? "none" : "flex";
}

async function send() {

    let input = document.getElementById("input");
    let message = input.value;

    let messages = document.getElementById("messages");

    messages.innerHTML += `<p><b>You:</b> ${message}</p>`;

    const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await res.json();

    messages.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;

    input.value = "";
}
