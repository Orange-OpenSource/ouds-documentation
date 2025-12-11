✅ **Do:** Use the skeleton state during content loading to maintain layout stability and reduce perceived wait time.  
❌ **Don't:** Show an empty container or leave blank space while alert content loads.

✅ **Do:** Transition smoothly from skeleton to enabled state once content is available.  
❌ **Don't:** Display skeleton state indefinitely without a timeout or fallback behavior.

✅ **Do:** Match the skeleton dimensions to the expected content size to prevent layout shifts.  
❌ **Don't:** Use a generic skeleton size that causes jarring visual changes when content appears.

✅ **Do:** Reserve skeleton usage for situations where loading time is noticeable (>300ms).  
❌ **Don't:** Flash skeleton state for near-instantaneous content loads.

✅ **Do:** Ensure skeleton state is accessible with appropriate ARIA attributes indicating loading status.  
❌ **Don't:** Leave skeleton elements without accessible indicators for screen reader users.