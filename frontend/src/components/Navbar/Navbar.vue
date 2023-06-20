<!-- Script -->

<script setup lang="ts">
</script>

<!-- Template -->

<template>

<nav id="navbar">
	<a id="brand" href="/">
		<img src="@/assets/png/logo64.png" />
	</a>
	<ul id="nav-links">
		<li class="nav-link"><a href="#">GitHub</a></li>
		<li class="nav-link"><a href="#">Documentation</a></li>
	</ul>
</nav>

</template>

<!-- Style -->

<style>

#navbar {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin: 0;
	background-color: var(--golden-honey);
}

#nav-links {
	display: flex;
	margin-right: 32px;
}

#brand {
	margin-left: 32px;
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
