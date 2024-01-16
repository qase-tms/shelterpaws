const { src, dest, parallel, watch } = require('gulp');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass')(require('sass'));
const nunjucks = require('gulp-nunjucks-render');

const TESTING_PATH = './testing';
const SRC_PATH = './src';
const SCSS_PATH = `${SRC_PATH}/scss`;
const STATIC_PATH = `${SRC_PATH}/static`;
const TEMPLATES_PATH = `${SRC_PATH}/templates`;

function server() {
  browserSync.init({
    injectChanges: true,
    server: { baseDir: TESTING_PATH },
    notify: false,
    online: true
  })
}

function styles() {
  return src(`${SCSS_PATH}/styles.scss`)
    .pipe(sass())
    .pipe(dest(STATIC_PATH))
    .pipe(dest(TESTING_PATH))
    .pipe(browserSync.stream())
}

function html() {
	return src(`${TEMPLATES_PATH}/pages/*/*.njk`)
		.pipe(nunjucks({
      path: [TEMPLATES_PATH]
    }))
    .pipe(dest(TESTING_PATH))
    .pipe(browserSync.stream());
}

function copyImages() {
  return src(`${STATIC_PATH}/img/**/*`)
    .pipe(dest(`${TESTING_PATH}/img`))
}

function copyContentImages() {
  return src(`${STATIC_PATH}/upload/**/*`)
    .pipe(dest(`${TESTING_PATH}/upload`))
}

async function copyResources() {
  copyImages();
  copyContentImages();
}

function startWatch() {
  watch(`${SCSS_PATH}/**/*.scss`, styles);
  watch(`${TEMPLATES_PATH}/**/*.(njk|html)`, html);
}

exports.browsersync = server;
exports.styles = styles;
exports.html = html;
exports.copyResources = copyResources;

exports.default = parallel(styles, html, server, copyResources, startWatch);
