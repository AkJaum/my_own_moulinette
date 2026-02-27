from app.tests import test_ex00, test_ex01

def run_all_tests(base):

    exercises = [
        ("ex00", test_ex00),
        ("ex01", test_ex01),
    ]

    results = []

    for name, test in exercises:
        success = test(base)

        results.append({
            "exercise": name,
            "success": success
        })

        if not success:
            break

    return results
