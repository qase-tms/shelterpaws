type FormState = {
	fields: {
		password: InputParams<string>;
		username: InputParams<string>;
	};
	isLoading: boolean;
	hasChanges: boolean;
	error?: string;
};

type InputParams<T> = {
	value: T;
	isValid: boolean;
	hasChanges: boolean;
};

export const initialFormState: FormState = {
	fields: {
		password: {
			isValid: true,
			value: '',
			hasChanges: false
		},
		username: {
			isValid: true,
			value: '',
			hasChanges: false
		}
	},
	hasChanges: false,
	isLoading: false,
	error: undefined
};
