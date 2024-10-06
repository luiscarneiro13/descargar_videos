<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\DownloaderController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', [HomeController::class, 'index'])->name('home');
Route::post('prepare', [DownloaderController::class, 'prepare'])->name('prepare');
Route::post('status/{video}', [DownloaderController::class, 'status'])->name('status');
Route::post('download/{video}', [DownloaderController::class, 'download'])->name('download');
