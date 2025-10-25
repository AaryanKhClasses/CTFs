# Flag in Flame
The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.

Download the encoded data here: [Logs Data](logs.txt). Be prepared—the file is large, and examining it thoroughly is crucial.

## My Solution:
1. Download the provided `logs.txt` file.
2. Inspecting the file, we notice it contains a large block of what appears to be base64 encoded text.
3. Decode the base64 content using the following command:
```bash
base64 -d logs.txt > decoded_output.bin
```
4. On examining the resulting `decoded_output.bin` file, we find its a PNG image file.
5. Copy the binary data to a PNG file:
```bash
cp decoded_output.bin img.png
```
6. Open the `img.png` file using an image viewer, and we can see some text written: `7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F32346431363839357D`
7. The text appears to be hexadecimal encoded. On decoding the hex string, we get the flag.

### Flag:
```
picoCTF{forensics_analysis_is_amazing_24d16895}
```
