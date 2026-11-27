# Circular progress indicator — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([circular_progress_indicator.md](circular_progress_indicator.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ File uploads or downloads with measurable, reportable progress

✅ Compact contexts where vertical space is limited and a bar would not fit

✅ Indicating ongoing activity when the wait time cannot be measured

✅ Embedding inside another component (button, tag, toast) to show in-context loading

✅ Short waits between 200 ms and 5 s that still need visual feedback

✅ Long determinate tasks (over 5 s) where percentage or step progress reassures users

✅ Centered, attention-focused loading on an otherwise empty screen or card

✅ Data sync, installation, or processing where the system can estimate completion

✅ Brand-forward or status-driven loading using Accent or functional status colors

✅ Reduced-motion contexts where a static determinate value is preferable to animation

## Progress type — do & don't

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

## Progress (Determinate state only) — do & don't

✅ **Do:** Use motion to reassure users that a determinate process is actively advancing  
❌ **Don't:** Animate a value that never changes — static content should not appear to load

✅ **Do:** Keep the indicator static when displaying a fixed, already-known value (e.g. 50%)  
❌ **Don't:** Force continuous motion when the result is frozen or complete

✅ **Do:** Favor the static option when the user has enabled reduced-motion preferences  
❌ **Don't:** Override OS reduced-motion settings with non-essential looping animation

✅ **Do:** Keep motion smooth and proportional to the actual change in progress  
❌ **Don't:** Use looping motion that implies activity where there is none

✅ **Do:** Limit motion control to the Determinate variant, as the component intends  
❌ **Don't:** Expect static behavior from Indeterminate, which always relies on motion

## Status — do & don't

✅ **Do:** Use Neutral for generic loading where progress carries no semantic meaning  
❌ **Don't:** Apply a functional color (Positive, Negative…) to ordinary background loading

✅ **Do:** Reserve Negative for error recovery, rollback, or failure-related progress  
❌ **Don't:** Use Negative merely to draw attention to a routine process

✅ **Do:** Use Accent to reinforce brand on key user-initiated operations (uploads, onboarding)  
❌ **Don't:** Overuse Accent so that it loses its emphasis across the interface

✅ **Do:** Match the status color to the meaning of the operation, not its completion level  
❌ **Don't:** Change status color to represent percentage (e.g. green = almost done)

✅ **Do:** Pair functional statuses with text, since color alone is not an accessible signal  
❌ **Don't:** Rely solely on status color to convey success, warning, or error

## Animated (for Determinate state only) — do & don't

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

## Gap size — do & don't

✅ **Do:** Use Default gap for most cases to keep the value easy to read  
❌ **Don't:** Reduce the gap so far that indicator and track visually merge

✅ **Do:** Use Small gap for compact placements or to match a tighter brand style  
❌ **Don't:** Mix gap sizes inconsistently across the same screen or product area

✅ **Do:** Keep the gap consistent when several indicators appear together  
❌ **Don't:** Vary gap size decoratively without a functional reason

✅ **Do:** Verify the gap stays proportional after scaling or zoom  
❌ **Don't:** Let a small gap collapse at smaller sizes, hurting legibility

✅ **Do:** Choose gap size with the track shown, where the separation is most visible  
❌ **Don't:** Assume gap matters visually when the track is hidden

## Rounded corner — do & don't

✅ **Do:** Use True to follow the standard rounded artistic direction  
❌ **Don't:** Mix rounded and twisted ends within a single coherent UI

✅ **Do:** Use False when the brand's visual identity relies on twisted corner radii  
❌ **Don't:** Override a brand-level corner decision at the component level without reason

✅ **Do:** Keep the corner style consistent with sibling components nearby  
❌ **Don't:** Switch corner style per instance, creating visual inconsistency

✅ **Do:** Let the corner setting cascade from brand or component context  
❌ **Don't:** Treat rounded corner as a decorative per-screen choice

✅ **Do:** Verify both stroke ends read cleanly at small sizes  
❌ **Don't:** Assume corner style is invisible — it affects perceived precision

## Track — do & don't

✅ **Do:** Show the track for standalone determinate indicators to frame the full range  
❌ **Don't:** Hide the track when users need to judge how much progress remains

✅ **Do:** Hide the track when embedding the indicator in buttons, tags, or toasts  
❌ **Don't:** Keep a heavy track inside dense components where it adds visual noise

✅ **Do:** Use the track to improve readability of the current value  
❌ **Don't:** Rely on the track to convey progress — that is the indicator's job

✅ **Do:** Keep adequate contrast between track and indicator  
❌ **Don't:** Use a track color so close to the indicator that the value is unclear

✅ **Do:** Choose track visibility based on context (standalone vs embedded)  
❌ **Don't:** Apply one track setting everywhere regardless of placement

## User zoom and responsiveness — do & don't

✅ **Do:** Let the loader scale proportionally with user zoom  
❌ **Don't:** Block resizing or cap the component at a fixed pixel size

✅ **Do:** Preserve shape, stroke thickness, and spacing at every zoom level  
❌ **Don't:** Allow the indicator to distort, pixelate, or clip when scaled

✅ **Do:** Keep the original aspect ratio when embedding in another component  
❌ **Don't:** Stretch the loader to fill available container space

✅ **Do:** Ensure it stays visible and recognizable at 50%, 100%, and 200%  
❌ **Don't:** Let meaning become ambiguous at small or large sizes

✅ **Do:** Respect reduced-motion settings when applicable  
❌ **Don't:** Convey essential progress information through motion alone

## Screen Reader — do & don't

✅ **Do:** Announce the purpose first, then the current stage or percentage  
❌ **Don't:** Read every incremental value (1, 2, 3…), overwhelming the listener

✅ **Do:** Group determinate progress into meaningful milestones (e.g. steps of 10)  
❌ **Don't:** Fire constant live-region updates that flood the screen reader

✅ **Do:** Provide a clear status message for indeterminate waits (“Connecting…”)  
❌ **Don't:** Leave an indeterminate process silent, implying nothing is happening

✅ **Do:** Add descriptive context at the parent level, since helper text is not built in  
❌ **Don't:** Assume the indicator alone tells assistive tech what is loading

✅ **Do:** Use polite live updates so progress does not interrupt the user  
❌ **Don't:** Use assertive announcements that hijack focus on every change
