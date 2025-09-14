# 🔍 Domain & Subdomain Extractor  

This tool extracts **unique domains and subdomains** from raw text (e.g., data copied from [crt.sh](https://crt.sh)) for a given parent domain.  
It removes duplicates, strips `http/https/www`, and outputs only clean domains.  

---

## 📥 Step 1 — Copy Data from crt.sh  
1. Go to [crt.sh](https://crt.sh).  
2. Search for your target domain (e.g., `domain.com`).  
3. Copy all the displayed results using `CTRL a` + `CTRL c`.  
4. Paste the content into a text file, for example:  

```bash
nano crt-output
```

## ⚙️ Step 2 — Run the Extractor
```bash
python3 crt-sh-domain-extractor.py domain.com crt-output > domain-output.txt
```
## 📤 Example Output
```bash
api.example.com
example.com
mail.example.com
test.example.com
mail.example.com
```
