const uploadBtn = document.getElementById('uploadBtn');
const imageInput = document.getElementById('imageInput');
const preview = document.getElementById('preview');
const result = document.getElementById('result');

uploadBtn.addEventListener('click', async () => {
    const file = imageInput.files[0];
    if (!file) {
        alert('Please select an image first.');
        return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = () => {
        preview.innerHTML = `<img src="${reader.result}" alt="Preview">`;
    };
    reader.readAsDataURL(file);

    // Prepare form data
    const formData = new FormData();
    formData.append('file', file);

    result.innerHTML = ' Analyzing...';

    try {
        const response = await fetch('http://127.0.0.1:8000/classify', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        if (data.category) {
            result.innerHTML = ` <strong>${data.category}</strong> <br> Confidence: ${(data.confidence * 100).toFixed(1)}%`;
        } else if (data.error) {
            result.innerHTML = `⚠️ Error: ${data.error}`;
        } else {
            result.innerHTML = `⚠️ Unexpected response`;
        }
    } catch (error) {
        result.innerHTML = ` Failed to connect to backend: ${error}`;
    }
});
