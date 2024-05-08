<script lang="ts">
	import 'carbon-components-svelte/css/white.css';

	import { Button, TextInput, Loading, InlineNotification } from 'carbon-components-svelte';
	import Card from '$lib/components/card/index.svelte';
	import { onMount } from 'svelte';

	import { formComposable } from './store';
	import { handleInputChange } from './utils';
	import { checkIsEmpty } from '$lib/utils/validations';

	let isLoading = false;
	let errorMessage: string | undefined;
	let isUsernameValid = true;
	let isPasswordValid = true;
	let isFormHasChanges = false;

	const { setUsername, setPassword, handleSubmit, formState, abortController } = formComposable();

	const handleUsernameChange = handleInputChange(setUsername);
	const handlePasswordChange = handleInputChange(setPassword);

	onMount(() => {
		const unsubscribeFormState = formState.subscribe((value) => {
			isLoading = value.isLoading;
			errorMessage = value.error;
			isUsernameValid = !value.username.hasChanges ? true : value.username.isValid;
			isPasswordValid = !value.password.hasChanges ? true : value.password.isValid;
			isFormHasChanges = value.hasChanges;
		});

		return () => {
			abortController.abort();
			unsubscribeFormState();
		};
	});
</script>

<div class="wrapper">
	<Card --max-card-width="600px">
		<form class="form" on:submit|preventDefault={handleSubmit}>
			<TextInput
				name="username"
				labelText="Username"
				id="username"
				invalid={!isUsernameValid}
				on:change={(e) => handleUsernameChange(e.detail)}
				invalidText="This field is required"
				placeholder="Enter username"
			/>

			<TextInput
				name="password"
				labelText="Password"
				id="password"
				type="password"
				invalid={!isPasswordValid}
				invalidText="This field is required"
				placeholder="Enter password"
				on:change={(e) => handlePasswordChange(e.detail)}
			/>
			{#if !checkIsEmpty(errorMessage)}
				<InlineNotification kind="error" subtitle={errorMessage} />
			{/if}
			<Button
				type="submit"
				disabled={!isFormHasChanges ? true : !(isUsernameValid && isPasswordValid)}
			>
				{#if isLoading}
					<Loading withOverlay={false} small />
				{:else}
					Sign up
				{/if}
			</Button>
		</form>
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
