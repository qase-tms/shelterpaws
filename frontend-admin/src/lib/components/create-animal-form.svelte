<script lang="ts">
	let name_en = '';
	let name_ru = '';
	let type = '';
	let sex = '';
	let age = '';
	let size = '';

	let isLoading = false;

	const handleSubmit = async () => {
		const token = localStorage.getItem('token');
		const url = 'http://0.0.0.0:8080/animals';
		isLoading = true;
		const response = await fetch(url, {
			method: 'POST',
			headers: {
				'content-type': 'application/json',
                'x-auth': token,
			},
			body: JSON.stringify({
				name_en,
				name_ru,
				type,
				sex,
				age,
				size,
				shelter_id: 1
			})
		});

		if (response.status == 200) {
			console.log('ok');
		}

		const result = await response.json();
		console.log(result);

		setTimeout(() => {
			isLoading = false;
		}, 1000);
	};
</script>

<div>
	<h2>Create an animal</h2>
	{#if isLoading}
		<div class="loading" />
	{:else}
		<form on:submit|preventDefault={handleSubmit}>
			<input type="text" name="name_en" id="name_en" placeholder="name_en" bind:value={name_en} />
			<input type="text" name="name_ru" id="name_ru" placeholder="example" bind:value={name_ru} />
			<input type="text" name="type" id="type" placeholder="example" bind:value={type} />
			<input type="text" name="sex" id="sex" placeholder="example" bind:value={sex} />
			<input type="text" name="age" id="age" placeholder="example" bind:value={age} />
			<input type="text" name="size" id="size" placeholder="example" bind:value={size} />
			<button> create animal </button>
		</form>
	{/if}
</div>

<style>
	form {
		max-width: 500px;
		padding: 20px;
		margin: 0 auto;

		border-radius: 20px;
		box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);

		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 20px;
	}

	.loading {
		width: 50px;
		height: 50px;
		border-left: 2px solid black;
		border-bottom: 2px solid black;
		border-radius: 50%;
		animation: loader 0.3s ease-in-out infinite;
	}

	@keyframes loader {
		0% {
			transform: rotate(0);
		}

		50% {
			transform: rotate(180deg);
		}
		100% {
			transform: rotate(360deg);
		}
	}
</style>
