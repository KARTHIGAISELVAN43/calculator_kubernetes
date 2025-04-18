let display = document.getElementById('display');

function appendToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

async function calculate() {
    try {
        const expression = display.value;
        const response = await fetch('http://localhost:5000/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression }),
        });
        const result = await response.json();
        if (result.error) {
            display.value = 'Error';
        } else {
            display.value = result.result;
        }
    } catch (error) {
        display.value = 'Error';
    }
}