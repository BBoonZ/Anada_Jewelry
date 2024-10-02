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

// ปุ่ม Next เปิด popup หน้า 2
let popupWindow2;

document.getElementById('next_button').addEventListener('click', function() {
    const popupWidth = 900;
    const popupHeight = 600;

    // คำนวณตำแหน่งสำหรับหน้าต่าง Popup ให้อยู่ตรงกลางหน้าจอ
    const left = Math.max(0, (window.screen.availWidth - popupWidth) / 2);
    const top = Math.max(0, (window.screen.availHeight - popupHeight) / 2);

    popupWindow2 = window.open('popup_sale_record_2.html', 'popupWindow2', `width=${popupWidth},height=${popupHeight},top=${top},left=${left},resizable=0,scrollbars=yes`);
    window.close();
});
