# A simple script to demonstrate Python basics for ML data prep
def calculate_accuracy(correct_predictions, total_predictions):
    if total_predictions == 0:
        return 0
    return (correct_predictions / total_predictions) * 100

# Simulated ML model evaluation
total_test_images = 150
correct_guesses = 132

accuracy = calculate_accuracy(correct_guesses, total_test_images)

print(f"Model evaluated on {total_test_images} images.")
print(f"Model Accuracy: {accuracy:.2f}%")
