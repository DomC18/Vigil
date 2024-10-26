from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

def advise_perf(complements_data:list[list]):
    data = ""
    for complement_pairs in complements_data:
        data += f"Data Point: {complement_pairs[0]}, Complement: {complement_pairs[1]}, Percent Error: {complement_pairs[2]}%\n"
    result = model.invoke(
        input = f"""
        For an FRC Robot performing during a match,
        with this list of data point names and their complements as well as their percent error through the matches: {data},
        advise the team on how to improve the performance of their robot in future matches.
    """
    )
    return result

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