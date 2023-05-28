<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $emailOrUsername = $_POST["emailOrUsername"];
    $password = $_POST["password"];

    $conn = mysqli_connect("localhost", "root", "", "agroaid_db");
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $sql = "SELECT * FROM users WHERE (email = '$emailOrUsername' OR username = '$emailOrUsername') AND password = '$password'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) == 1) {
        $row = mysqli_fetch_assoc($result);
        $_SESSION["username"] = $row["username"];
        header("Location: dashboard.php");
    } else {
        echo "Invalid email/username or password";
    }

    mysqli_close($conn);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST" action="login.php">
        <label for="emailOrUsername">Email or Username:</label>
        <input type="text" name="emailOrUsername" required><br>

        <label for="password">Password:</label>
        <input type="password" name="password" required><br>

        <input type="submit" value="Login">
    </form>
</body>
</html>
