

<?php
$mysqli = mysqli_connect("localhost" , "root" ,"" , "shopping bag");

// Check connection
if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
}

?>