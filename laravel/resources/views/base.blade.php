<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Video downloader</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</head>
<body>

<main role="main">
    <div class="container">
        <div class="row">
            <div class="col-6 text-center" style="margin: 0 auto;">
                <h1 class="mt-5">@yield('title')</h1>
                @yield('content')
            </div>
        </div>
    </div>
</main>

</body>
</html>
Crea una nueva vista llamada home.blade.php con el siguiente contenido:

@extends('base')
@section('title', 'Video Downloader')

@section('content')
    <form method="post" action="{{ route('prepare') }}">
        @csrf

        @if(Session::has('error'))
            <div class="alert alert-danger">{{ Session::get('error') }}</div>
        @endif

        <div class="form-group">
            <input name="url" type="text" required class="form-control @error('url')  is-invalid @enderror" id="url"
                   aria-describedby="url" value="{{ old('url') }}"
                   autocomplete="off" autofocus>

            @error('url')
                <div class="invalid-feedback">{{ $message }}</div>
            @enderror
        </div>

        <div class="text-center">
            <button class="btn btn-lg btn-primary">Download</button>
        </div>
    </form>
@endsection
