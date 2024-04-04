/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [    
  './app/**/*.html', 
  './app/**/*.js',],
  theme: {
    extend: {
      colors: {
        beachGrass:'#c8e7b0',
        sand:'#f5f5dc',
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


