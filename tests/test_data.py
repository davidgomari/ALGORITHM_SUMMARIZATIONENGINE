TEST_CASES = [
    # --- Easy Cases (Short, clear topic) ---
    {
        "id": 1,
        "type": "easy",
        "text": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected.",
        "expected_len": 1
    },
    {
        "id": 2,
        "type": "easy",
        "text": "The sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma. The Sun radiates energy mainly as light, ultraviolet, and infrared radiation.",
        "expected_len": 1
    },
    
    # --- Medium Cases (Tech articles, News) ---
    {
        "id": 3,
        "type": "medium",
        "text": """Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals.
        The term "artificial intelligence" had previously been used to describe machines that mimic and display "human" cognitive skills that are associated with the human mind, such as "learning" and "problem-solving". This definition has since been rejected by major AI researchers who now describe AI in terms of rationality and acting rationally, which does not limit how intelligence can be articulated.""",
        "expected_len": 2
    },
    
    # --- Hard Cases (Complex vocabulary, ambiguous structure) ---
    {
        "id": 9,
        "type": "hard",
        "text": "Quantum superposition is a fundamental principle of quantum mechanics. It states that, much like waves in classical physics, any two (or more) quantum states can be added together ('superposed') and the result will be another valid quantum state; and conversely, that every quantum state can be represented as a sum of two or more other distinct states. Mathematically, it refers to a property of solutions to the Schrödinger equation; since the Schrödinger equation is linear, any linear combination of solutions will also be a solution.",
        "expected_len": 2
    },

    # --- Failure Case (Gibberish / Empty / Single word) ---
    {
        "id": 10,
        "type": "failure",
        "text": "Hello.", # Too short to summarize
        "expected_len": 0 # Should handle gracefully
    }
]