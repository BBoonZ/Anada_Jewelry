// ฟังก์ชันตัวนับใน popup แรก
let counterInput = document.getElementById('counter');
let counter = parseInt(counterInput.value);

// ปุ่มลดจำนวน
document.getElementById('decrement').addEventListener('click', function() {
    if (counter > 1) {  //ไม่ให้ค่าต่ำกว่า 1
        counter--;
        counterInput.value = counter;
    }
});

// ปุ่มเพิ่มจำนวน
document.getElementById('increment').addEventListener('click', function() {
    counter++;
    counterInput.value = counter;
});

// การพิมพ์แก้ไขจำนวนเอง
counterInput.addEventListener('input', function() {
    let newValue = parseInt(counterInput.value);
    if (!isNaN(newValue) && newValue >= 1) { //ไม่ให้ค่าต่ำกว่า 1
        counter = newValue;
    } else {
        counterInput.value = null;
    }
});

function closePopup() {
    window.parent.closePopup();
}

function goBackToMainPage() {
    closePopup();
    window.parent.location.reload();
}