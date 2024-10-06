function closePopup2() {
    window.parent.closePopup();
}

function goBackToMainPage() {
    closePopup2();
    window.parent.location.reload();
}
