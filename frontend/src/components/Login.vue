<!-- Script -->

<script setup lang="ts">
</script>

<!-- Template -->

<template>

<div class="center">
	<div id="login">
		<h2>Sign In</h2>
		<form>
			<label for="username">Username</label><br>
			<input type="text" id="username" name="username" /><br><br>
			<label for="password">Password</label><br>
			<input type="password" id="password" name="password" /><br><br>
			<input type="submit" value="Enter" class="form-enter" />
		</form>
	</div>
</div>

</template>

<!-- Style -->

<style>

#login {
	height: 100%;
	background-color: var(--golden-honey);
	width: max-content;
	border-radius: 4px;
	padding: 16px;
	margin-top: 64px;
}

#login h2 {
	text-align: center;
}

.center {
	display: flex;
	justify-content: center;
}

.form-enter {
	width: 100%;
}

</style>
