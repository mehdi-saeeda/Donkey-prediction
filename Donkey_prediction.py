def get_responses(n):
    responses = {}
    for i in range(n):
        try:
            line = input("Please enter a pair of words (first word and second word separated by space): ").split()
            if len(line) != 2:
                print("Error: Each word pair must contain exactly two words.")
                return {}
            first_word = line[0]
            second_word = line[1]
            responses[first_word] = second_word
        except Exception as e:
            print(f"Error: {e}")
            return {}
    return responses
def process_questions(responses):
    try:
        questions = input("Please enter your questions (separated by space): ").split()
        result = []
        for j in questions:
            if j in responses:
                result.append(responses[j] + " kachal!")
            else:
                result.append("kachal!")
        return result
    except Exception as e:
        print(f"Error while processing questions: {e}")
        return []
def main():
    try:
        n, m = input("Please enter the number of word pairs and number of questions (separated by space): ").split()
        n = int(n)
        m = int(m)

        if not (1 <= n <= 1000) or not (1 <= m <= 1000):
            print("Error: n and m must be between 1 and 1000.")
            return

        responses = get_responses(n)

        if not responses:
            return

        result = process_questions(responses)
        print(" ".join(result))

    except ValueError as e:
        print(f"Error: Invalid input. Please enter the numbers correctly.")

main()
