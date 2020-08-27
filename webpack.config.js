const path = require('path');
const process = require('process');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin'); 

module.exports = {
    mode: process.env.APP_ENV,
    entry: path.resolve('./static/index.js'),
    output: {
        path: path.resolve('./static/bundles'),
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
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            hmr: process.env.APP_ENV === 'development'
                        }
                    },
                    'css-loader'
                ]
            }
        ]
    },
    optimization: {
        minimize: true
    }
}