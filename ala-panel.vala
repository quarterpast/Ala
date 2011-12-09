using Gdk;

public class Wingpanel.Panel : Gtk.Window {

    private Gtk.MenuBar menubar;
    private IndicatorsModel model;
    private Gee.HashMap<string, Gtk.MenuItem> menuhash;

    public Panel () {
        

        set_default_size (-1, 25);

        menuhash = new Gee.HashMap<string, Gtk.MenuItem> ();


        /* No taskbar, no decoration */
        skip_taskbar_hint = true;
        decorated = false;
        app_paintable = true;
        set_type_hint (Gdk.WindowTypeHint.DOCK);
        set_visual(screen.get_rgba_visual());
        resizable = false;
        menubar = new Gtk.MenuBar ();
        add (menubar);
        menubar.can_focus = true;
        menubar.border_width = 0;
        menubar.set_size_request(-1,24);
        menubar.set_name ("indicator-applet-menubar");
        /*Gtk.rc_parse_string ("""
            style "wingpanel-menuitem"
            {
                 GtkMenuItem::horizontal-padding = 2
            }
            widget_class "*.<GtkMenuItem>" style "wingpanel-menuitem"
            """
            );*/

        model = IndicatorsModel.get_default ();
        var indicators_list = model.get_indicators ();

        foreach (Indicator.Object o in indicators_list)
        {
             load_indicator(o);
        }

        menubar.draw.connect (draw_background);

        destroy.connect (Gtk.main_quit);
    }

    private void create_entry (Indicator.ObjectEntry entry,
                               Indicator.Object      object)
    {
        //delete_entry(entry, object);
        Gtk.MenuItem menuitem = new IndicatorObjectEntry (entry, object);
        menuhash[model.get_indicator_name(object)] = menuitem;
        menubar.prepend (menuitem);
    }

    private void delete_entry(Indicator.ObjectEntry entry,
                               Indicator.Object      object)
    {
        print ("\n\n"+ model.get_indicator_name(object) +"\n\n");
        if (menuhash.has_key(model.get_indicator_name(object)))
        {
            var menuitem = menuhash[model.get_indicator_name(object)];
            menubar.remove (menuitem);
        }
    }

    private void on_entry_added (Indicator.Object      object,
                                 Indicator.ObjectEntry entry)
    {
        create_entry (entry, object);
    }

    private void on_entry_removed(Indicator.Object      object,
                                 Indicator.ObjectEntry entry)
    {
        delete_entry(entry, object);
    }

    public void load_indicator(Indicator.Object indicator) {
        if (indicator is Indicator.Object)
        {
            indicator.entry_added.connect (this.on_entry_added);
            indicator.entry_removed.connect (this.on_entry_removed);
            indicator.ref();

            unowned GLib.List<Indicator.ObjectEntry> list = indicator.get_entries ();

            for (int i = 0; i < list.length (); i++)
            {
                unowned Indicator.ObjectEntry entry = (Indicator.ObjectEntry) list.nth_data (i);
                this.create_entry (entry, indicator);
            }
        } else {
            warning ("Unable to load %s\n", model.get_indicator_name(indicator));
        }
    }

    bool draw_background (Gtk.Widget widget, Cairo.Context context) {
        Rectangle monitor_dimensions;
        get_screen().get_monitor_geometry(0, out monitor_dimensions);
        
        int width, natural;
        get_preferred_width(out width,out natural);
        bool right_align = widget.get_direction () == Gtk.TextDirection.LTR;
        //Cairo.Context context = widget.get_parent_window().cairo_create();
        if (right_align) {
            move (monitor_dimensions.width - width, 0);
        } else {
            move (0, 0);
        }
        //Gtk.cairo_transform_to_window(context,widget,this as Gdk.Window);
        context.set_operator(Cairo.Operator.CLEAR);
        // Makes the mask fill the entire window
        context.rectangle(0.0, 0.0, width,25);
        // Deletes everything in the window (sice the compositing operator is clear and mask fills the entire window
        context.fill();
        // Set the compositing operator back to the default
        context.set_operator(Cairo.Operator.OVER);

        if (right_align)
            rounded_bottom_left (context, 0, 0, width, 25, 16);
        else
            rounded_bottom_right (context, 0, 0, width, 25, 16);
        context.clip ();

        context.set_source_rgba (0.0, 0.0, 0.0, 0.9);
        context.set_operator (Cairo.Operator.OVER);
        context.paint ();
        (widget as Gtk.MenuBar).foreach((child)=>{
            child.draw (context);
            context.translate(child.get_allocated_width(),0);
        });
        context.translate(-widget.get_allocated_width(),0);
        /*
        context.set_source_rgba (1.0, 1.0, 1.0, 0.7);
        context.set_operator (Cairo.Operator.SOURCE);
        if (right_align)
            rounded_bottom_left_stroke (context, 0, 0, width, 25, 16);
        else
            rounded_bottom_right_stroke (context, 0, 0, width, 25, 16);
        context.stroke ();*/
        return true;


    }

    void rounded_bottom_left (Cairo.Context context, double x, double y,
        double width, double height, double radius) {
        context.move_to (x, y);
        /* Right Top */
        context.line_to (x + width, y);
        /* Right Bottom */
        context.line_to (x + width, y + height);
        /* Left Bottom */
        context.line_to (x + radius, y + height);
        context.curve_to (x, y + height, x, y + height, x, y + height - radius);
        /* Left Top */
        context.line_to (x, y);
    }

    void rounded_bottom_left_stroke (Cairo.Context context, double x, double y,
        double width, double height, double radius) {
        /* Start in the Bottom Right corner */
        context.move_to (x + width, y + height);
        /* Left Bottom */
        context.line_to (x + radius, y + height);
        context.curve_to (x, y + height, x, y + height, x, y + height - radius);
        /* Left Top */
        context.line_to (x, y);
    }

    void rounded_bottom_right (Cairo.Context context, double x, double y,
        double width, double height, double radius) {
        context.move_to (x, y);
        /* Right Top */
        context.line_to (x + width, y);
        /* Right Bottom */
        context.line_to (x + width, y + height - radius);
        context.curve_to (x + width, y + height, x + width,
                          y + height, x + width - radius, y + height);
        /* Left Bottom */
        context.line_to (x, y + height);
        /* Left Top */
        context.line_to (x, y);
    }

    void rounded_bottom_right_stroke (Cairo.Context context, double x, double y,
        double width, double height, double radius) {
        context.move_to (x + width, y);
        /* Right Bottom */
        context.line_to (x + width, y + height - radius);
        context.curve_to (x + width, y + height, x + width,
                          y + height, x + width - radius, y + height);
        /* Left Bottom */
        context.line_to (x, y + height);
    }


    static int main (string[] args) {
        Gtk.init (ref args);

        var app = new Unique.App ("org.elementary.Wingpanel", null);
        if (app.is_running()) {
            var response = app.send_message (Unique.Command.ACTIVATE, null);
            if (response == Unique.Response.OK)
                return 0;
            GLib.error (_("Failed to activate running instance"));
        }

        var panel = new Wingpanel.Panel ();
        panel.show_all ();

        Gtk.main ();

        return 0;
    }
}

