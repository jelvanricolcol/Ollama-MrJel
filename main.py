def prompt_jelvan_ai(prompt, model="jelvan-ai-model"):
    # Example: Replace this with your API call to Jelvan Ai backend if needed
    print(f"[Jelvan Ai] Sending prompt to model '{model}':")
    print(prompt)
    # Fake response for CLI demo
    return "Jelvan Ai says: This is a sample response."

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Jelvan Ai: ")
    print("Sending to Jelvan Ai...")
    response = prompt_jelvan_ai(user_prompt)
    print(response)