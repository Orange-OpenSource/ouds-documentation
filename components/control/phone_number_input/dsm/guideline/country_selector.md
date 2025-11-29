**`Country selector`** When enabled, it is possible to display a country selector with its flag. Country selector is displayed as a secondary button with only an icon (flag) and a chevron.

### Do & don'ts

✅ **Do:** Default the country selector to the user's detected geolocation when available.  
❌ **Don't:** Force users to manually select a country when their location can be automatically detected.

✅ **Do:** Provide a searchable dropdown for the country list—there are nearly 200 countries.  
❌ **Don't:** Display countries only as a scrollable list without search capability.

✅ **Do:** Show both country name and dial code in the dropdown for clarity (e.g., "France (+33)").  
❌ **Don't:** Display only country codes in the selector, requiring users to memorize codes.

✅ **Do:** Preserve the entered phone number if the user changes the country selection.  
❌ **Don't:** Clear the phone number field when users switch countries, forcing re-entry.

✅ **Do:** Make the chevron indicator clearly visible to signal the selector is interactive.  
❌ **Don't:** Use a flag alone without affordance indicators—users may not recognize it as clickable.