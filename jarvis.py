import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from your environment

SYSTEM = "You are Jarvis, a witty and helpful AI assistant like Tony Stark's Jarvis. Keep replies short."
history = []

while True:
    user = input("You: ")
    if user.lower() in ("exit", "quit"):
        break
    history.append({"role": "user", "content": user})
    resp = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=500,
        system=SYSTEM,
        messages=history,
    )
    reply = resp.content[0].text
    history.append({"role": "assistant", "content": reply})
    print("Jarvis:", reply)
