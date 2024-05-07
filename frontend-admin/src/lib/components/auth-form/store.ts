import { derived, get } from 'svelte/store';
import { goto } from '$app/navigation';
import { writable } from 'svelte/store';

import { checkIsEmpty } from '$lib/utils/validations';
import { authRequest } from './utils';
import { initialFormState } from './consts';

export const formComposable = () => {
	const formState = writable(initialFormState);

	const setUsername = (value: string) => {
		formState.update((state) => ({ ...state, username: value }));
	};

	const setPassword = (value: string) => {
		formState.update((state) => ({ ...state, password: value }));
	};

	const setIsLoading = (loading: boolean) =>
		formState.update((state) => ({ ...state, isLoading: loading }));

	const isFormValid = derived(
		formState,
		($formState) => checkIsEmpty($formState.password) && checkIsEmpty($formState.username)
	);

	const handleSubmit = async () => {
		setIsLoading(true);
		const { password, username } = get(formState);
		await authRequest({
			username,
			password
		});
		setIsLoading(false);
		goto('/animals');
	};

	return { setUsername, setPassword, isFormValid, formState, handleSubmit };
};
