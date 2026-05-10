def get_response(user_input):
    message = user_input.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Bot: Hello. Welcome to customer support. How can I help you?"

    if "product" in message or "item" in message:
        return "Bot: We offer laptops, headphones, keyboards, and mice."

    if "price" in message or "cost" in message:
        return "Bot: Prices depend on the product. Tell me the item name for details."

    if "order" in message or "track" in message:
        return (
            "Bot: Please share your order ID. "
            "A typical order is delivered in 3 to 5 days."
        )

    if "delivery" in message or "shipping" in message:
        return "Bot: Standard delivery takes 3 to 5 working days."

    if "return" in message or "refund" in message:
        return (
            "Bot: Products can be returned within 7 days "
            "if they are unused and in original condition."
        )

    if "payment" in message:
        return (
            "Bot: We accept UPI, debit card, "
            "credit card, and net banking."
        )

    if "contact" in message or "support" in message:
        return (
            "Bot: You can contact support at "
            "support@example.com or call 1800-123-456."
        )

    if message in ["bye", "exit", "quit", "thank you", "thanks"]:
        return "Bot: Thank you for visiting. Have a good day."

    return (
        "Bot: I can help with products, prices, orders, "
        "delivery, returns, payments, and support."
    )


def main():
    print("Elementary Chatbot for Customer Interaction")
    print("Type 'exit' to stop the chat.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)

        print(response)

        if user_input.lower().strip() in [
            "bye",
            "exit",
            "quit",
            "thank you",
            "thanks",
        ]:
            break


if __name__ == "__main__":
    main()