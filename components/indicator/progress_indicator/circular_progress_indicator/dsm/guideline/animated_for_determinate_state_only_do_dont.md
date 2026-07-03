✅ **Do:** Enable animation when a determinate value updates over time  
❌ **Don't:** Animate a determinate indicator whose value is fixed and final

✅ **Do:** Use Start animation (0% → value) when introducing a brand-new process  
❌ **Don't:** Replay the intro animation when simply restoring a known, in-progress value

✅ **Do:** Set Start animation to false when the current value is already known on load  
❌ **Don't:** Delay perceived readiness with an intro animation users do not need

✅ **Do:** Keep animation tied to the Determinate variant, as Indeterminate handles its own motion  
❌ **Don't:** Expect an Animated toggle on Indeterminate — it is not exposed

✅ **Do:** Honor reduced-motion settings by allowing a non-animated determinate display  
❌ **Don't:** Make essential progress information depend only on motion