// เพิ่มสินค้าใหม่ popup


let newItem = document.getElementById("new_item");
let newProduct = document.getElementById("newProductPopup");
let overlay = document.getElementById("overlay");
let cancelButton = document.getElementById("newCancelButton");



cancelButton.addEventListener("click", function(){
    console.log("hello")
    newProduct.style.display = 'none';
    overlay.style.display = 'none';
})


// เรื่องรูปภาพ
// Trigger file input when the "Add Picture" button is clicked
document.getElementById('add-picture-button').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

// แสดงภาพตัวอย่างเมื่อเลือกไฟล์
document.getElementById('fileInput').addEventListener('change', function(event) {
    console.log("ww")
    const file = event.target.files[0]; // รับไฟล์ที่เลือก
    if (file) {
        const reader = new FileReader(); // สร้าง FileReader เพื่ออ่านไฟล์
        reader.onload = function(e) {
            const img = document.getElementById('imagePreview'); // รับอิลิเมนต์ img
            img.src = e.target.result; // ตั้งค่าตัวอย่างภาพ
            img.style.display = 'block'; // แสดงภาพตัวอย่าง
        }
        reader.readAsDataURL(file); // อ่านไฟล์เป็น URL
    } else {
        // หากไม่พบไฟล์ ให้ซ่อนภาพตัวอย่าง
        const img = document.getElementById('imagePreview');
        img.style.display = 'none';
    }
});

document.getElementById('fileInput').addEventListener('change', function() {
    const fileName = this.files[0] ? this.files[0].name : 'No file chosen';
    console.log(fileName);  // You can display it in the UI or log it for debugging
});


// document.getElementById('add-picture-button').addEventListener('click', function() {
//     document.getElementById('fileInput').click();
// });


// document.getElementById('fileInput').addEventListener('change', function() {
//     const file = this.files[0];
//     if (file) {
//         console.log('File selected: ' + file.name);
//     } else {
//         console.log('No file selected');
//     }
// });