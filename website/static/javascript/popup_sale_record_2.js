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