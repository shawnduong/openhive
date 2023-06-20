<!-- Script -->

<script setup lang="ts">
</script>

<!-- Template -->

<template>

<div class="center">
	<div id="login">
		<div id="form">
			<h2>Sign In</h2>
			<form>
				<label for="username">Username</label><br>
				<input type="text" id="username" name="username" /><br><br>
				<label for="password">Password</label><br>
				<input type="password" id="password" name="password" /><br><br>
				<input type="submit" value="Enter" class="form-enter" />
			</form>
		</div>
		<div id="description">
			<p>OpenHive is a free and open-source self-hosted network management platform for AeroHive wireless access points.</p>
			<p>Liberate your WAPs from vendor lock and use the hardware you own!</p>
			<p><b>This project is a WIP. Some features may be unstable.</b></p>
		</div>
	</div>
</div>

</template>

<!-- Style -->

<style scoped>

#login {
	background-color: var(--secondary);
	width: max-content;
	border-radius: 4px;
	padding: 32px;
	margin-top: 96px;
}

#login h2 {
	text-align: center;
}

#form {
	display: inline-block;
	margin-right: 32px;
	vertical-align: middle;
}

#form input {
	background-color: var(--primary-alt-off);
	border: none;
	border-radius: 4px;
	padding: 4px;
	margin-top: 4px;
}

#description {
	display: inline-block;
	vertical-align: middle;
	border-left: 2px solid var(--secondary-off);
	height: 100%;
	max-width: 18em;
	text-align: justify;
	padding-left: 32px;
}

.center {
	display: flex;
	justify-content: center;
	height: 100%;
}

.form-enter {
	width: 100%;
	background-color: var(--primary-alt) !important;
	border: none;
	border-radius: 2px;
	padding: 4px;
}

.form-enter:hover {
	cursor: pointer;
}

</style>
