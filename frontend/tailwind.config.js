/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'pink-lace': '#FFCEEFB3',
        'anakiwa': '#ACE9FFB3',
        'alto': '#D6D6D6'
      },
    },
  },
  plugins: [],
}

