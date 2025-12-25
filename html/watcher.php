<?php
// Dosya yükleme işlemi
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    $uploadDir = 'uploads/'; // Yükleme dizini
    $uploadFile = $uploadDir . basename($_FILES['file']['name']); // Dosyanın hedef yolu

    // Dosya yükleme işlemini gerçekleştir
    if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadFile)) {
        echo "Dosya başarıyla yüklendi!";
    } else {
        echo "Dosya yüklenirken hata oluştu.";
    }
}

// Dosyaları listeleme işlemi
$dir = "uploads/"; // Yüklenen dosyaların bulunduğu dizin
$files = scandir($dir); // Dizin içindeki dosyaları tara

// HTML görünümü
echo "<h1>The Watcher</h1>";
echo "<p>Your uploaded files:</p>";
echo "<div class='file-list'>";

// Dosyaları listele (dizin ve .. öğelerini hariç tut)
foreach ($files as $file) {
    if ($file !== "." && $file !== "..") {
        echo "<p><a href='$dir$file' target='_blank'>$file</a></p>";
    }
}
echo "</div>";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Watcher</title>
    <style>
        body {
            background: black;
            color: #ff0000;
            font-family: 'Courier New', monospace;
            text-align: center;
            overflow: hidden;
        }

        nav ul {
            list-style: none;
            padding: 0;
        }

        nav ul li a:hover {
            text-shadow: 0 0 10px red;
            animation: glitch 0.2s infinite alternate;
        }

        .eye-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 200px;
            height: 200px;
            background: url('eye.gif') no-repeat center center;
            background-size: contain;
            opacity: 0.8;
        }

        .file-list {
            margin-top: 20px;
            font-size: 1.2em;
        }

        /* Stil düzenlemeleri */
        .upload-form {
            margin-top: 20px;
        }

        .upload-form input[type="file"] {
            color: #ff0000;
        }
    </style>
</head>
</html>
