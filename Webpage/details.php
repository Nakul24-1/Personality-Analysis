
Your name is <?php 
$name = isset($_POST['name']) ? $_POST['name']:'';
echo $_POST["name"]; ?>
<br>
Your email address is  <?php 
$email = isset($_POST['email']) ? $_POST['email']:'';
echo $_POST["email"]; ?>
<br>
Your phone number is  <?php
$contact = isset($_POST['contact']) ? $_POST['contact']:'';
echo $_POST["contact"]; ?>
<br>
Your Gender is <?php 
$gender = isset($_POST['gender']) ? $_POST['gender']:'';
if (isset($_POST["gender"])){ echo $_POST["gender"]; } ?>
<br>
You have experience of  <?php 
$list = isset($_POST['list']) ? $_POST['list']:'';
if (isset($_POST["list"])){ echo $_POST["list"]; } ?>
<br>
Fluent in following languages: <?php
$checklist = isset($_POST['checklist']) ? $_POST['checklist']:'';
if(!empty($_POST['checklist']))
{
	foreach($_POST['checklist'] as $selected)
		{
			echo $selected."</br>";
		}
}
?>
<br>
Job Profile applied for <?php
$list2 = isset($_POST['list2']) ? $_POST['list2']:'';
if (isset($_POST["list2"])){ echo $_POST["list2"]; } ?>