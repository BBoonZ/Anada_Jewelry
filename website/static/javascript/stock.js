// document.querySelector('.button_sale_record').addEventListener('click', function() {
//     window.location.href = '/recordsales/none';
// });

// document.querySelector('.dropdown_Stock_class').addEventListener('click', function() {
//     window.location.href = 'stock.html';
// });

// เพิ่มสินค้าใหม่ popup


let newItem = document.getElementById("new_item");
let newProduct = document.getElementById("newProductPopup");
let overlay = document.getElementById("overlay");
let cancelButton = document.getElementById("newCancelButton");

newItem.addEventListener("click", function(){
    newProduct.style.display = 'block';
    overlay.style.display = 'block';
})

cancelButton.addEventListener("click", function(){
    newProduct.style.display = 'none';
    overlay.style.display = 'none';
})

document.getElementById('add-picture-button').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

// เมื่อมีการเลือกไฟล์ แสดงชื่อไฟล์ที่เลือกใน console
document.getElementById('fileInput').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        console.log('File selected: ' + file.name);
    } else {
        console.log('No file selected');
    }
});

// Edit สินค่้า popup

// ตั้งค่า default ของประเภทสินค้า
document.getElementById("product-type").value = "option4"; 

// เพิ่มลดจำนวน

function decrement() {
    var input = document.getElementById('quantity');
    var value = parseInt(input.value);
    if (value > 1) {
        input.value = value - 1;
    }
}

function increment() {
    var input = document.getElementById('quantity');
    var value = parseInt(input.value);
    input.value = value + 1;
}

// เปิด edit popup
function openEdit(url){
    document.getElementById('popupContainer').style.display = 'block';
    var iframe = document.getElementById('contentIframe');
    iframe.src = url;
    console.log(url)
}

// ปิดหน้าต่าง edit popup
function closeEdit(){
    document.getElementById('popupContainer').style.display = 'none';
}

// เปิดหน้าเลือกไฟล์ของ edit popup
document.getElementById('change-picture-button').addEventListener('click', function() {
    document.getElementById('editFileInput').click();
});

// เมื่อมีการเลือกไฟล์ แสดงชื่อไฟล์ที่เลือกใน console
document.getElementById('editFileInput').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        console.log('File selected: ' + file.name);
    } else {
        console.log('No file selected');
    }
});