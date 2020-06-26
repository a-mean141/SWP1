html = b"""
<html>
    <body>
	<form method="get" action="">
            x = <input type="number" name="a">
	    y = <input type="number" name="b"><br><br>
	    <input type="submit">
	</form>
	<p>
	    Sum: %(sum)s</br>
	    Mul: %(mul)s</br>
	</p>
    </body>
</html>
"""
