:html_theme.sidebar_secondary.remove:

Interactive scatter plot
-----------------------------

This page demonstrates a scatter plot.

* hovering the mouse provides more detail about each data point (defined in file ``src/interactive_html_plots/main.py``, in the ``px.scatter(..., hover_name="country")`` kwarg).
* single clicking an item in the legend hides it from the plot; double clicking an item in the legend hides all other items from the plot.
* click and drag in the plot to define a window to zoom in; double clicking in the plot resets the zoom.
* additional controls are visible at the top right of the plot.

.. raw:: html
   :file: prerendered_figures/figure_1.html
