<nav class="navbar navbar-default">
	<div class="container-fluid">
		<div class="navbar-header">
			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#header">
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="/myhealth">
				<img src="/myhealth/assets/myhealth/img/logo-small.png"/>
				MyHealth
			</a>
		</div>
		<div class="collapse navbar-collapse" id="header">
      			<ul class="nav navbar-nav">
        			<li<?php if($_SERVER['REQUEST_URI'] == "/myhealth/") { print ' class="active"'; } ?>><a href="/myhealth">Home</a></li>
				<li<?php if($_SERVER['REQUEST_URI'] == "/myhealth/page/measurements/") { print ' class="active"'; } ?>><a href="page/measurements">Meetingen</a></li>
      			</ul>
		</div>
	</div>
</nav>