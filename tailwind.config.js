/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [    
  './app/**/*.html', 
  './app/**/*.js',],
  theme: {
    extend: {
      colors: {
        gold: '#ffd700',
        skin: {
          lightest: '#ffdbac',
          light: '#f1c27d',
          medium: '#e0ac69',
          dark: '#c68642',
          darkest: '#8d5524',
        },
      },
    },
  },
  plugins: [],
}


