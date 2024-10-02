// ตัวแปรเพื่อเก็บ popup หน้าแรก
let popupWindow1;

document.getElementById('edit_button').addEventListener('click', function() {
    if (!popupWindow1 || popupWindow1.closed) {
        const popupWidth = 900;
        const popupHeight = 600;

        // คำนวณตำแหน่งสำหรับหน้าต่าง Popup ให้อยู่ตรงกลางหน้าจอ
        const left = Math.max(0, (window.screen.availWidth - popupWidth) / 2);
        const top = Math.max(0, (window.screen.availHeight - popupHeight) / 2);

        popupWindow1 = window.open('popup_sale_record_1.html', 'popupWindow1', `width=${popupWidth},height=${popupHeight},top=${top},left=${left},resizable=0,scrollbars=yes`);
    } else {
        popupWindow1.focus();
    }
    window.close();
});

document.getElementById('cancel_button').addEventListener('click', function() {
    window.close();
});

document.getElementById('submit_button').addEventListener('click', function() {
    window.close();
});
