**When losing focus, the truncation behavior of the input area differs depending on the technical environment. It's important to respect the native behaviors designed to handle truncation:**

For this component, if the text volume exceeds the visible width of the field, the input area truncates the value on the right with a visual truncation indicator (...).

**⚠️ In all cases:** the entire text must remain accessible when the field regains focus:

* Either by opening the dropdown (either by clicking on it or using the down arrow) in which the item is selected and thus seeing the text in its entirety.
* Or via a tooltip on hover in certain desktop contexts.
