import { get } from 'svelte/store';
import { goto } from '$app/navigation';
import { writable } from 'svelte/store';

import { initialFormState } from './consts';
import { authRequest } from '$lib/utils/requests/auth-request';
import { requestsWrapper } from '$lib/utils/requests/request-wrapper';
import { checkIsEmpty } from '$lib/utils/validations';

export const formComposable = () => {
	const formState = writable(initialFormState);

	const setUsername = (value: string) => {
		formState.update((state) => ({
			...state,
			// hasChanges: true && state.fields.hasChanges
			fields: {
				...state.fields,
				username: {
					value: value,
					hasChanges: true,
					isValid: !checkIsEmpty(value)
				}
			}
		}));
	};
	const setPassword = (value: string) => {
		formState.update((state) => ({
			...state,
			// hasChanges: true && state.username.hasChanges,
			fields: {
				...state.fields,
				password: {
					value: value,
					hasChanges: true,
					isValid: !checkIsEmpty(value)
				}
			}
		}));
	};

	const setError = (value?: string) => {
		formState.update((state) => ({ ...state, error: value }));
	};

	const setIsLoading = (loading: boolean) =>
		formState.update((state) => ({ ...state, isLoading: loading }));

	const abortController = new AbortController();
	const handleSubmit = async () => {
		const { password, username } = get(formState).fields;
		await requestsWrapper({
			setLoadingState: setIsLoading,
			onError: setError,
			requestParams: { username: username.value, password: password.value },
			onSuccess: (data: string) => {
				localStorage.setItem('token', data);
				goto('/animals');
			},
			request: authRequest,
			abortController
		});
	};

	return {
		setUsername,
		setPassword,
		formState,
		handleSubmit,
		abortController
	};
};
