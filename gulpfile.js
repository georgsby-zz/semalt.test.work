var gulp = require("gulp"),
    sass = require("gulp-sass"),
    browserSync = require("browser-sync"),
    clean = require("gulp-clean"),
    cache = require("gulp-cache"),
    autoprefixer = require("gulp-autoprefixer");
    reload = browserSync.reload;


var scssPath = {
    sourceMain: './web/assets/web/scss/main.scss',
    dist: './web/static/web/css',
    watch: './web/assets/web/scss/**/*.scss'
};
var jsPath = {
    source: './web/assets/web/js/**/*.js',
    dist: './web/static/web/js'
};
var imagesPath = {
    source: './web/assets/web/img/**/*',
    dist: './web/static/web/img'
};
var staticPath = './web/static/web/';
var templatesPath = './web/templates/**/*.html';

gulp.task("css:blink", function () {
    return gulp
        .src(scssPath.sourceMain)
        .pipe(sass())
        .pipe(
            autoprefixer(["last 15 versions", ">1%", "ie 8", "ie 7"], {
                cascade: true
            })
        )
        .pipe(gulp.dest(scssPath.dist))
        .pipe(browserSync.reload({stream: true}));
});

gulp.task("img:blink", function () {
    return gulp.src(imagesPath.source).pipe(gulp.dest(imagesPath.dist));
});

gulp.task("clear", function () {
    return cache.clearAll();
});

gulp.task("js:blink", function () {
    return gulp.src(jsPath.source).pipe(gulp.dest(jsPath.dist));
});

gulp.task("clean", function () {
    return gulp.src(staticPath).pipe(clean());
});

gulp.task("browser-sync", function () {
    browserSync.init({
        server: {
            baseDir: "./"
        },
        notify: false,
        open: false
    });
});

gulp.task("watch", ["browser-sync", "css:blink", "js:blink", "img:blink"],
    function () {
        gulp.watch(scssPath.watch, ["css:blink"]);
        gulp.watch(jsPath.source, ["js:blink"]);
        gulp.watch(imagesPath.source, ["img:blink"]);
        gulp.watch(templatesPath).on("change", reload);
    }
);