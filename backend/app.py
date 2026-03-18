from graph import pmgt_graph

print("PMGT Assistant is running... (type 'hi' to initiate conversation)")

while True:

    user_input = input("\nYou: ")

    response = pmgt_graph(user_input)

    print("\nPMGT Assistant:", response)
