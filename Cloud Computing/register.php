<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $username = $_POST["username"];
    $password = $_POST["password"];
    
    $conn = mysqli_connect("localhost", "root", "", "agroaid_db");
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

     $sql = "INSERT INTO users (email, username, password) VALUES ('$email', '$username', '$password')";

    if (mysqli_query($conn, $sql)) {
        echo "Registration successful";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }

    mysqli_close($conn);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST" action="register.php">
        <label for="email">Email:</label>
        <input type="email" name="email" required><br>
        
        <label for="username">Username:</label>
        <input type="text" name="username" required><br>

        <label for="password">Password:</label>
        <input type="password" name="password" required><br>

        <input type="submit" value="Register">
    </form>
</body>
</html>
