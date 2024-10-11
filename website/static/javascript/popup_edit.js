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



// ปิดหน้าต่าง edit popup
function closeEdit(){
    document.getElementById("edit-popup").style.display = 'none';
    overlay.style.display = 'none';
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
