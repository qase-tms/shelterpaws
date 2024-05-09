import { goto } from '$app/navigation';

import { initialValues } from './consts';
import { authRequest, type TAuthParams } from '$lib/utils/requests/auth-request';
import { checkIsEmpty } from '$lib/utils/validations';
import { formComposable } from '$lib/composable';

export const store = () => {
	const { formState, abortController, handleSubmit } = formComposable<string, TAuthParams>({
		initialValues,
		onSuccess: (data) => {
			localStorage.setItem('token', data);
			goto('/animals');
		},
		request: authRequest
	});

	const setUsername = (value: string) => {
		formState.update((state) => ({
			...state,
			hasChanges: true && state.fields.password.hasChanges,
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
			hasChanges: true && state.fields.username.hasChanges,
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

	return {
		setUsername,
		setPassword,
		formState,
		handleSubmit,
		abortController
	};
};
