✅ **Do:** Use a determinate indicator whenever the system can measure or estimate progress  
❌ **Don't:** Default to indeterminate when a real percentage or step count is available

✅ **Do:** Reserve indeterminate indicators for genuinely unknown wait times (e.g. server responses)  
❌ **Don't:** Show any indicator for instant operations under ~200 ms — it only flickers

✅ **Do:** Transition from indeterminate to determinate once progress becomes measurable  
❌ **Don't:** Switch types back and forth repeatedly, which makes the wait feel unstable

✅ **Do:** Pair long waits (over 5 s) with descriptive context about what is happening  
❌ **Don't:** Leave users guessing whether a long indeterminate process is still alive

✅ **Do:** Choose the type from expected duration and measurability, not visual preference  
❌ **Don't:** Mix determinate and indeterminate styles for the same task in one flow