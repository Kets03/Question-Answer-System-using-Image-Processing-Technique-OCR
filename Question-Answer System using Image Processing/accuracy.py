import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
correctly_detected = 12
incorrectly_detected = 4

# Calculate the accuracy percentage
total_images = correctly_detected + incorrectly_detected
accuracy_percentage = (correctly_detected / total_images) * 100

# Create a bar chart
categories = ['Correctly Detected', 'Incorrectly Detected']
values = [correctly_detected, incorrectly_detected]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=['green', 'red'])
plt.ylabel('Number of Words')
plt.title(f'Word Detection Accuracy\nAccuracy: {accuracy_percentage:.2f}%')

# Show the accuracy percentage on top of the bars
for i, v in enumerate(values):
    plt.text(i, v + 0.10, str(v), color='black', ha='center')

plt.show()
