import re

def extract_data(transcription):
    text = " ".join(transcription)
    policy_number = re.search(r"C\d{9,}", text)
    due_date = re.search(r"\d{1,2} ?जुलाई ?\d{4}", text)
    amount_due = re.search(r"\d{2,3},?\d{3}", text)
    return {
        "policy_number": policy_number.group() if policy_number else None,
        "due_date": due_date.group() if due_date else None,
        "amount_due": amount_due.group() if amount_due else None
    }
