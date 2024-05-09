const preHandledStatusCodes: number[] = [401, 500] as const;
type TPreHandledStatusCodes = (typeof preHandledStatusCodes)[number];

const defaultErrorMessagesByStatus: Record<TPreHandledStatusCodes, string> = {
	401: 'Could not validate credentials',
	500: 'Something went wrong, please try again'
} as const;

export const requestErrorHandler = (status: number = 500, message: string) => {
	if (preHandledStatusCodes.includes(status)) {
		return defaultErrorMessagesByStatus[status];
	}
	return message;
};
