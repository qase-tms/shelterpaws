export const handleInputChange = (
	// mutateField: (value: boolean) => void,
	changeState: (value: string) => void
) => {
	return (value: string | number | null) => {
		if (value === null) {
			return;
		}
		changeState(value?.toString());
	};
};
