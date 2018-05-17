class Message:
    BASIC = "Press i to input command"

    SEARCH_FAILED = "No files found."

    @staticmethod
    def SEARCH(search_term):
        return "Results for: " + search_term + ". Press Esc to exit."
