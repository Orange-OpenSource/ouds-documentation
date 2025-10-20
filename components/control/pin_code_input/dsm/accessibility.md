# Accessibility

### Keyboard Navigation

The component must support full keyboard accessibility with intuitive navigation between cells. Users should be able to tab into the component, which focuses the first empty cell (or first cell if all are empty). Arrow keys (Left/Right) should move focus between cells, allowing users to navigate freely to correct mistakes. Backspace should delete the current cell's content and move focus to the previous cell, while Delete should clear the current cell without moving focus. The Tab key should move focus out of the component to the next focusable element on the page. All focus indicators must meet a minimum contrast ratio of 3:1 against adjacent colors and be clearly visible, typically using a 2-3px outline or border highlight. When errors occur, focus should remain on or return to the first cell to allow easy re-entry.

---

### Screen Reader Support

Each input cell must be implemented as a proper form input element (input type="text" with inputmode="numeric") with semantic HTML ensuring native screen reader support. The component container should have a role="group" with an accessible name describing its purpose (e.g., "Verification code input"). Each individual cell must have an accessible label indicating its position, such as "Digit 1 of 6" using aria-label or aria-labelledby. When a digit is entered, screen readers should announce the entered value and automatically indicate focus has moved to the next cell. Error states must use aria-invalid="true" on affected cells with associated error messages linked via aria-describedby. Status messages (like "Code accepted" or "Invalid code") should be announced through ARIA live regions (aria-live="polite" for non-urgent messages, aria-live="assertive" for critical errors).

---

### ARIA Attributes

The component requires several ARIA attributes for proper accessibility. The container must use role="group" with aria-labelledby pointing to the component's label element. Each input cell should include aria-label="Digit [X] of [Y]" to indicate position within the sequence. When in error state, cells must have aria-invalid="true" and aria-describedby pointing to the error message element's ID. If using helper text, associate it with the component using aria-describedby on the container. For auto-complete functionality, cells should include autocomplete="one-time-code" to enable browser/OS-level code detection from SMS. Status updates should use aria-live="polite" for general messages and aria-live="assertive" for critical errors, ensuring announcements don't interrupt current screen reader activity unnecessarily.

---

### Focus Management

Focus must be managed programmatically throughout the interaction lifecycle. On component mount, if auto-focus is enabled, focus should move to the first input cell automatically. When a digit is entered, focus should automatically advance to the next empty cell. When Backspace is pressed, focus should move to the previous cell after clearing the current one. If users navigate with arrow keys, focus should move appropriately between cells. When validation occurs and an error is detected, focus should return to the first cell to allow easy re-entry of the complete code. Focus indicators must be clearly visible with sufficient contrast (minimum 3:1 ratio) and typically implemented as a 2-3px colored border or outline. Focus should never be trapped within the component—users must always be able to tab out to other page elements. When the component is disabled, it should not receive focus at all.

---

### Error Handling

Error states must be communicated through multiple channels for accessibility. Visual changes alone (color shifts) are insufficient—errors must be programmatically announced to screen readers using aria-live regions. Each input cell in error state should have aria-invalid="true" applied. A descriptive error message must appear below the component and be associated via aria-describedby on the input cells, with messages like "The code you entered is invalid. Please check your messages and try again." The error message element should have role="alert" or be within an element with aria-live="assertive" to ensure immediate announcement. Focus should return to the first input cell when an error occurs, allowing users to easily re-enter the code. Error messages should be persistent (not automatically dismissed) until the user begins correcting the input. Color contrast for error text must meet WCAG requirements (4.5:1 for normal text).

---

### Touch Targets

All interactive elements must meet minimum touch target size requirements for mobile accessibility. Each input cell should be at least 44x44 pixels (iOS standard) or 48x48 pixels (Android standard) to ensure comfortable touch interaction. Spacing between adjacent cells should be sufficient (minimum 8px) to prevent accidental taps on neighboring cells. On mobile devices, tapping any cell should bring up the numeric keyboard automatically with inputmode="numeric" or type="tel" on the input elements. The entire component should be positioned with adequate spacing from other interactive elements on the page (minimum 8px clearance) to prevent mis-taps. For tablet devices, consider slightly larger target sizes (48-52px) to accommodate stylus input. Touch targets should include visual feedback on tap (such as brief background color change) to confirm interaction.

---

### Color Contrast

All text and interactive elements must meet WCAG 2.1 AA contrast requirements. Input cell borders must have a contrast ratio of at least 3:1 against adjacent backgrounds for both filled and outlined variants. Text content within cells (entered digits) must meet 4.5:1 contrast for normal text or 3:1 for large text (18px+ regular or 14px+ bold). Placeholder indicators or empty cell backgrounds must provide sufficient contrast to be perceivable. Focus indicators must have a minimum 3:1 contrast ratio against both the cell background and the surrounding page background. Error states must not rely solely on color—red borders for errors must be accompanied by text messages and/or iconography. When using color to indicate states (focused, filled, error), ensure each state is distinguishable by at least one additional non-color characteristic (border width, icon, pattern). Test the component in both light and dark modes to ensure contrast requirements are met in all themes.

---

### Component-Specific Considerations

The Pin Code Input has unique accessibility requirements beyond standard form inputs. Since it presents a single logical input split across multiple visual cells, screen readers must understand it as a unified code entry field rather than separate, unrelated inputs. Use role="group" on the container with a clear accessible name to establish this relationship. The component must handle auto-fill from SMS and authenticator apps accessibly—when a code is auto-populated, screen readers should announce "Code automatically entered" or similar confirmation. For security reasons, consider whether to implement masking (showing dots instead of numbers after entry)—if implemented, provide a "Show/Hide code" toggle that's keyboard accessible and properly announced. Time-limited codes should include accessible timer announcements ("Code expires in 30 seconds") without interrupting the input process. If the component includes a "Resend code" button, ensure it's keyboard accessible, has clear focus indication, and announces its state (disabled/enabled) and any cooldown periods ("Resend available in 30 seconds").