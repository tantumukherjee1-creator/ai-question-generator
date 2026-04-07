if __name__ == "__main__":
    from question_generator import QuestionGenerator

    generator = QuestionGenerator()
    questions = generator.generate_questions()
    for question in questions:
        print(question)