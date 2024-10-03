// document.getElementById("dropdown_financial_id").addEventListener("click", function() {
//     const drop = document.getElementById("drop");
//     const dropdown_financial_id = document.getElementById("dropdown_financial_id");

//     if (drop.style.display === "block") {
//         drop.style.display = "none";
//         dropdown_financial_id.classList.remove("active");
//     } else {
//         drop.style.display = "block";
//         dropdown_financial_id.classList.add("active");
//     }
// });

function openPopup() {
    const popupWidth = 900;
    const popupHeight = 600;

    // คำนวณตำแหน่งสำหรับหน้าต่าง Popup ให้อยู่ตรงกลางหน้าจอ
    const left = Math.max(0, (window.screen.availWidth - popupWidth) / 2);
    const top = Math.max(0, (window.screen.availHeight - popupHeight) / 2);

    // เปิดหน้าต่าง Popup
    window.open('popup_sale_record_1.html', 'popupWindow', `width=${popupWidth},height=${popupHeight},top=${top},left=${left},resizable=0,scrollbars=yes`);
}
