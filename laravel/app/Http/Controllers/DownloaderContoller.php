<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;

class DownloaderController extends Controller
{
    public function prepare(Request $request)
    {
        $this->validate($request, [
           'url' => 'required'
        ]);

        try {
            $process = new Process([
                'youtube-dl',
                $request->url,
                '-o',
                storage_path('app/public/downloads/%(title)s.%(ext)s')
                , '--print-json'
            ]);

            $process->mustRun();

            $output = json_decode($process->getOutput(), true);

            if (json_last_error() !== JSON_ERROR_NONE) {
                throw new \Exception("Could not download the file!");
            }

            return response()->download($output['_filename']);

        }  catch (\Throwable $exception) {
            $request->session()->flash('error', 'Could not download the given link!');
            logger()->critical($exception->getMessage());
            return back();
        }
    }
}
