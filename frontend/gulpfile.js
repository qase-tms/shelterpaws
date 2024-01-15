const { src, dest, parallel, watch } = require('gulp');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass')(require('sass'));
const nunjucks = require('gulp-nunjucks-render');

function server() {
  browserSync.init({
    injectChanges: true,
    server: { baseDir: './testing' },
    notify: false,
    online: true
  })
}

function styles() {
  return src('./src/scss/styles.scss')
    .pipe(sass())
    .pipe(dest('./src/static/'))
    .pipe(dest('./testing/'))
    .pipe(browserSync.stream())
}

function html() {
	return src('./src/templates/pages/*/*.njk')
		.pipe(nunjucks({
      path: ['src/templates/']
    }))
    .pipe(dest('./testing/'))
    .pipe(browserSync.stream());
}

function startWatch() {
  watch('./src/scss/**/*.scss', styles);
  watch('./src/templates/**/*.(njk|html)', html);
}

exports.browsersync = server;
exports.styles = styles;
exports.html = html;

exports.default = parallel(styles, html, server, startWatch);
