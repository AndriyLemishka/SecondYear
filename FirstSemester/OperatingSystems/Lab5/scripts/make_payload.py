import gzip
import base64

with open('guest_setup_full.ps1', 'rb') as f:
    data = f.read()

compressed = gzip.compress(data)
b64 = base64.b64encode(compressed).decode('ascii')
print(f"Original: {len(data)} bytes, Compressed b64: {len(b64)} chars")

chunk_size = 120
with open('inject_b64.txt', 'w', encoding='ascii') as out:
    out.write('$b = ""\n')
    for i in range(0, len(b64), chunk_size):
        chunk = b64[i:i+chunk_size]
        out.write(f'$b += "{chunk}"\n')
    out.write('$bytes = [System.Convert]::FromBase64String($b)\n')
    out.write('$ms = New-Object System.IO.MemoryStream(,$bytes)\n')
    out.write('$gz = New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress)\n')
    out.write('$sr = New-Object System.IO.StreamReader($gz, [System.Text.Encoding]::UTF8)\n')
    out.write('$code = $sr.ReadToEnd()\n')
    out.write('$sr.Close()\n')
    out.write('$gz.Close()\n')
    out.write('$ms.Close()\n')
    out.write('$code | Out-File C:\\setup.ps1 -Encoding UTF8\n')
    out.write('& C:\\setup.ps1\n')

print("Wrote inject_b64.txt successfully")
