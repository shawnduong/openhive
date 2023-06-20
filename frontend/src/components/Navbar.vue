<!-- Script -->

<script setup lang="ts">
</script>

<!-- Template -->

<template>

<nav id="navbar">
	<a id="brand" href="/">
		<img src="@/assets/png/logo_light.png" />
	</a>
	<ul id="nav-links">
		<li class="nav-link"><a href="#">GitHub</a></li>
		<li class="nav-link"><a href="#">Documentation</a></li>
	</ul>
</nav>

</template>

<!-- Style -->

<style scoped>

#navbar {
	display: flex;
	position: fixed;
	width: 100%;
	justify-content: space-between;
	align-items: center;
	margin: 0;
	background-color: var(--secondary);
}

#nav-links {
	display: flex;
	margin-right: 32px;
}

#brand {
	margin: 8px 32px;
}

#brand img {
	height: 64px;
}

.nav-link {
	list-style: none;
	padding-left: 1em;
}

.nav-link a, .nav-link a:visited, .nav-link a:hover, .nav-link a:active {
	text-decoration: none;
	color: inherit;
}

</style>
