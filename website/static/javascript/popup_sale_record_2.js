function closePopup2() {
    window.parent.closePopup();
}

function goBackToMainPage() {
    closePopup2();
    window.parent.location.reload();
}

function checkQuantity(input) {
    if (input.value.length > 3) {
        input.value = input.value.slice(0, 3);
    }else if (input.value < 1) {
        input.value = 1;
    }
}

function preventRemoveSymbol(input) {
    const originalValue = "฿ ";
    if (!input.value.startsWith("฿")) {
        input.value = originalValue;
    } else if (input.value.length < originalValue.length) {
        input.value = originalValue;
    }
}

function submitPrice(input, id) {
    const priceValue = input.value.replace('฿', '').trim(); // Get the price value without the symbol
    if (priceValue !== "") {
        // Optionally, do some validation here if needed
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = "/cart/edit/" + id + "/price/" + encodeURIComponent(priceValue);

        // Create a hidden input for price (optional since it's in the URL)
        const priceInput = document.createElement('input');
        priceInput.type = 'hidden';
        priceInput.name = 'price'; // Name of the parameter
        priceInput.value = priceValue; // Set the value

        // Append the price input to the form (optional)
        form.appendChild(priceInput);
        document.body.appendChild(form);
        form.submit();
    }
}

function submitValue(input, id) {
    const quantityValue = input.value; // Get the quantity value directly
    if (quantityValue !== "") {
        // Create a new form
        const form = document.createElement('form');
        form.method = 'POST';  // Use POST method
        form.action = "/cart/edit/" + id + "/value/" + encodeURIComponent(quantityValue);

        // Create a hidden input for quantity (optional since it's in the URL)
        const quantityInput = document.createElement('input');
        quantityInput.type = 'hidden';
        quantityInput.name = 'value'; // Name of the parameter
        quantityInput.value = quantityValue; // Set the value

        // Append the quantity input to the form (optional)
        form.appendChild(quantityInput);
        document.body.appendChild(form);
        form.submit(); // Submit the form
    }
}