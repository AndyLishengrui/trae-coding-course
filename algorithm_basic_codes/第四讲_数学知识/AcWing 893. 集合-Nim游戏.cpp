memset(f,-1,sizeof f);

int res = 0;
for (int i = 0; i < n; i++)
{
  int x; cin >> x;
  res ^= sg(x);
}

if (res) puts("Yes");
else puts("No");

return 0;