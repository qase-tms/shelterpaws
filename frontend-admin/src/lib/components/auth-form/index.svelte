<script lang="ts">
	import 'carbon-components-svelte/css/white.css';

	import { Button, TextInput, Loading } from 'carbon-components-svelte';
	import Card from '$lib/components/card/index.svelte';
	import { onMount } from 'svelte';

	import { formComposable } from './store';

	const { setUsername, setPassword, handleSubmit, formState, isFormValid } = formComposable();

	let isLoading = false;
	let isDisabled = true;
	let isPasswordValid = true;
	let isUsernameValid = true;
	onMount(() => {
		const unsubscribeFormState = formState.subscribe((value) => {
			isLoading = value.isLoading;
			isUsernameValid = Boolean(value.username);
			isPasswordValid = Boolean(value.password);
		});
		const unsubscribeFormValidation = isFormValid.subscribe((value) => {
			isDisabled = value;
		});

		return () => {
			unsubscribeFormState();
			unsubscribeFormValidation();
		};
	});
</script>

<div class="wrapper">
	<Card --max-card-width="600px">
		{#if isLoading}
			<Loading withOverlay={false} small />
		{:else}
			<form class="form" on:submit|preventDefault={handleSubmit}>
				<TextInput
					name="username"
					labelText="Username"
					id="username"
					invalid={!isUsernameValid}
					on:change={(e) => setUsername(e.detail)}
					invalidText="This field is required"
					placeholder="Enter user name"
				/>

				<TextInput
					name="password"
					labelText="Password"
					required
					id="password"
					type="password"
					invalid={!isPasswordValid}
					invalidText="This field is required"
					placeholder="Enter password"
					on:change={(e) => setPassword(e.detail)}
				/>
				<Button type="submit">login</Button>
			</form>
		{/if}
	</Card>
</div>

<style>
	.wrapper {
		margin: 24px auto;
		max-width: 600px;
	}
	.form {
		width: 100%;
		display: flex;
		flex-direction: column;
		gap: 20px;
	}
</style>
