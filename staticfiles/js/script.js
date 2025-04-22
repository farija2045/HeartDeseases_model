document.getElementById('predictBtn').addEventListener('click', async () => {
    const formData = {
      Age: parseFloat(document.getElementById('age').value),
      Gender: parseFloat(document.getElementById('gender').value),
      BloodPressure: parseFloat(document.getElementById('bloodPressure').value),
      Cholesterol: parseFloat(document.getElementById('cholesterol').value),
      HeartRate: parseFloat(document.getElementById('heartRate').value),
      QuantumPatternFeature: parseFloat(document.getElementById('quantumPatternFeature').value),
    };
  
    try {
      const response = await fetch('/predict', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        queryParams: new URLSearchParams(formData).toString(),
      });
  
      if (response.ok) {
        const data = await response.json();
        document.getElementById('result').textContent = `Prediction: ${data.prediction}`;
      } else {
        const error = await response.json();
        document.getElementById('result').textContent = `Error: ${error.error}`;
      }
    } catch (error) {
      document.getElementById('result').textContent = 'An unexpected error occurred.';
    }
  });