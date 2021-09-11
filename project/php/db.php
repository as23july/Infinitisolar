<?php
$servername = "sql305.epizy.com";
$username = "epiz_29420611";
$password = "aditya23";
$db = "epiz_29420611_adityacode";
// Create connection
$conn = mysqli_connect($servername, $username, $password,$db);
// Check connection
if (!$conn) {
   die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?>