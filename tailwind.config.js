/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		'./src/templates/**/*.{html,js}',
		'./src/**/forms.py'
	],
	theme: {
		extend: {},
	},
	plugins: [
		require('@tailwindcss/forms'),
		require('@tailwindcss/typography')
	],
}
