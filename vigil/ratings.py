from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

def complement_rating_from(complements:list):
    return 96

def nonpairs_rating_from(nonpairs:list):
    return 96

def health_from(faults:list):
    return 96

def advise_perf(complements:list, nonpairs:list):
    return "Do something useful with your PID for once."

def advise_health(faults:list):
    result = model.invoke(
        input = f"""
        For an FRC Robot performing during a match,
        with this list of faults for the match: {[fault.title for fault in faults]},
        advise the team on what they should do to prevent this fault from occurring in future matches.
        Depending on the fault, provide appropriate recommendations.
    """
    )
    return result