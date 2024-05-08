import { get } from 'svelte/store';
import { goto } from '$app/navigation';
import { writable } from 'svelte/store';

import { initialFormState } from './consts';
import { authRequest } from '$lib/utils/requests/auth-request';
import { requestsWrapper } from '$lib/utils/requests/request';
import { checkIsEmpty } from '$lib/utils/validations';

export const formComposable = () => {
	const formState = writable(initialFormState);

	const setUsername = (value: string) => {
		formState.update((state) => ({
			...state,
			username: {
				value: value,
				hasChanges: true,
				isValid: !checkIsEmpty(value)
			},
			hasChanges: true && state.password.hasChanges
		}));
	};
	const setPassword = (value: string) => {
		formState.update((state) => ({
			...state,
			password: {
				value: value,
				hasChanges: true,
				isValid: !checkIsEmpty(value)
			},
			hasChanges: true && state.username.hasChanges
		}));
	};

	const setError = (value?: string) => {
		formState.update((state) => ({ ...state, error: value }));
	};

	const setIsLoading = (loading: boolean) =>
		formState.update((state) => ({ ...state, isLoading: loading }));

	let outsideAbortController = new AbortController();
	const handleSubmit = async () => {
		const { password, username } = get(formState);
		const { data, abortController } = await requestsWrapper({
			setLoadingState: setIsLoading,
			setErrorState: setError,
			params: { username: username.value, password: password.value },
			request: authRequest
		});
		localStorage.setItem('token', data);
		outsideAbortController = abortController;
		goto('/animals');
	};

	return {
		setUsername,
		setPassword,
		formState,
		handleSubmit,
		abortController: outsideAbortController
	};
};
