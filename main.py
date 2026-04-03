students = [
    {"name": "Anna", "score": 85, "status": "passed"},
    {"name": "Ben", "score": 55, "status": "failed"},
    {"name": "Cara", "score": 90, "status": "passed"},
    {"name": "Dan", "score": 70, "status": "passed"},
    {"name": "Ella", "score": 40, "status": "failed"},
    {"name": "Finn", "score": 95, "status": "passed"}
]

def get_score_totals(students):
    passed_score_total = 0 
    failed_score_total = 0

    for s in students:
        if s ["status"] == "passed":
            passed_score_total = passed_score_total + s ["score"]

        else:
            failed_score_total = failed_score_total + s ["score"]

    return passed_score_total, failed_score_total

def get_student_counts(students):
    passed_count = 0 
    failed_count = 0 

    for s in students:
        if s ["status"] == "passed":
            passed_count = passed_count + 1

        else:
            failed_count = failed_count + 1

    return passed_count, failed_count

def get_flags(students):
    has_failing_student = False
    has_high_scorer = False

    for s in students:
        if s ["status"] == "failed":
            has_failing_student = True

        elif s ["score"] >= 90:
            has_high_scorer = True

    return has_failing_student, has_high_scorer

def get_class_status(students):
    passed_score_total, failed_score_total = get_score_totals(students)
    passed_count, failed_count = get_student_counts(students)

    if failed_count >= 2:
        return "Needs Attention"
    
    elif passed_score_total >= 300 and passed_count > failed_count:
        return "Excellent"
    
    else:
        return "Stable"
    
def generate_report(students):
    passed_score_total, failed_score_total = get_score_totals(students)
    passed_count, failed_count = get_student_counts(students)    
    has_failing_student, has_high_scorer = get_flags(students)
    status = get_class_status(students)

    print(f"Passed Score Total: {passed_score_total}")
    print(f"Failed Score Total: {failed_score_total}")
    print(f"Passed Count: {passed_count}")
    print(f"Failed Count: {failed_count}")
    print(f"Has Failing Student: {has_failing_student}")
    print(f"Has High Scorer: {has_high_scorer}")
    print(f"Class Status: {status}")

generate_report(students)