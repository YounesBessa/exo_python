import random

# Quote class 
class Quote:
    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return self.phrase

# RandomQuotes class
class RandomQuotes:
    def __init__(self):
        self.citations = [
            Quote("The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela"),
            Quote(
                "The way to get started is to quit talking and begin doing. -Walt Disney"),
            Quote(
                "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs"),
            Quote(
                "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt"),
            Quote("If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey")
        ]

    def random_quote(self):
        return random.choice(self.citations)

# Main function to test the class RandomQuotes
if __name__ == "__main__":
    citations_aleatoires = RandomQuotes()
    citation = citations_aleatoires.random_quote()
    print(citation)