const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin'); 

module.exports = {
    entry: path.resolve('./static/styles/index.js'),
    output: {
        path: path.resolve(__dirname, './static/bundles'),
        filename: '[name]-[hash].js'
    },
    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
        new MiniCssExtractPlugin({ filename: '[name]-[hash].css' }),
        new OptimizeCssAssetsPlugin()
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader']
            }
        ]
    },
    optimization: {
        minimize: true
    }
}