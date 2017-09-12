$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
$ErrorActionPreference = "SilentlyContinue"

Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip
{
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}

Unzip "$scriptPath\ffmpeg.zip" "$scriptPath\ffmpeg"
